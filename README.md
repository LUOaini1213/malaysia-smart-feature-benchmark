# 马来西亚 / 东南亚市场智能化功能需求与法规对标

> **English summary.** A requirements and regulation benchmark for ADAS and cockpit features in Malaysia / Southeast Asia: a reproducible market analysis of Malaysian JPJ vehicle registrations (Jan 2025 – Aug 2026, 1,436,804 registrations), 46 requirements from official sources (ASEAN NCAP 2026–2030 including IVASA, EU GSR, UN R152/R79/R156, Malaysia's VTA), a 7-model feature matrix with a source URL and quote for every cell, and a P0/P1/P2 feature-priority list in SOR style. Facts and recommendations are kept apart, and anything not found in an official source is marked "未核实" (unverified).

个人项目（2026-10），使用 AI 工具辅助完成。练习的工作内容：梳理海外市场需求、做技术方案可行性分析、跟踪海外法规与竞品、规划智能功能迭代。

## 做了什么

1. **市场**：用 JPJ 登记汇总（2025-01 至 2026-08，共 1,436,804 次登记）算出品牌排名、奇瑞系和中国品牌的份额、纯电份额及趋势。脚本可以重跑，并带 45 项一致性校验。
2. **法规与评级**：整理了 46 条要求，来源只用官方文件，覆盖 ASEAN NCAP 2026–2030 规程与 IVASA、欧盟 GSR (EU) 2019/2144 及其实施细则、UN R152/R79/R156 等、马来西亚 JPJ 的 VTA 型式认证。每条都有条款、生效日期或版本，以及来源 URL。
3. **竞品**：从马来西亚官网和官方手册收集 7 款 SUV 的智驾与座舱配置，共 23 项、161 格，每格有 URL 和原文摘录，查不到的标「未核实」。车型为 Jaecoo J7、Omoda E5、Proton X50、Perodua Ativa、Toyota Corolla Cross、Honda HR-V、BYD Atto 3。
4. **综合**：按 SOR 格式写了「功能需求优先级 + 可行性备注」，分 P0/P1/P2 共 23 条，事实和建议分开写。

## 主要发现（出处见 report.md）

- **马来西亚还没有强制乘用车装 AEB。**JPJ 2025-11 的报告把 UN R152 列为「未来实施、需进一步与国内产业协商」，M1 现行强制的是 ESC（R140）。
- **实际推动 AEB 上车的是 ASEAN NCAP。**没有 AEB 时，Safety Assist 最多约 68%，达不到 5 星门槛 75%（按官方分值推算）。Proton X90 改款去掉 ADAS 后，5 星被撤销，重评为 1 星。
- **座舱有了官方评价。**ASEAN NCAP 与中国汽车工程研究院推出的 IVASA 分英语和本地语言测语音，也测 DMS。竞品里只有 Proton 官方写明支持马来语语音，只有奇瑞系官方列出 DMS。
- **奇瑞系份额上升，但增量主要来自 Jetour。**Chery+Jetour 的份额从 3.92% 升到 5.07%（两年 1–8 月对比），其中 Jetour +538.6%，Chery 品牌 +3.7%。纯电份额从 4.24% 翻倍到 8.38%。

## 文件

| 文件 | 内容 |
|---|---|
| `report.md` | 完整分析：方法、市场、法规、竞品、综合、未核实清单，以及 41 条编号来源 |
| `sor_priority.md` | 功能需求优先级和可行性备注（SOR 摘要） |
| `regulation_requirements.csv` | 法规与评级要求清单：功能 × 来源 × 要求 × 生效日期 × 核实状态 |
| `feature_matrix.csv` | 竞品配置矩阵（长表），逐格附 URL、来源类型和原文摘录 |
| `jpj_market.py` | 从 TSV 重算所有市场表的脚本（只用 Python 标准库） |
| `jpj_market_*.csv` | 脚本输出：summary、brand_top15、chery_monthly、chinese_brands、chinese_monthly、fuel_monthly |
| `data/expected_aggregates.tsv` | 脚本的输入：JPJ 登记汇总快照（来源和许可见 `data/README.md`） |

CSV 都是 UTF-8 带 BOM，Excel 可以直接打开。

## 如何重跑市场数据

需要 Python 3.10 以上，不用安装第三方包。在仓库根目录执行：

```bash
python jpj_market.py
# 或者指定输入和输出位置
python jpj_market.py --tsv data/expected_aggregates.tsv --out .
```

- **校验**：脚本先检查各切片合计是否一致（品牌、燃料、地区、月份合计都等于总数，每月的「品牌」「燃料」切片合计也等于当月总数），通过后才写 CSV。
- **中国品牌口径**：口径表在脚本顶部的 `CN_BRANDS`，改完重跑即可。
- **刷新数据**：输入是 [malaysia-auto-ask](https://github.com/LUOaini1213/malaysia-auto-ask) 仓库冻结的快照（截至 2026-08-31）。data.gov.my 已更新到 2026-09-30，要用新数据，需先用该仓库的管线重新生成 TSV。
- **复现**：用 `data/` 里的快照重跑，6 个 `jpj_market_*.csv` 与仓库里的版本逐字节一致（2026-10-27 验证）。

## 核实规则和局限

- **核实规则**
  - 只认官方来源：ASEAN NCAP 官网、EUR-Lex 或欧盟出版局文本、UN 条约库、JPJ 官员报告、品牌马来西亚官网或手册。
  - 官网没写不等于没有：只有规格表明确标「-」才写「无」，否则写「未核实」。
- **数据局限**
  - JPJ 登记量不是销量。
  - TSV 没有车型字段，所以所选车型是否为各品牌销量第一未核实，Omoda/Jaecoo 记在哪个 maker 标签下也未核实。
- **配置核实范围**：只核实了最高配，51 格配置未核实，主要是语音语言、OTA、CPD、DMS、部分 ASEAN NCAP 评级。完整清单见 report.md 第 7 节。
- **定位**：这是个人练习，不代表任何车企的立场或内部 SOR。

## 许可

- 代码与文档：MIT（见 `LICENSE`）。
- 数据：JPJ 登记数据来自 data.gov.my，按 CC BY 4.0 开放，署名见 `data/README.md`。配置矩阵引用的是各品牌官网和手册的公开信息，每格附来源 URL。
