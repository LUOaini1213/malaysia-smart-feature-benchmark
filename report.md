# 马来西亚 / 东南亚市场智能化功能需求与法规对标

作者：罗文杰｜完成日期：2026-10-27｜个人项目，使用 AI 工具辅助完成。

> 写作规则：每条事实都标出处，编号见第 8 节。官方文件里查不到的写「未核实」。我自己的推断标【推论】。市场数字只来自 JPJ 登记汇总 TSV，并可用 `jpj_market.py` 重新算出。

---

## 1. 摘要

1. **马来西亚还没有强制乘用车装 AEB。**
   - JPJ 2025 年 11 月的报告把 UN R152（M1/N1 AEB）放在「未来实施、需进一步与国内产业协商」一栏 [S30]。同一报告「ADAS 现行实施」页里，对 M1 的强制项只有 ESC（UN R140，2020-07-01 起）。
   - 按 UN 条约库，马来西亚从 2020-01-22 起「适用」R152 [S25]。这只表示马来西亚可以按 R152 发证、承认他国按 R152 发的证，不等于强制装配。
2. **ASEAN NCAP 实际上是在逼 AEB 上车。**
   - 2026–2030 规程中，Safety Assist 满分 23.5，5 星要求该项达到 75% [S5][S6]。
   - 【推算】没有 AEB 时这一项最多 16 分，约 68%，拿不到 5 星。
   - 2026 年 3 月，Proton X90 改款取消了 AEB、LKA、盲区监测等功能，原 5 星被撤销，重评为 1 星 [S12]。
3. **智能座舱开始有官方评价。**
   - ASEAN NCAP 和中国汽车工程研究院（CAERI）推出了 IVASA。座舱规程分英语和本地语言测语音唤醒率、识别率、响应时间，也测 DMS [S14][S15]。首批结果计划 2026 年 10 月发布 [S13]。
   - 竞品中只有 Proton X50 官方写明支持马来语和英语语音 [S34]；只有奇瑞系的 J7 和 E5 官方列出 DMS [S32][S33]。
4. **奇瑞系份额上升，但增长主要来自 Jetour。**
   - Chery+Jetour 的登记份额从 2025 年 1–8 月的 3.92% 升到 2026 年同期的 5.07%，同比 +32.8%。其中 Jetour +538.6%，Chery 品牌 +3.7% [S1]。
   - 同期纯电份额从 4.24% 升到 8.38%。2026 年 1–8 月的纯电登记中，至少 76.4% 不是 BYD 或 Tesla 的（保守下限）[S1]。
5. **7 款对标车里，没有一款官方列出传感器式儿童遗留检测（CPD）。**ASEAN NCAP 2026–2030 中 CPD 最高 5 分 [S9]，对奇瑞是一个可以做出差异的点（见 SOR-09）。

---

## 2. 范围、数据和方法

| 项目 | 做法 |
|---|---|
| 市场数据 | 只用 [S1]：JPJ 登记汇总 TSV，覆盖 2025-01 至 2026-08，共 1,436,804 次登记，上游是 data.gov.my 的 Car Registration Transactions [S2]。用 `jpj_market.py`（只用 Python 标准库）重算，并做 45 项合计一致性校验。 |
| 口径 | 一行等于一次登记，不等于销量或 MAA 的 TIV。品牌按 JPJ 的 maker 标签计，只合并大小写（BMW/Bmw、McLaren/Mclaren）。TSV 没有车型字段，也没有「品牌 × 燃料」交叉。 |
| 法规和评级 | 只用官方文件：ASEAN NCAP 官网的协议 PDF、技术公告和新闻；EUR-Lex 文本；UN Regulation 正文（欧盟官方公报转载的 UNECE 文本）和 UN 条约库；JPJ 官员在 JASIC 论坛的报告。EUR-Lex 和 unece.org 拒绝脚本访问，所以欧盟文本是通过欧盟出版局 Cellar 接口按 CELEX 号拿的同一份官方文本。 |
| 选车规则 | 品牌按 TSV 排名选（Perodua、Proton、Toyota、Honda、Chery、BYD），每个品牌选一款官网在售的 SUV。奇瑞系选 Jaecoo J7。Omoda 5 已不在马来西亚官网，换成 Omoda E5。TSV 没有车型字段，所以这些车型是不是各品牌销量最高的车型**未核实**。都取官网最高配。 |
| 配置核实 | 每格都要有官方 URL 和一句原文摘录，否则写「未核实」。官网没提到不等于没有：只有规格表明确标「-」才写「无」。访问日期都是 2026-10-27。 |

---

## 3. 市场事实（JPJ 登记数据）

### 3.1 品牌排名前 15（2025-01 至 2026-08）

| 排名 | 品牌 | 归类 | 2025-01至2026-08 | 份额% | 2025全年份额% | 2026年1-8月份额% | 1-8月同比% |
|---|---|---|---:|---:|---:|---:|---:|
| 1 | Perodua | 其他 | 579,463 | 40.33 | 41.36 | 38.75 | -5.2 |
| 2 | Proton | 其他 | 286,730 | 19.96 | 17.42 | 23.86 | 38.5 |
| 3 | Toyota | 其他 | 202,013 | 14.06 | 14.83 | 12.87 | -9.4 |
| 4 | Honda | 其他 | 112,680 | 7.84 | 8.67 | 6.56 | -20.3 |
| 5 | Chery | 中国品牌 | 52,872 | 3.68 | 3.64 | 3.74 | 3.7 |
| 6 | Mitsubishi | 其他 | 22,680 | 1.58 | 1.59 | 1.56 | -4.2 |
| 7 | BYD | 中国品牌 | 21,879 | 1.52 | 1.66 | 1.32 | 1.1 |
| 8 | Mazda | 其他 | 17,440 | 1.21 | 1.10 | 1.39 | 40.7 |
| 9 | Mercedes Benz | 其他 | 13,954 | 0.97 | 1.03 | 0.88 | -20.9 |
| 10 | BMW | 其他 | 11,863 | 0.83 | 0.90 | 0.70 | -21.5 |
| 11 | Tesla | 其他 | 11,015 | 0.77 | 0.84 | 0.66 | 18.1 |
| 12 | Great Wall | 中国品牌 | 10,484 | 0.73 | 0.68 | 0.81 | 38.2 |
| 13 | Lexus | 其他 | 10,346 | 0.72 | 0.69 | 0.76 | 8.0 |
| 14 | Jetour | 中国品牌 | 10,246 | 0.71 | 0.32 | 1.32 | 538.6 |
| 15 | Isuzu | 其他 | 9,994 | 0.70 | 0.78 | 0.57 | -22.8 |

同比只比较两年都有数据的 1–8 月。全市场 2026 年 1–8 月同比 +2.8%（566,616 次 vs 551,365 次）。

### 3.2 月度趋势：奇瑞系、中国品牌、纯电

| 月份 | 全市场 | Chery | Jetour | Chery+Jetour份额% | 中国品牌份额% | 纯电份额% | 混动份额% |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2025-01 | 53,926 | 1,678 | 1 | 3.11 | 5.49 | 3.14 | 4.17 |
| 2025-02 | 67,320 | 2,435 | 0 | 3.62 | 5.31 | 3.21 | 3.14 |
| 2025-03 | 77,103 | 2,713 | 1 | 3.52 | 6.10 | 3.86 | 3.60 |
| 2025-04 | 65,190 | 2,285 | 56 | 3.59 | 6.63 | 4.44 | 3.48 |
| 2025-05 | 74,381 | 2,562 | 71 | 3.54 | 6.43 | 5.58 | 3.62 |
| 2025-06 | 58,840 | 2,493 | 270 | 4.70 | 7.99 | 5.56 | 3.52 |
| 2025-07 | 75,635 | 2,643 | 402 | 4.03 | 6.75 | 3.69 | 3.27 |
| 2025-08 | 78,970 | 3,636 | 374 | 5.08 | 8.10 | 4.38 | 3.67 |
| 2025-09 | 62,587 | 2,219 | 322 | 4.06 | 7.80 | 5.64 | 3.83 |
| 2025-10 | 81,404 | 2,967 | 321 | 4.04 | 8.42 | 5.34 | 3.44 |
| 2025-11 | 77,865 | 2,379 | 327 | 3.48 | 7.85 | 6.96 | 3.27 |
| 2025-12 | 96,967 | 3,656 | 598 | 4.39 | 9.60 | 8.38 | 4.01 |
| 2026-01 | 67,989 | 2,968 | 593 | 5.24 | 8.94 | 9.18 | 3.17 |
| 2026-02 | 56,683 | 2,133 | 297 | 4.29 | 6.81 | 6.41 | 3.90 |
| 2026-03 | 67,823 | 2,643 | 790 | 5.06 | 7.99 | 6.95 | 6.03 |
| 2026-04 | 77,819 | 2,956 | 1,197 | 5.34 | 9.13 | 7.57 | 6.35 |
| 2026-05 | 66,053 | 2,576 | 968 | 5.37 | 9.45 | 7.63 | 7.73 |
| 2026-06 | 72,943 | 2,698 | 1,203 | 5.35 | 9.63 | 8.52 | 7.74 |
| 2026-07 | 80,030 | 2,588 | 1,216 | 4.75 | 8.81 | 8.67 | 7.02 |
| 2026-08 | 77,276 | 2,644 | 1,239 | 5.02 | 7.97 | 11.43 | 6.42 |

### 3.3 关键指标（两年 1–8 月对比）

| 指标 | 2025年1-8月 | 2026年1-8月 | 同比 |
|---|---:|---:|---:|
| Chery+Jetour 份额 | 3.92% | 5.07% | 登记 +32.8% |
| 其中 Chery | 3.71% | 3.74% | +3.7% |
| 其中 Jetour | 0.21% | 1.32% | +538.6% |
| 中国品牌份额（主口径） | 6.63% | 8.64% | +33.9% |
| 中国品牌份额（含 MG、Smart） | 6.93% | 8.97% | +33.0% |
| 纯电份额 | 4.24% | 8.38% | +103.1% |
| 混动份额 | 3.54% | 6.13% | +77.7% |

**怎么解读**
- **奇瑞系增长靠 Jetour。**Jetour 从 2025 年 4 月开始有规模登记（56 次），2026 年 4–8 月每月 968–1,239 次；Chery 品牌的份额基本持平。
- **中国品牌份额提高了约 2 个百分点**，排名前 15 中有 Chery、BYD、Great Wall、Jetour。BYD 2026 年 1–8 月同比只有 +1.1%，份额从 2025 年全年的 1.66% 降到 1.32%。
- **纯电增量不靠 BYD/Tesla。**TSV 没有「品牌 × 燃料」交叉，没法直接算每个品牌的纯电量。保守算法：把 BYD 和 Tesla 2026 年 1–8 月的全部登记（7,472 + 3,733）都当成纯电，同期 47,508 次纯电登记中仍至少有 36,303 次（76.4%）来自其他品牌。具体是哪些品牌，要用明细里的 model 字段才能拆（本项目未做）。

**口径限制**
- **Omoda/Jaecoo 的登记标签**：TSV 中 "Jaecoo" 标签只有 3 次登记。Omoda/Jaecoo 车型是否记在 "Chery" 标签下，要用明细的 model 字段核实（未核实）。
- **state 字段**：表示办理登记的 JPJ 办公室或合作门户，不是车主所在地 [S2]。其中 Rakan Niaga（门户）占 1,244,912 次，所以本项目不做地区分析。
- **中国品牌归类**：口径表写在脚本里。主口径只算起源和母公司都在中国的品牌，不含 Proton、Volvo、Lotus 等。另有 9 个标签来源不确定，合计 1,306 次，即使全算进去，全期份额最多改变 0.09 个百分点。
- **混动**：数据字典里的 hybrid 指「可以用电或燃料驱动的混合动力车」[S2]，没有区分 HEV 和 PHEV。

---

## 4. 法规和评级要求

完整清单见 [regulation_requirements.csv](regulation_requirements.csv)，共 46 行。每行都有文件条款、生效日期或版本、来源 URL 和核实状态。

### 4.1 ASEAN NCAP 2026–2030（评级，自愿参评）

- **总体规则** [S5]
  - 四个支柱：AOP 40%（32 分）、COP 20%（54 分）、SA 20%（23.5 分）、MS 20%（24 分 [S8]）。
  - 5 星要求四个支柱分别达到 80% / 75% / 75% / 55%。
- **Safety Assist v3.2（From January 2026）**[S6]

  | 项目 | 分值 | 要点 |
  |---|---|---|
  | 安全带提醒 SBR | 6 | 前后排全覆盖且有座椅占用检测才是满分系数 |
  | ESC/ABS（EBA） | 6 | |
  | AEB 车对车 | 2.5 + 5.0 | CCRs 2.5；CCRm/CCRb 5.0，前提是默认开启、不能单次短按关闭、至少工作到 60 km/h |
  | 车道支持 | 2 | 本周期新增 |
  | Advanced SAT | 上限 2 | 包括 AEB 行人、MCB、SAS、DSM、RCTA/RCTB；每项 1 分，不做实车试验 |

- **适配评级系统 FRS v2.0** [S7]
  - 标配系数 1，选配 0.5，所以「全系标配」直接影响分数。
  - 马来西亚、泰国、印尼同属 Sector 1，每国 Country Score 为 3。
  - FRS v2.0 和 SA v3.2 对车道支持 2 分的拆分写法不一致（LKA 1.5 + LDW 0.5，对 LDW 1.0 + LKA 1.0），是官方文件之间的差异。
- **Motorcyclist Safety v2.0（东盟特有）**[S8]

  | 项目 | 分值 | 要点 |
  |---|---|---|
  | 盲区技术 BST | 8 | 检测式和影像式同分 |
  | AEB 车对摩托车 | 6 | 场景：追尾、转弯穿越、路口、对向车道偏离 |
  | 后视增强 ARV | 3 | |
  | AHB / ADB | 3 | |
  | 行人保护 | 2 | |
  | Advanced MST | 2 | |

- **Child Occupant Protection v3.3（From May 2026）**[S9]
  - CPD 最高 5 分：直接感知 5 分或 4 分，间接提醒 2.5 分。
  - 锁车后 3 分钟内须首次通知，例如手机推送。
  - 评估方法另见技术公告 ATB003（2026-07-09）[S11]。
- **星级有效期** [S10][S12]
  - 默认最长 6 年；删减标配或改成选配可以让星级提前失效。
  - Proton X90 是实例：原 5 星被撤销，改款重评为 1 星。
- **IVASA（不影响星级）**[S13][S14][S15]
  - 三部分：基础驾驶辅助、公开道路智能驾驶辅助、智能座舱交互；结果分 5 档。
  - 座舱规程测 DMS（注视 3 个分心点 5 s、闭眼 5 s）和语音（免唤醒、连续对话，英语和本地语言各测唤醒率、识别率、响应时间，以及行驶中语音安全指令）。
  - 「本地语言」具体指哪种语言，文件没写（未核实）。
- **结果库状态** [S16]
  - 截至访问日，ASEAN NCAP 官方结果库的协议筛选项只有 2012–2016、2017–2020、2021–2025 三个，未见 2026–2030 规程下的结果。
  - 新闻标题显示 Jetour T2（2026-01-09）、T1（2026-01-26）获 ASEAN NCAP 5 星 [S41]。

### 4.2 欧盟 GSR（Regulation (EU) 2019/2144，合并文本 2026-08-02）

Annex II 的日期代码有两个日期：第一个起拒绝新车型型式批准，第二个起禁止不合规新车注册 [S17]。
- 代码 B：2022-07-06 / 2024-07-07
- 代码 C：2024-07-07 / 2026-07-07

| 功能（M1/N1） | 代码 | 实施细则 | 关键技术要求 |
|---|---|---|---|
| AEB 车对车/障碍物 | B | UN R152 | 见 4.3 |
| AEB 行人/骑行者 | C | UN R152 | 见 4.3 |
| ELKS | B | (EU) 2021/646 [S21] | LDWS 65–130 km/h；纠偏转向 70–130 km/h，越线不超过 0.3 m |
| ISA | B | (EU) 2021/1958 [S18] | 限速信息 + 超速警告或速度控制；可关闭，每次上电恢复；语音提示须能设为任一欧盟官方语言 |
| DDAW | B | (EU) 2021/1341 [S19] | 70 km/h 以上启用；KSS ≥ 8 必须报警；不得用生物识别 |
| ADDW | C | (EU) 2023/2590 [S20] | 20 km/h 以上启用；≥50 km/h 视线离开 3.5 s 须报警；可以用摄像头，但不得识别身份 |
| 倒车检测 / EDR / 网络安全 | B | UN R158 / (EU) 2022/545 + UN R160 / UN R155 | — |

- **盲区监测**：GSR 对乘用车没有强制；BSIS（R151）只适用于 M2、M3、N2、N3。
- **儿童遗留检测**：GSR 合并文本中检索不到 CPD 条目。
- **UN R156**：合并文本的 Annex II 没有列 R156。欧盟是否通过其他法规强制 R156，本项目未核实。

### 4.3 UNECE 技术法规

- **UN R152（02 系列，Supplement 3）** [S22]
  - 车对车：10–60 km/h 内工作；碰撞预警最迟在紧急制动前 0.8 s；制动需求 ≥ 5.0 m/s²。
  - M1 避撞要求：最大质量下 ≤40 km/h、整备质量下 ≤42 km/h 须完全避撞；60 km/h 时碰撞速度 ≤35 km/h。
  - 行人：同样的避撞要求。
  - 自行车（02 系列新增）：最大质量下 ≤38 km/h 须完全避撞；60 km/h 时碰撞速度 ≤40 km/h。
  - 手动关闭要至少两步操作，10 km/h 以上不能手动关闭。
  - R152 的场景只有车、行人、自行车，不含摩托车。
- **UN R79（03 系列）**[S23]
  - ACSF B1 类（车道内保持）：脱手 15 s 内视觉警告，30 s 内红色图标加声音警告，声音警告开始后 30 s 内系统退出。
  - 已有 04 系列，变化未核对。
- **UN R171 DCAS**：2024-09-22 生效 [S29]，技术条款未读（部分核实）。
- **UN R156** [S24]
  - RXSWIN 唯一可识别、可经 OBD 读取、防篡改。
  - 升级失败能回滚或进入安全状态；电量不足不升级。
  - 升级前告知用户：目的、功能变化、预计时长、期间不可用的功能、操作说明。
- **马来西亚的适用日期**（UN 条约库）：R79 为 2006-02-03，R152 为 2020-01-22，R155/R156 为 2021-01-22，R171 为 2024-09-22 [S25–S29]。

### 4.4 马来西亚 JPJ（VTA 型式认证）

- **VTA 总体**：新车型上市前强制，依据 135 项 UNR 和 12 项马来西亚标准（MS）[S30]。
- **现行强制**（2020-07-01 起）[S30]
  - 新 M1 必须装 ESC（UN R140）。
  - 装了 LDWS 的 M1 须符合 UN R130。
  - 装了 AEBS 的重型车须符合 UN R131。
- **未来实施**：以下法规都标注「需进一步与国内产业协商」[S30]
  - UN R139（制动辅助）
  - UN R151（盲区）
  - UN R152（M1/N1 AEB）
  - UN R157（ALKS）
  - UN R158（倒车）
  - UN R159（起步信息）
  - UN R166（前侧方近距弱势道路使用者感知）
- **2022 年的提议**：JPJ 提议新增 13 项 UNR，含 R152、R155、R156、R157 [S31]。目前是否已列入 VTA 强制，未核实。
- **未见要求的功能**：CPD、DMS、ISA 在所查 JPJ 文件中都没有出现。

### 4.5 功能 × 来源总览

| 功能 | ASEAN NCAP 2026–2030 | 欧盟 GSR（所有新车） | UNECE | 马来西亚 JPJ |
|---|---|---|---|---|
| AEB 车对车 | SA 7.5 分 [A02] | 2024-07-07 [E01] | R152 [U01] | 未强制，列入未来实施 [M05] |
| AEB 行人/骑行者 | Advanced SAT，合计 ≤2 分 [A03] | 2026-07-07 [E02] | R152 [U01] | 同上 |
| AEB 车对摩托车 | MS 6 分 [A04] | 无 | R152 不覆盖 | 无 |
| 车道支持 | SA 2 分 [A05] | ELKS 2024-07-07 [E03] | R79、R130 | R130 若装配须合规 [M03] |
| L2 车道居中 | IVASA（独立评价）[A18] | 无强制 | R79 B1、R171 [U02][U03] | 未见 [M08] |
| 盲区监测 | MS 8 分 [A06] | 仅重型车 [E10] | R151（重型） | R151 列入未来实施 [M06] |
| RCTA/RCTB | Advanced SAT/MST [A10] | 无 | — | 无 |
| 限速辅助 | Advanced SAT [A11] | ISA 2024-07-07 [E05] | — | 未见 |
| 驾驶员监测 | DSM [A12]；IVASA [A19] | DDAW 2024-07-07、ADDW 2026-07-07 [E06][E07] | — | 未见 |
| CPD | COP 5 分 [A14] | 无 [E13] | — | 未见 |
| 语音（本地语言） | IVASA 座舱 [A20] | 只涉及 ISA 语音提示的语言 [E05] | — | 未见 |
| 网络安全 / OTA | CPD 允许经销商应客户要求 OTA 停用 [A14] | R155 强制 [E11]；R156 未列入 [E12] | R155、R156 [U04][U05] | 2022 年提议纳入，现状未核实 [M07] |

---

## 5. 竞品配置对比

完整数据见 [feature_matrix.csv](feature_matrix.csv)：7 款车 × 23 项，共 161 格。其中 110 格有官方来源和原文摘录，51 格为「未核实」。

### 5.1 选车和配置

| 车型 | 配置（官网最高配） | 来源 |
|---|---|---|
| Jaecoo J7 | AWD（CKD），官方价目 RM148,800 | [S32] |
| Omoda E5（Omoda 5 已不在官网，用它替代） | OMODA E5 150kW（唯一配置） | [S33] |
| Proton All-New X50 | 1.5TD Flagship | [S34] |
| Perodua Ativa | 1.0L Turbo AV | [S35] |
| Toyota Corolla Cross | HEV GR Sport | [S36] |
| Honda HR-V | 1.5L e:HEV RS | [S37] |
| BYD Atto 3（2026 款） | Performance AWD | [S38] |

### 5.2 对比总表

✓ = 官方列出；? = 未核实（官方没提到）；* = 官网注明要等 Android Auto 在马来西亚正式上线。

| 功能 | J7 | E5 | X50 | Ativa | Corolla Cross | HR-V | Atto 3 |
|---|---|---|---|---|---|---|---|
| AEB 车对车 | ✓ | ✓ | ✓（入门版无） | ✓ 全系 | ✓ | ✓ 全系 | ✓ 全系 |
| AEB 行人 | ? | ✓（官网文字） | ? | ✓（NCAP 2021 记录） | ? | ✓（NCAP 2022 记录） | ? |
| LDW / LKA | ✓ / ✓（LDP+ELK） | ✓ / ✓（LDP+ELK） | ✓ / ✓（LDP） | ✓ / ✓（LDP，全系） | ✓ / ✓ | ✓ / ✓（+RDM） | ✓ / ✓ |
| 车道居中 / TJA | ✓（ICA+TJA） | ✓（ICA+TJA） | ✓（LCC+ICC） | ?（LKC 含义未说明） | ✓（LTA） | ? | ? |
| ACC | ✓（Stop&Go ?） | ✓（Stop&Go ?） | ✓ Stop&Go | ✓（仅 AV） | ✓ All Speeds | ✓ + LSF | ✓ Stop&Go |
| 盲区 BSD | ✓ | ✓ | ✓（全系） | ✓（仅 AV） | ✓ | ?（LaneWatch 摄像头） | ✓ |
| RCTA / RCTB | ✓ / ✓ | ✓ / ✓ | ✓（全系）/ ? | ✓（仅 AV）/ ? | ✓ / ?（有 PKSB） | ? | ✓ / ✓ |
| 开门预警 DOW | ✓ | ✓ | ✓（全系） | ? | ? | ? | ✓ |
| 限速识别 / 辅助 | ✓ 限速提醒 | ✓（官网有，手册无） | ✓ TSI | ? | ? | ? | ✓ TSR+ISLC |
| DMS | ✓ | ✓ | ? | ? | ? | ? | ? |
| CPD | ? | ? | ? | ? | ? | 后排提醒 | ? |
| 360 影像 | ✓ 540° | ✓ 540° | ✓ 360°+透明 | ?（仅倒车影像） | ✓ 3D PVM | ✓（经销商推荐件） | ✓ |
| 中控屏 / 仪表 | 14.8" / 10.25" | 24.6" 双联屏 | 14.6" / 8.88" | 9" / 7" | 10.1" / 12.3" | 8" / 7（未写单位） | 15.6" / 8.8" |
| 语音助手 | ✓ | ✓ | ✓ "Hi PROTON" | ✓（需连 Smart Link） | ? | ? | ✓ |
| 语音语言 | ? | ? | **马来语 + 英语** | ? | ? | ? | ? |
| CarPlay / Android Auto | 无线 / 无线 | 无线 / 无线 | ✓ / ✓* | ? / ? | 无线 / ✓* | ✓ / ✓* | 有线+无线 / ? |
| 车联网 App | ?（有远程空调预启动） | ? | PROTON Link 2.0 | ? | Toyota MY App | Honda CONNECT | BYD App |
| OTA | ?（只有 J7 PHEV 宣称） | ? | 部分（语音系统） | ? | ? | ? | ? |
| ASEAN NCAP | ?（库中未见） | ?（燃油版 Omoda 5：2024 年 5★） | ?（初代 2020 年 5★） | 5★ 2021 | 5★ 2020（2017–2020 规程） | 5★ 2022 | ?（库中未见） |

### 5.3 观察（事实）

1. **ADAS 已经是主流，差异在「是不是全系标配」。**7 款车的最高配都有 AEB、LDW 和车道保持。Ativa、HR-V、Atto 3 是全系标配 AEB；X50 入门版没有。
2. **奇瑞系的独有项是 DMS。**J7 手册还列有 Multi Collision Braking（MCB）[S32]，它也是 ASEAN NCAP 的 Advanced SAT 项目 [S6]。
3. **座舱本地化只有 Proton 写明。**Proton 称 X50 是全球首个马来语语音识别，并会通过 OTA 继续增强语音系统 [S34]。
4. **车联网 App 是常见配置，OTA 很少有人宣称。**Proton、Toyota、Honda、BYD 都有官方 App；J7、E5 的官方页面没写 App 名称。
5. **ASEAN NCAP 评级空白。**J7、E5、Atto 3、新款 X50 都没有官方结果；燃油版 Omoda 5（2024）的配置记录写着 "AEB PEDESTRIAN NOT AVAILABLE" [S39]。
6. **两处官方资料自相矛盾。**
   - E5：官网写有 TSR，2026 年 1 月手册没有。
   - Ativa：手册说语音识别只有 AV 版有，官网规格表的 H 版也写有语音识别。
   - 两处都在 CSV 的备注里写明了。

---

## 6. 综合：功能需求优先级

详见 [sor_priority.md](sor_priority.md)。其中事实（F1–F22）和建议分开写，每条建议都对应法规/评级要求、竞品差距或市场数据。

| 优先级 | 编号和功能 |
|---|---|
| **P0** | SOR-01 AEB 全系标配<br>SOR-02 LDW+LKA 全系标配<br>SOR-03 BSD 全系标配<br>SOR-04 ESC（R140）<br>SOR-05 前后排安全带提醒（带后排座椅占用检测）<br>SOR-06 后排遗留提醒（间接式 CPD）<br>SOR-07 送评配置冻结规则（流程需求） |
| **P1** | SOR-08 AEB 车对摩托车<br>SOR-09 直接感知 CPD + 手机推送<br>SOR-10 摄像头 DMS 保持标配<br>SOR-11 马来语 + 英语语音<br>SOR-12 限速辅助<br>SOR-13 RCTA/RCTB<br>SOR-14 车联网 App<br>SOR-15 OTA（遵循 R156）<br>SOR-16 AEB 行人/骑行者<br>SOR-17 L2 车道居中 + 全速域 ACC<br>SOR-18 360 影像<br>SOR-19 无线 CarPlay/Android Auto<br>SOR-20 AHB |
| **P2** | SOR-21 ARV<br>SOR-22 DOW<br>SOR-23 IVASA 参评准备 |

【推论】**排序逻辑**：
- **P0 主要是保 ASEAN NCAP 5 星的可行性和马来西亚准入。**这几项奇瑞系大多已有硬件，要做的是全系标配和配置管控。
- **P1 主要缩小座舱本地化的差距，并抢 CPD、摩托车 AEB 这类东盟特有的分数。**座舱本地化指语音、App、OTA。

---

## 7. 局限和未核实清单

1. **马来西亚 AEB 强制时间**：所查最新官方材料是 2025-11 的 JPJ 报告，2026 年是否有新规未核实；宪报原文 P.U.(A) 80/2024 未查阅。
2. **马来西亚 R155/R156**：是否已列入 VTA 强制，未核实。
3. **欧盟 R156**：GSR 未列入；是否通过其他法规强制，未核实。
4. **R171 和 R79 04 系列**：技术条款未阅读。
5. **IVASA**：「本地语言」指哪种语言，首批结果是否已经发布，都未核实。
6. **ASEAN NCAP 文件之间不一致**：车道支持分值拆分不同（A05）。
7. **数据口径**
   - TSV 没有车型字段：所选车型是否为各品牌销量第一，Omoda/Jaecoo 记在哪个 maker 标签下，都未核实。
   - 9 个小标签的中国品牌归属不确定，影响不超过 0.09 个百分点。
   - hybrid 没有区分 HEV 和 PHEV。
8. **配置矩阵**：51 格未核实，主要集中在：
   - 语音语言（除 X50 外 6 款）
   - OTA（除 X50 外 6 款）
   - CPD（除 HR-V 外 6 款）
   - DMS（除 J7、E5 外 5 款）
   - AEB 行人（4 款），骑行者（7 款都未核实）
   - ASEAN NCAP 评级（J7、E5、新 X50、Atto 3）
   - 其他：Ativa、HR-V 的多项 ADAS
   - 只核实了最高配，低配差异只记录了官网明确写出的部分。
9. **Atto 3 手册的托管位置**：手册放在 Google Drive，由 BYD 马来西亚官方经销主体 BYD Sime Motors 的车型页链接过去。我把它当作官方规格表，但它不在品牌域名下。
10. **J7 / E5 手册的读取方式**：手册是纯图片，配置是渲染成图片后人工读取的（摘录照抄原文）。

---

## 8. 来源列表（访问日期均为 2026-10-27）

**数据**
- [S1] JPJ 登记汇总 TSV（只读）：`E:\C盘整理_20261012\项目审查\malaysia-auto-ask\warehouse\serving\inputs\expected_aggregates.tsv`（冻结快照，截至 2026-08-31）
- [S2] data.gov.my，Car Registration Transactions（JPJ、交通部，CC BY 4.0），数据目录和字段说明：https://data.gov.my/data-catalogue/registration_transactions_car

**ASEAN NCAP**
- [S3] 2026–2030 协议列表（1–10）：https://www.aseancap.org/our-test-no-1-10-2026-2030-protocols
- [S4] 2026–2030 协议列表（11–20）：https://www.aseancap.org/our-test-no-11-20-2026-2030-protocols
- [S5] Overall Assessment Protocol v3.1：https://www.aseancap.org/uploads/documents/ASEAN-NCAP-Overall-Assessment-Protocol-Version-3.1.pdf
- [S6] Assessment Protocol – Safety Assist v3.2（From January 2026）：https://www.aseancap.org/uploads/documents/ASEAN-NCAP-Assessment-Protocol-Safety-Assist-Version-3.2-13012026.pdf
- [S7] Fitment Rating System v2.0：https://www.aseancap.org/uploads/documents/ASEAN-NCAP-Fitment-Rating-System-Version-2.0.pdf
- [S8] Assessment Protocol – Motorcyclist Safety v2.0：https://www.aseancap.org/uploads/documents/1.-ASEAN-NCAP_Assessment-Protocol-Motorcyclist-Safety-Ver-2.0_20May2024-Clean.pdf
- [S9] Assessment Protocol – Child Occupant Protection v3.3（From May 2026）：https://www.aseancap.org/uploads/files/ASEAN_NCAP_Assessment_Protocol_Child_Occupant_Protection_Version_3.3_20260526080930.pdf
- [S10] Star Rating Validity v1.0：https://www.aseancap.org/uploads/documents/ASEAN-NCAP-Star-Rating-Validity-Version-1.0.pdf
- [S11] 技术公告页（ATB001、ATB003、ATB004）：https://www.aseancap.org/our-test-technical-bulletin
- [S12] 新闻：Proton X90 5 星被撤销（2026-03-15）：http://www.aseancap.org/x/news_post.php?slug=asean-ncap-revokes-proton-x90s-5-star-rating-new-2026-model-downgraded-to-1-star-due-to-removal-of-critical-safety-technologies
- [S13] 新闻：IVASA 启动（2026-06-06）：https://www.aseancap.org/x/news_post.php?slug=asean-ncap-launches-new-initiative-on-intelligent-vehicle-advanced-safety-assessment-ivasa
- [S14] 新闻：与 CAERI 合作推出 IVASA（2026-07-28）：http://www.aseancap.org/x/news_post.php?slug=asean-ncap-partners-with-caeri-to-launch-ivasa-for-intelligent-vehicle-safety-in-southeast-asia-1786723419
- [S15] IVASA Test Protocol for Intelligent Cabin Interaction：http://www.aseancap.org/uploads/files/03-EN-IVASA_Test_Protocol_for_Intelligent_Cabin_20260810105644.pdf
- [S16] 官方结果库：https://www.aseancap.org/x/results.php

**欧盟**（EUR-Lex 页面；本项目经欧盟出版局 Cellar 接口 `http://publications.europa.eu/resource/celex/<CELEX>` 获取同一文本）
- [S17] Regulation (EU) 2019/2144，合并文本 2026-08-02：https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02019R2144-20260802
- [S18] Commission Delegated Regulation (EU) 2021/1958（ISA）：https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32021R1958
- [S19] Commission Delegated Regulation (EU) 2021/1341（DDAW）：https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32021R1341
- [S20] Commission Delegated Regulation (EU) 2023/2590（ADDW）：https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R2590
- [S21] Commission Implementing Regulation (EU) 2021/646（ELKS）：https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32021R0646

**UNECE**（欧盟官方公报转载的 UN/ECE 文本；具有法律效力的是 UN/ECE 原文）
- [S22] UN Regulation No 152（02 series，Suppl. 3），OJ 2024/2497：https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:42024X2497
- [S23] UN Regulation No 79（03 series），OJ 2018/1947：https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:42018X1947
- [S24] UN Regulation No 156，OJ 2021/388：https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:42021X0388

**UN 条约库**（法规生效日期，以及各缔约方从何时开始适用）
- [S25] R152：https://treaties.un.org/doc/Publication/MTDSG/Volume%20I/Chapter%20XI/XI-B-16-152.en.xml
- [S26] R155：https://treaties.un.org/doc/Publication/MTDSG/Volume%20I/Chapter%20XI/XI-B-16-155.en.xml
- [S27] R156：https://treaties.un.org/doc/Publication/MTDSG/Volume%20I/Chapter%20XI/XI-B-16-156.en.xml
- [S28] R79：https://treaties.un.org/doc/Publication/MTDSG/Volume%20I/Chapter%20XI/XI-B-16-79.en.xml
- [S29] R171：https://treaties.un.org/doc/Publication/MTDSG/Volume%20I/Chapter%20XI/XI-B-16-171.en.xml

**马来西亚 JPJ**（JPJ 官员会议报告，托管在 JASIC 网站）
- [S30] JPJ Automotive Engineering Division，"Introduction of Vehicle Type Approval (VTA) System in Malaysia"，JASIC Public-Private Forum，2025-11，第 16–18 页：https://www.jasic.org/meeting_docs_admin/contents/uploads/doc/meeting2/6%20Malaysia%20-%20VTA%20Framework%20-%20PP%20Forum%20JASIC%20Nov%202025.pdf
- [S31] JPJ Automotive Engineering Division，"Country Report (Current Activities under VTA Procedure in Malaysia)"，13th Public and Private Joint Forum in Asia，2022-11：https://www.jasic.org/meeting_docs_admin/contents/uploads/doc/meeting2/4-10%20Malaysia%20-%20Country%20Report%20v2.pdf

**品牌官网**（逐格 URL 见 feature_matrix.csv）
- [S32] Jaecoo J7：手册 https://omodajaecoo.com.my/themes/demo/assets/brochure/J7_brochure_website.pdf ；车型页 https://omodajaecoo.com.my/modelj7
- [S33] Omoda E5（Chery Malaysia）：手册 https://www.chery.my/wp-content/uploads/2026/01/Chery_OMODA_E5_Brochure_Jan_2026.pdf ；车型页 https://www.chery.my/model/omoda-e5/
- [S34] Proton X50：车型页 https://www.proton.com/models/all-new-x50 ；马来语语音新闻稿（2025-07-31）https://www.proton.com/happenings/2025/july/proton-unveils-world-s-first-bahasa-melayu-vr-in-all-new-proton-x50
- [S35] Perodua Ativa：https://www.perodua.com.my/our-models/suv/ativa.html ；手册 https://www.perodua.com.my/files/Ativa_Brochure.pdf
- [S36] Toyota Corolla Cross HEV GR Sport：https://www.toyota.com.my/en/models/corolla-cross-hybrid-electric/corolla-cross-hev-gr-sport.html
- [S37] Honda HR-V：https://www.honda.com.my/model/hrv/spec ；https://www.honda.com.my/model/hrv/safety ；https://www.honda.com.my/technology/honda-connect
- [S38] BYD Atto 3（BYD Sime Motors）：https://byd.simemotors.my/byd-atto-3 ；官网链接的手册 https://drive.google.com/file/d/1Qy3WraoV9PIa4085AiZG-kW7zm6fk0Qh/view
- [S39] ASEAN NCAP 单车结果页：
  - Ativa：https://www.aseancap.org/x/result.php?slug=perodua-ativa-2
  - HR-V：https://www.aseancap.org/x/result.php?slug=honda-hr-v-2022
  - Corolla Cross：https://www.aseancap.org/x/result.php?slug=toyota-corolla-cross
  - Omoda 5：https://www.aseancap.org/x/result.php?slug=chery-omoda-5
  - X50（2020）：https://www.aseancap.org/x/result.php?slug=proton-x50

**其他**
- [S40] Jaecoo J7 PHEV 的 OTA 新闻稿（2025-03-02），完整 URL 见 feature_matrix.csv 中 J7 / OTA升级 一行的备注
- [S41] ASEAN NCAP 新闻列表（Jetour T2 2026-01-09、Jetour T1 2026-01-26 获 5 星的标题）：http://www.aseancap.org/x/news.php
