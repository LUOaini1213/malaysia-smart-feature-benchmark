"""Pin the committed tables and the numbers quoted in README.md / report.md.

Stdlib only:  python -m unittest discover -s tests -v
"""
from __future__ import annotations

import contextlib
import csv
import io
import re
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import jpj_market  # noqa: E402


def read_text(name: str) -> str:
    return (ROOT / name).read_bytes().decode("utf-8")


def read_csv(name: str) -> list[dict]:
    with (ROOT / name).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def summary_value(label: str, period: str, col: str = "占比%") -> str:
    for row in read_csv("jpj_market_summary.csv"):
        if row["指标"] == label and row["期间"] == period:
            return row[col]
    raise KeyError((label, period))


def md_table(text: str, heading: str) -> list[list[str]]:
    """Rows (cells stripped, header and separator dropped) of the first table after `heading`."""
    start = text.index(heading)
    rows = []
    for line in text[start:].splitlines()[1:]:
        if line.startswith("|"):
            rows.append([c.strip() for c in line.strip().strip("|").split("|")])
        elif rows:
            break
    return rows[2:]


def num(s: str) -> str:
    return s.replace(",", "")


YOY = "同比%(2026年1-8月 vs 2025年1-8月)"


class Reproduction(unittest.TestCase):
    def test_regenerated_csvs_are_byte_identical(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                self.assertEqual(jpj_market.main(["--out", tmp]), 0)
            self.assertIn("[校验] 45 项全部通过；记录数 1,436,804", out.getvalue())
            for name in jpj_market.OUTPUT_FILES:
                with self.subTest(name=name):
                    self.assertEqual((Path(tmp) / name).read_bytes(), (ROOT / name).read_bytes())

    def test_check_flag_exit_codes(self):
        ok = subprocess.run([sys.executable, str(ROOT / "jpj_market.py"), "--check"],
                            capture_output=True)
        self.assertEqual(ok.returncode, 0, ok.stdout.decode("utf-8", "replace"))
        with tempfile.TemporaryDirectory() as tmp:
            for name in jpj_market.OUTPUT_FILES:
                data = (ROOT / name).read_bytes()
                if name == "jpj_market_summary.csv":
                    data = data.replace(b"\n", b"\r\n")   # same content, different bytes
                (Path(tmp) / name).write_bytes(data)
            bad = subprocess.run([sys.executable, str(ROOT / "jpj_market.py"), "--check", "--out", tmp],
                                 capture_output=True)
            self.assertEqual(bad.returncode, 1)


class HeadlineNumbers(unittest.TestCase):
    """Every market number on the first screen and in the report summary comes from jpj_market_summary.csv."""

    def test_summary_values(self):
        self.assertEqual(summary_value("全市场", "2025-01至2026-08", "登记量或同比%"), "1436804")
        self.assertEqual(summary_value("Chery+Jetour", "2025年1-8月"), "3.92")
        self.assertEqual(summary_value("Chery+Jetour", "2026年1-8月"), "5.07")
        self.assertEqual(summary_value("Chery+Jetour", YOY, "登记量或同比%"), "32.8")
        self.assertEqual(summary_value("Jetour", YOY, "登记量或同比%"), "538.6")
        self.assertEqual(summary_value("Chery", YOY, "登记量或同比%"), "3.7")
        self.assertEqual(summary_value("纯电(electric)", "2025年1-8月"), "4.24")
        self.assertEqual(summary_value("纯电(electric)", "2026年1-8月"), "8.38")
        self.assertEqual(summary_value("纯电中来自BYD/Tesla以外品牌(下限)", "2026年1-8月"), "76.41")

    def test_readme_quotes_summary(self):
        readme = read_text("README.md")
        for s in ("1,436,804", "3.92%", "5.07%", "+538.6%", "+3.7%", "4.24%", "8.38%"):
            with self.subTest(s=s):
                self.assertIn(s, readme)
        # the derived AEB ceiling: 16 of 23.5 Safety Assist points
        self.assertEqual(round(100 * 16 / 23.5), 68)
        self.assertIn("68%", readme)

    def test_report_summary_quotes_summary(self):
        report = read_text("report.md")
        for s in ("3.92%", "5.07%", "+32.8%", "+538.6%", "+3.7%", "4.24%", "8.38%", "76.4%", "1,436,804"):
            with self.subTest(s=s):
                self.assertIn(s, report)

    def test_report_table_3_3(self):
        rows = {r[0]: r[1:] for r in md_table(read_text("report.md"), "### 3.3")}
        expect = {
            "Chery+Jetour 份额": "Chery+Jetour",
            "其中 Chery": "Chery",
            "其中 Jetour": "Jetour",
            "中国品牌份额（主口径）": "中国品牌(主口径)",
            "中国品牌份额（含 MG、Smart）": "中国品牌(含MG/Smart)",
            "纯电份额": "纯电(electric)",
            "混动份额": "混动(hybrid)",
        }
        self.assertEqual(set(rows), set(expect))
        for md_label, csv_label in expect.items():
            with self.subTest(row=md_label):
                a25, a26, y = rows[md_label]
                self.assertEqual(a25, summary_value(csv_label, "2025年1-8月") + "%")
                self.assertEqual(a26, summary_value(csv_label, "2026年1-8月") + "%")
                self.assertTrue(y.endswith(summary_value(csv_label, YOY, "登记量或同比%") + "%"), y)

    def test_report_table_3_1_matches_top15(self):
        rows = md_table(read_text("report.md"), "### 3.1")
        ref = read_csv("jpj_market_brand_top15.csv")
        self.assertEqual(len(rows), 15)
        for md, r in zip(rows, ref):
            with self.subTest(brand=r["品牌(JPJ maker)"]):
                self.assertEqual(md, [r["排名"], r["品牌(JPJ maker)"], r["归类"],
                                      md[3], r["份额%_全期"], r["份额%_2025全年"],
                                      r["份额%_2026年1-8月"], r["同比%_1-8月"]])
                self.assertEqual(num(md[3]), r["登记量_2025-01至2026-08"])

    def test_report_table_3_2_matches_monthly(self):
        rows = md_table(read_text("report.md"), "### 3.2")
        chery = read_csv("jpj_market_chery_monthly.csv")
        cn = read_csv("jpj_market_chinese_monthly.csv")
        fuel = read_csv("jpj_market_fuel_monthly.csv")
        self.assertEqual(len(rows), 20)
        for md, c, k, f in zip(rows, chery, cn, fuel):
            with self.subTest(month=c["月份"]):
                self.assertEqual([md[0], num(md[1]), num(md[2]), num(md[3])] + md[4:],
                                 [c["月份"], c["全市场登记"], c["Chery"], c["Jetour"],
                                  c["Chery+Jetour份额%"], k["份额%_主口径"], f["纯电份额%"], f["混动份额%"]])


class StructuralCounts(unittest.TestCase):
    def test_feature_matrix(self):
        rows = read_csv("feature_matrix.csv")
        self.assertEqual(len(rows), 161)
        self.assertEqual(len({r["车型"] for r in rows}), 7)
        self.assertEqual(len({r["功能项"] for r in rows}), 23)
        self.assertEqual(len({(r["车型"], r["功能项"]) for r in rows}), 161)
        unverified = [r for r in rows if r["来源类型"] == "未核实"]
        sourced = [r for r in rows if r["来源类型"] != "未核实"]
        self.assertEqual((len(sourced), len(unverified)), (110, 51))
        for r in sourced:
            with self.subTest(cell=(r["车型"], r["功能项"])):
                self.assertRegex(r["来源URL"], r"^https?://")
                self.assertTrue(r["证据摘录"].strip())
                self.assertRegex(r["来源编号"], r"^S\d+(;S\d+)*$")
        for r in unverified:
            self.assertTrue(r["取值"].startswith("未核实"), r)
        readme, report = read_text("README.md"), read_text("report.md")
        self.assertIn("110 of 161 cells", readme)
        self.assertIn("161 格：110 格", readme)
        self.assertIn("其中 110 格有官方来源和原文摘录，51 格为「未核实」", report)

    def test_regulation_requirements(self):
        rows = read_csv("regulation_requirements.csv")
        self.assertEqual(len(rows), 46)
        self.assertEqual(len({r["编号"] for r in rows}), 46)
        for r in rows:
            with self.subTest(id=r["编号"]):
                self.assertRegex(r["来源URL"], r"^https?://")
        self.assertIn("46 条要求", read_text("README.md"))

    def test_source_ids_resolve(self):
        report = read_text("report.md")
        defined = [int(n) for n in re.findall(r"^- \[S(\d+)\]", report, flags=re.M)]
        self.assertEqual(defined, list(range(1, 42)))     # S1..S41, in order
        self.assertIn("41 条编号来源", read_text("README.md"))
        cited = set()
        for name in ("report.md", "sor_priority.md"):
            cited |= {int(n) for n in re.findall(r"\bS(\d+)\b", read_text(name))}
        for name in ("feature_matrix.csv", "regulation_requirements.csv"):
            for r in read_csv(name):
                cited |= {int(n) for n in re.findall(r"S(\d+)", r["来源编号"])}
        self.assertLessEqual(cited, set(defined), sorted(cited - set(defined)))

    def test_sor_items(self):
        ids = sorted(set(re.findall(r"SOR-(\d+)", read_text("sor_priority.md"))))
        self.assertEqual(ids, [f"{i:02d}" for i in range(1, 24)])
        self.assertIn("共 23 条", read_text("README.md"))


class Hygiene(unittest.TestCase):
    LOCAL_PATH = re.compile(r"(?<![A-Za-z])[A-Za-z]:[\\/][^\s]|[\\/]Users[\\/]|/home/[a-z]")

    def test_no_local_paths_in_tracked_text(self):
        files = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True,
                               check=True).stdout.split()
        hits = []
        for name in files:
            if not name.endswith((".md", ".py", ".csv", ".txt", ".yml", ".toml")):
                continue
            for i, line in enumerate(read_text(name).splitlines(), 1):
                if self.LOCAL_PATH.search(line.replace("https://", "").replace("http://", "")):
                    hits.append(f"{name}:{i}")
        self.assertEqual(hits, [])


if __name__ == "__main__":
    unittest.main()
