#!/usr/bin/env python3
"""jpj_market.py：用 JPJ 登记汇总 TSV 重算本项目的全部市场事实表（只用 Python 标准库）。

输入：malaysia-auto-ask 仓库冻结的 expected_aggregates.tsv（只读，不修改）。
  4 列、无表头：category, key, sub_key, count
  category ∈ total / month / state / fuel / maker / month_maker / month_fuel
  覆盖 2025-01 至 2026-08，共 1,436,804 次汽车登记。
  上游来源：data.gov.my「Car Registration Transactions」(JPJ，CC BY 4.0)。

口径提醒（已写进报告）：
  1. 一行 = 一次登记，不等于批发量、零售量或 MAA 的 TIV。
  2. 品牌按 JPJ 的 maker 标签统计，只合并大小写差异（BMW/Bmw、McLaren/Mclaren），
     不按集团合并。TSV 没有车型字段，因此无法拆出 Omoda/Jaecoo 车型。
  3. TSV 没有「品牌 × 燃料」交叉，不能算某品牌的纯电占比。
  4. 2026 年只有 1–8 月，同比只比较两年都有的 1–8 月。

用法：
  python jpj_market.py                              # 使用默认 TSV 路径，输出到脚本所在目录
  python jpj_market.py --tsv <路径> --out <目录>
  python jpj_market.py --check                      # 重算到临时目录，逐字节对比仓库里的 6 个 CSV，不一致就退出码 1

输出（UTF-8 带 BOM，Excel 直接打开不乱码）：
  jpj_market_summary.csv          关键指标（总量、份额、同比）
  jpj_market_brand_top15.csv      品牌排名前 15
  jpj_market_chery_monthly.csv    Chery + Jetour 月度登记与份额
  jpj_market_chinese_brands.csv   中国品牌口径表（每个 maker 标签的归类和合计）
  jpj_market_chinese_monthly.csv  中国品牌月度份额（主口径 / 含 MG、Smart 的敏感性口径）
  jpj_market_fuel_monthly.csv     纯电 / 混动月度份额
"""
from __future__ import annotations

import argparse
import csv
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

REPO_DIR = Path(__file__).resolve().parent
DEFAULT_TSV = REPO_DIR / "data" / "expected_aggregates.tsv"
OUTPUT_FILES = (
    "jpj_market_summary.csv",
    "jpj_market_brand_top15.csv",
    "jpj_market_chery_monthly.csv",
    "jpj_market_chinese_brands.csv",
    "jpj_market_chinese_monthly.csv",
    "jpj_market_fuel_monthly.csv",
)

# ---- 品牌归类（口径表；改动这里即可重算） ----
# 主口径「中国品牌」：品牌起源和母公司都在中国大陆。
CN_BRANDS = {
    "BYD", "Denza",                                   # 比亚迪
    "Chery", "Jetour", "Jaecoo", "iCaur", "Lepas",    # 奇瑞集团（Jetour 捷途、Jaecoo 捷酷、iCaur、Lepas 均为奇瑞旗下）
    "Great Wall",                                     # 长城
    "Zeekr",                                          # 吉利旗下极氪
    "Xpeng", "Leapmotor", "Neta",                     # 新势力
    "GAC", "GAC Aion", "GAC Hyptec", "GAC Motor", "Hycann",  # 广汽系
    "Foton", "BAIC", "BAW",                           # 北汽系
    "Dong Feng",                                      # 东风
    "TQ Wuling",                                      # 五菱
    "Maxus", "Weststar Maxus",                        # 上汽大通
    "JAC", "JMC", "King Long Xiamen", "Higer",        # 江淮、江铃、金龙、海格
    "Foday", "ZXAuto", "Seres", "Skyworth", "Shineray",
}
# 敏感性口径额外加入：中国企业控股、中国生产，但品牌起源不在中国。
CN_OWNED_FOREIGN_ORIGIN = {"MG", "Smart"}
# 其余标签：「其他」。下列标签来源不确定，单独列为「未分类」，报告中给出其上限影响。
UNCLASSIFIED = {"Cam", "Go Auto", "JMS", "Bison", "Xinneng", "Xiamen", "Yangtse", "EVEasy", "Standard"}

CHERY_PLUS_JETOUR = ("Chery", "Jetour")   # 任务口径：Chery + 子品牌 Jetour
EV_FUELS = ("electric",)
HYBRID_FUELS = ("hybrid_petrol", "hybrid_diesel")


def load(tsv: Path):
    """读取 TSV，返回各类别的计数字典；并做完整性校验。"""
    rows = []
    with tsv.open(encoding="utf-8", newline="") as f:
        for line_no, rec in enumerate(csv.reader(f, delimiter="\t"), start=1):
            if not rec:
                continue
            if len(rec) != 4:
                raise ValueError(f"第 {line_no} 行不是 4 列：{rec!r}")
            cat, key, sub, cnt = (x.strip() for x in rec)
            rows.append((cat, key, sub, int(cnt)))

    total = None
    month = Counter()                     # "YYYY-MM" -> n
    maker_raw = Counter()                 # 原始 maker 标签 -> n
    fuel = Counter()
    state = Counter()
    month_maker_raw = defaultdict(Counter)
    month_fuel = defaultdict(Counter)
    for cat, key, sub, n in rows:
        if cat == "total":
            total = n
        elif cat == "month":
            month[f"{key}-{sub}"] += n
        elif cat == "maker":
            maker_raw[key] += n
        elif cat == "fuel":
            fuel[key] += n
        elif cat == "state":
            state[key] += n
        elif cat == "month_maker":
            month_maker_raw[key][sub] += n
        elif cat == "month_fuel":
            month_fuel[key][sub] += n
        else:
            raise ValueError(f"未知类别：{cat}")

    # ---- 完整性校验：所有切片的合计必须一致 ----
    checks = {
        "maker 合计 = total": sum(maker_raw.values()) == total,
        "fuel 合计 = total": sum(fuel.values()) == total,
        "state 合计 = total": sum(state.values()) == total,
        "month 合计 = total": sum(month.values()) == total,
    }
    for m, n in month.items():
        checks[f"{m} month_maker 合计 = month"] = sum(month_maker_raw[m].values()) == n
        checks[f"{m} month_fuel 合计 = month"] = sum(month_fuel[m].values()) == n
    per_maker = Counter()
    for m in month_maker_raw:
        per_maker.update(month_maker_raw[m])
    checks["各月 month_maker 按品牌累加 = maker"] = per_maker == maker_raw
    failed = [k for k, ok in checks.items() if not ok]
    if failed:
        raise AssertionError("校验失败：" + "; ".join(failed))
    print(f"[校验] {len(checks)} 项全部通过；记录数 {total:,}；月份 {min(month)}–{max(month)}")

    # ---- 只合并大小写差异，保留出现次数最多的写法 ----
    by_lower = defaultdict(list)
    for name, n in maker_raw.items():
        by_lower[name.lower()].append((n, name))
    canon = {}
    for variants in by_lower.values():
        keep = max(variants)[1]
        for _, name in variants:
            canon[name] = keep
        if len(variants) > 1:
            print(f"[大小写合并] {sorted(v[1] for v in variants)} -> {keep}")
    maker = Counter()
    for name, n in maker_raw.items():
        maker[canon[name]] += n
    month_maker = defaultdict(Counter)
    for m, c in month_maker_raw.items():
        for name, n in c.items():
            month_maker[m][canon[name]] += n

    unknown_labels = (CN_BRANDS | CN_OWNED_FOREIGN_ORIGIN | UNCLASSIFIED) - set(maker)
    if unknown_labels:
        raise AssertionError(f"口径表里的标签在数据中不存在：{sorted(unknown_labels)}")
    return total, month, maker, fuel, month_maker, month_fuel


def pct(a: int, b: int, nd: int = 2) -> str:
    return f"{100 * a / b:.{nd}f}" if b else ""


def yoy(cur: int, prev: int) -> str:
    return f"{100 * (cur - prev) / prev:.1f}" if prev else ""


def write_csv(path: Path, header, rows):
    # 固定 LF 行尾：csv.writer 默认写 CRLF，而仓库按 .gitattributes 以 LF 保存，
    # 不固定的话重跑后每个文件的字节都会变。
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)
    print(f"[输出] {path.name}（{len(rows)} 行）")


def classify(name: str) -> str:
    if name in CN_BRANDS:
        return "中国品牌"
    if name in CN_OWNED_FOREIGN_ORIGIN:
        return "中国控股的非中国起源品牌"
    if name in UNCLASSIFIED:
        return "未分类"
    return "其他"


def main(argv=None) -> int:
    # Windows 繁体/简体控制台默认代码页可能无法输出中文日志，统一改为 UTF-8
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--tsv", type=Path, default=DEFAULT_TSV)
    ap.add_argument("--out", type=Path, default=REPO_DIR)
    ap.add_argument("--check", action="store_true",
                    help="重算到临时目录，逐字节对比 --out 目录（默认仓库根目录）里的 6 个 CSV，不一致则返回 1")
    args = ap.parse_args(argv)
    if args.check:
        return check(args.tsv, args.out)
    total, month, maker, fuel, month_maker, month_fuel = load(args.tsv)
    args.out.mkdir(parents=True, exist_ok=True)

    months = sorted(month)
    m25 = [m for m in months if m.startswith("2025-")]
    m26 = [m for m in months if m.startswith("2026-")]
    m25_same = [m for m in m25 if m.replace("2025-", "2026-") in m26]   # 2025 年与 2026 年都有的月份

    def maker_sum(names, ms):
        return sum(month_maker[m][n] for m in ms for n in names)

    def total_sum(ms):
        return sum(month[m] for m in ms)

    def fuel_sum(fs, ms):
        return sum(month_fuel[m][f] for m in ms for f in fs)

    # 1) 品牌排名前 15
    top = maker.most_common(15)
    rows = []
    for i, (name, n) in enumerate(top, 1):
        a25 = maker_sum([name], m25)
        a25s = maker_sum([name], m25_same)
        a26 = maker_sum([name], m26)
        rows.append([i, name, classify(name), n, pct(n, total), a25, pct(a25, total_sum(m25)),
                     a26, pct(a26, total_sum(m26)), a25s, yoy(a26, a25s)])
    write_csv(args.out / "jpj_market_brand_top15.csv",
              ["排名", "品牌(JPJ maker)", "归类", "登记量_2025-01至2026-08", "份额%_全期",
               "登记量_2025全年", "份额%_2025全年", "登记量_2026年1-8月", "份额%_2026年1-8月",
               "登记量_2025年1-8月", "同比%_1-8月"],
              rows)

    # 2) Chery + Jetour 月度
    rows = []
    for m in months:
        c, j = month_maker[m]["Chery"], month_maker[m]["Jetour"]
        rows.append([m, month[m], c, j, c + j, pct(c, month[m]), pct(c + j, month[m])])
    write_csv(args.out / "jpj_market_chery_monthly.csv",
              ["月份", "全市场登记", "Chery", "Jetour", "Chery+Jetour", "Chery份额%", "Chery+Jetour份额%"],
              rows)

    # 3) 中国品牌口径表 + 月度份额
    rows = []
    for name, n in maker.most_common():
        cls = classify(name)
        if cls != "其他":
            rows.append([name, cls, n, pct(n, total, 3)])
    write_csv(args.out / "jpj_market_chinese_brands.csv",
              ["品牌(JPJ maker)", "归类", "登记量_2025-01至2026-08", "份额%_全期"], rows)

    cn = sorted(CN_BRANDS)
    cn_broad = sorted(CN_BRANDS | CN_OWNED_FOREIGN_ORIGIN)
    rows = []
    for m in months:
        a, b = maker_sum(cn, [m]), maker_sum(cn_broad, [m])
        rows.append([m, month[m], a, pct(a, month[m]), b, pct(b, month[m])])
    write_csv(args.out / "jpj_market_chinese_monthly.csv",
              ["月份", "全市场登记", "中国品牌(主口径)", "份额%_主口径", "含MG/Smart", "份额%_含MG/Smart"], rows)

    # 4) 燃料月度
    rows = []
    for m in months:
        e, h = fuel_sum(EV_FUELS, [m]), fuel_sum(HYBRID_FUELS, [m])
        rows.append([m, month[m], e, pct(e, month[m]), h, pct(h, month[m])])
    write_csv(args.out / "jpj_market_fuel_monthly.csv",
              ["月份", "全市场登记", "纯电(electric)", "纯电份额%", "混动(hybrid_petrol+hybrid_diesel)", "混动份额%"],
              rows)

    # 5) 关键指标汇总
    MKT = "同期全市场"
    periods = (("2025-01至2026-08", months), ("2025全年", m25),
               ("2025年1-8月", m25_same), ("2026年1-8月", m26))

    def block(label, names=None, fuels=None):
        def val(ms):
            return maker_sum(names, ms) if names is not None else fuel_sum(fuels, ms)
        out = [[label, p, val(ms), pct(val(ms), total_sum(ms)), MKT] for p, ms in periods]
        out.append([label, "同比%(2026年1-8月 vs 2025年1-8月)", yoy(val(m26), val(m25_same)), "", ""])
        return out

    unc = sorted(UNCLASSIFIED)
    rows = [["全市场", p, total_sum(ms), "100.00", MKT] for p, ms in periods]
    rows.append(["全市场", "同比%(2026年1-8月 vs 2025年1-8月)", yoy(total_sum(m26), total_sum(m25_same)), "", ""])
    rows += block("Chery", names=["Chery"])
    rows += block("Jetour", names=["Jetour"])
    rows += block("Chery+Jetour", names=list(CHERY_PLUS_JETOUR))
    rows += block("中国品牌(主口径)", names=cn)
    rows += block("中国品牌(含MG/Smart)", names=cn_broad)
    rows += block("未分类标签(上限影响)", names=unc)
    rows += block("纯电(electric)", fuels=list(EV_FUELS))
    rows += block("混动(hybrid)", fuels=list(HYBRID_FUELS))
    # 6) 纯电归属下限：TSV 没有「品牌 × 燃料」交叉。把 BYD、Tesla 的全部登记都当成纯电（上界），
    #    纯电登记里来自其他品牌的部分至少为「纯电 − BYD − Tesla」。这是保守下限，不是估计值。
    for p, ms in periods:
        ev = fuel_sum(EV_FUELS, ms)
        rest = ev - maker_sum(["BYD", "Tesla"], ms)
        rows.append(["纯电中来自BYD/Tesla以外品牌(下限)", p, rest, pct(rest, ev), "同期纯电登记"])
    write_csv(args.out / "jpj_market_summary.csv", ["指标", "期间", "登记量或同比%", "占比%", "占比分母"], rows)
    return 0


def check(tsv: Path, committed_dir: Path) -> int:
    """重算到临时目录，逐字节对比已提交的 CSV。"""
    with tempfile.TemporaryDirectory() as tmp:
        main(["--tsv", str(tsv), "--out", tmp])
        bad = []
        for name in OUTPUT_FILES:
            ref = committed_dir / name
            if not ref.exists():
                bad.append(f"{name}：仓库里没有这个文件")
            elif ref.read_bytes() != (Path(tmp) / name).read_bytes():
                bad.append(f"{name}：与重算结果不一致")
    if bad:
        print("[check] 失败：" + "; ".join(bad))
        return 1
    print(f"[check] {len(OUTPUT_FILES)} 个 CSV 与重算结果逐字节一致")
    return 0


if __name__ == "__main__":
    sys.exit(main())
