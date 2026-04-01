---
name: akshare
description: 使用 AKShare 库获取金融数据时使用此 skill。覆盖 A股/港股/美股
  行情与财务、宏观经济指标（CPI/PPI/PMI/利率）、期货期权、债券可转债、基金ETF、
  外汇汇率、大宗商品现货、北向资金、板块资金流、龙虎榜等 1086 个接口。
  当用户需要任何中国或全球金融市场数据、量化研究数据、经济指标时必须触发此 skill。
  即使用户只是问"用什么接口"或"怎么取某类数据"，也要触发。
---

# AKShare Skill

AKShare 是 Python 金融数据库，提供 **1086 个接口**，覆盖股票、宏观、期货、期权、
债券、基金、外汇、现货等全品类数据。

---

## 使用流程

```
Step 1  识别域   → 查下方【域速查表】，确定目标数据在哪个域
Step 2  扫描目录  → view references/catalog.md  找到候选函数名
Step 3  查阅详情  → view references/domains/<域名>.md  确认参数与返回字段
Step 4  查阅模式  → view references/patterns.md  （遇到不确定的参数格式/陷阱时）
Step 5  执行代码  → bash_tool 安装并调用
```

> **注意**：Step 2-3 是核心，不要跳过。先通过 catalog 定位函数，再通过 domain 文件
> 确认具体用法，避免参数猜测错误。

---

## 域速查表

| 域 | 函数数 | 核心内容 | 详情文件 |
|---|---|---|---|
| **stock** | 403 | A/港/美股行情、财务报表、资金流、北向、板块、股东、龙虎榜、涨停池... | `domains/stock.md` |
| **macro** | 226 | 中国CPI/PPI/PMI/GDP/LPR、美联储、欧央行、全球宏观指标... | `domains/macro.md` |
| **index** | 80 | 申万/中证/国证/全球指数、波动率QVIX、财新PMI... | `domains/index.md` |
| **fund** | 73 | ETF/LOF/开放式基金净值、持仓、评级、规模、基金经理... | `domains/fund.md` |
| **futures** | 67 | 国内四大交易所+外盘期货 行情/持仓/仓单/结算/库存... | `domains/futures.md` |
| **option** | 47 | 股票期权/商品期权 合约/行情/波动率/风险指标... | `domains/option.md` |
| **bond** | 42 | 国债/可转债/企业债 行情、收益率曲线、发行、质押回购... | `domains/bond.md` |
| **spot/fx/currency/energy** | 50+ | 黄金现货、外汇报价、人民币汇率、碳排放权... | `domains/others.md` |

---

## 常见需求 → 域映射（快速定位）

| 用户需求 | 优先查的域/接口群 |
|---|---|
| 某股票历史K线 | `stock` → `stock_zh_a_hist` |
| 实时行情快照 | `stock` → `stock_zh_a_spot_em` |
| 财务三大报表 | `stock` → `stock_balance/profit/cash_flow_sheet_*` |
| 估值（PE/PB）| `stock` → `stock_a_ttm_lyr`, `stock_index_pe_lg` |
| 北向资金 | `stock` → `stock_hsgt_*` |
| 板块资金流 | `stock` → `stock_sector_fund_flow_*`, `stock_fund_flow_*` |
| 龙虎榜 | `stock` → `stock_lhb_*` |
| 涨跌停池 | `stock` → `stock_zt_pool_*` |
| 股东持股 | `stock` → `stock_gdfx_*` |
| 机构调研 | `stock` → `stock_jgdy_*` |
| 中国CPI/PPI/PMI | `macro` → `macro_china_cpi/ppi/pmi*` |
| LPR/存准率 | `macro` → `macro_china_lpr`, `macro_china_reserve_requirement_ratio` |
| 美联储利率 | `macro` → `macro_bank_usa_interest_rate` |
| 非农/就业 | `macro` → `macro_usa_non_farm`, `macro_usa_unemployment_rate` |
| CFTC持仓 | `macro` → `macro_usa_cftc_*` |
| 黄金ETF持仓 | `macro` → `macro_cons_gold` |
| 指数成分股 | `index` → `index_stock_cons*` |
| 申万行业指数 | `index` → `index_hist_sw`, `index_realtime_sw` |
| ETF行情 | `fund` → `fund_etf_hist_em`, `fund_etf_spot_em` |
| 基金持仓 | `fund` → `fund_portfolio_hold_em` |
| 期货主力连续 | `futures` → `futures_main_sina`, `futures_hist_em` |
| 期货仓单 | `futures` → `futures_warehouse_receipt_*` |
| 可转债 | `bond` → `bond_zh_cov*`, `bond_cb_*` |
| 国债收益率 | `bond` → `bond_china_yield`, `bond_zh_us_rate` |
| 黄金现货 | `spot` → `spot_hist_sge`, `spot_quotations_sge` |
| 人民币汇率 | `currency` → `currency_boc_safe` / `macro` → `macro_china_rmb` |
| 碳排放交易 | `energy` → `energy_carbon_*` |

---

## 参数速记

```
symbol  → A股6位数字 "000001" | 港股5位 "00700" | 美股ticker "AAPL"
adjust  → "" 不复权 | "qfq" 前复权 | "hfq" 后复权
period  → "daily"/"weekly"/"monthly" | 分钟线: "1"/"5"/"15"/"30"/"60"
日期    → "YYYYMMDD" 字符串，如 "20230101"
数据源  → _em 东方财富(首选) | _ths 同花顺 | _sina 新浪(易封IP) | _cninfo 巨潮
```

> **封IP警告**：新浪系接口（`_sina`）批量调用必须加 `time.sleep(0.3~1)`

---

## Reference 文件索引

| 文件 | 内容 | 何时读 |
|---|---|---|
| `references/catalog.md` | 1086 个函数的单行速查目录 | Step 2：不确定函数名时 |
| `references/domains/stock.md` | stock 域 403 个接口完整文档，按9个主题分区 | Step 3：确认股票类接口用法 |
| `references/domains/macro.md` | macro 域 226 个接口，按国家/地区分区 | Step 3：确认宏观类接口用法 |
| `references/domains/index.md` | index 域 80 个接口 | Step 3：指数类 |
| `references/domains/fund.md` | fund 域 73 个接口 | Step 3：基金类 |
| `references/domains/futures.md` | futures 域 67 个接口 | Step 3：期货类 |
| `references/domains/option.md` | option 域 47 个接口 | Step 3：期权类 |
| `references/domains/bond.md` | bond 域 42 个接口 | Step 3：债券类 |
| `references/domains/others.md` | spot/fx/currency/energy 等域 | Step 3：现货/外汇/能源类 |
| `references/patterns.md` | 调用惯例、常见坑、典型场景代码 | Step 4：遇到参数疑问或报错时 |
