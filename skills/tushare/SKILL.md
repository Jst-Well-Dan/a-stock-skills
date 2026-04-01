---
name: tushare
description: 使用 Tushare Pro 获取金融数据时使用此 skill。涵盖股票（行情、财务、参考数据）、
  指数、基金、期货、期权、债券、外汇、宏观经济及另类数据（新闻、电影票房等）。
  由于 Tushare 接口众多，本 Skill 采用渐进式披露策略，仅展示接口目录。
---

# Tushare Pro Skill

Tushare Pro 是一个极其丰富的金融数据接口库。与 AKShare 不同，Tushare Pro 的大部分接口需要 **Token 认证** 且遵循 **积分制权限**。

---

## 使用流程

```
Step 1  获取 Token  → 前往 https://tushare.pro 个人中心获取 Token
Step 2  初始化接口  → 使用 ts.set_token() 和 pro = ts.pro_api()
Step 3  识别领域    → 查下方【域速查表】，确定需求所属的主题域
Step 4  定位接口    → view references/catalog.md 找到对应的 pro.<interface_name>
Step 5  查阅参数    → view references/domains/<域名>.md 或获取参数详情
Step 6  执行代码    → bash_tool 调用接口获取数据
```

> **注意**：Tushare 接口名通常以 `pro.` 开头。对于大部分接口，`ts_code` 是核心参数，格式为 `代码.市场` (如 `000001.SZ`, `600000.SH`)。

---

## 预初始化 (Token 设置)

在使用任何接口前，必须先进行初始化：

```python
import tushare as ts

# 设置你的 token（通常从环境变量中读取或用户直接提供）
ts.set_token('YOUR_TOKEN_HERE')

# 初始化 pro 接口实例
pro = ts.pro_api()

# 示例：获取股票列表
df = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
```

---

## 域速查表

| 域 | 核心内容 | 详情索引 |
|---|---|---|
| **stock** | 股票基础数据、日/周/月线行情、复权因子、停复牌、龙虎榜、大宗交易、股东持股 | `domains/stock.md` |
| **finance** | 上市公司三大财务报表（季报/年报）、财务指标、高管薪酬、分红送股、业绩预告 | `domains/finance.md` |
| **index** | 沪深重要指数行情、指数成分及权重、行业分类、大盘每日指标 | `domains/index.md` |
| **fund** | 公募基金基础信息、净值数据、分红、持仓、规模、基金经理详情 | `domains/fund.md` |
| **futures** | 期货合约、行情、持仓、结算、仓单、主力合约映射 | `domains/futures.md` |
| **options** | 期权合约、行情、结算、行权、期权持仓 | `domains/options.md` |
| **bond** | 债券基础数据、行情数据、可转债详情 | `domains/bond.md` |
| **global** | 港股行情、美股行情、外汇基本信息及行情 | `domains/global.md` |
| **macro** | 宏观经济指标、经济日历、各大洲经济指标 | `domains/macro.md` |
| **alternative** | 财经新闻、新闻VIP、重大事件、电影票房数据 | `domains/others.md` |

---

## 常见参数格式

*   **ts_code**: `000001.SZ` (深交所), `600000.SH` (上交所), `00700.HK` (港股), `AAPL.US` (美股)。
*   **start_date / end_date**: `YYYYMMDD` 字符串，如 `'20230101'`。
*   **asset**: 资产类别（E：股票 INDEX：指数 FT：期货 FD：基金）。
*   **adj**: 复权类型（None 未复权, qfq 前复权, hfq 后复权）。*注意：Tushare 的行情接口中，复权因子通常在 `adj_factor` 接口中独立提供，或者部分接口支持直接复权。*

---

## 详细索引列表

| 文件 | 内容说明 |
|---|---|
| `references/catalog.md` | **Tushare 接口全量单行目录**（快速检索接口名） |
| `references/domains/stock.md` | 股票市场相关接口列表 |
| `references/domains/finance.md` | 财务会计相关接口列表 |
| `references/domains/index.md` | 指数与行业相关接口列表 |
| `references/domains/fund.md` | 基金市场相关接口列表 |
| `references/domains/macro.md` | 宏观经济数据接口列表 |
| `references/domains/others.md` | 另类数据（外汇、大宗商品、新闻等）|
