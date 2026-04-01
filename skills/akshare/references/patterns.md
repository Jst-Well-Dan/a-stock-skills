# AKShare 使用模式与注意事项

## 安装与导入

```python
pip install akshare --upgrade
import akshare as ak
```

---

## 参数命名惯例

### symbol 格式
- **A股**：6位数字字符串，如 `"000001"`（平安银行）、`"600519"`（贵州茅台）
- **港股**：5位数字，如 `"00700"`（腾讯）
- **美股**：ticker，如 `"AAPL"`、`"TSLA"`
- **期货**：品种代码，如 `"rb2501"`（螺纹钢2501合约），主力连续用 `"RB0"` 或参考 `ak.futures_display_main_sina()`
- **指数**：如 `"000300"`（沪深300）、`"000001"`（上证指数，注意与平安银行同代码但不同接口）

### 日期格式
- 统一为 **`"YYYYMMDD"` 字符串**，如 `"20230101"`
- 少数接口用 `"YYYY-MM-DD"`，以接口文档为准
- 不传时通常默认返回全历史数据（`start_date="19700101"`, `end_date="20500101"`）

### adjust 复权参数（行情接口通用）
| 值 | 含义 |
|---|---|
| `""` | 不复权（默认） |
| `"qfq"` | 前复权（价格向后对齐，适合回测） |
| `"hfq"` | 后复权（价格向前调整，适合长期趋势） |

### period 频率参数
- `"daily"` / `"weekly"` / `"monthly"` — 日/周/月K线
- 分钟线通常用 `"1"` / `"5"` / `"15"` / `"30"` / `"60"`

---

## 数据源后缀含义

| 后缀 | 数据源 | 特点 |
|---|---|---|
| `_em` | 东方财富 | 最稳定，覆盖广，推荐首选 |
| `_ths` | 同花顺 | 财务指标细节好 |
| `_sina` | 新浪财经 | **高频调用易封IP**，加 `time.sleep()` |
| `_cninfo` | 巨潮资讯 | 官方披露数据权威 |
| `_xq` | 雪球 | 需要 token，有反爬 |
| `_lg` | 乐咕乐股 | 估值/情绪类指标 |
| `_tx` | 腾讯证券 | 行情数据备选 |
| `_baidu` | 百度股市通 | 估值数据 |

---

## 常见陷阱

### 1. 新浪接口 IP 封禁
```python
# 错误：循环调用新浪接口不加延迟
for code in stock_list:
    df = ak.stock_zh_a_daily(symbol=code)  # ❌ 快速封IP

# 正确：加延迟
import time
for code in stock_list:
    df = ak.stock_zh_a_daily(symbol=code)
    time.sleep(0.5)  # ✅
```

### 2. `stock_zh_a_hist` 后复权负价格 bug
部分股票（如 600734）在某些时间段后复权数据会出现负价格，属于已知问题。
```python
df = ak.stock_zh_a_hist(symbol="600734", adjust="hfq")
df = df[df['收盘'] > 0]  # 过滤异常值
```

### 3. 股票代码 vs 指数代码冲突
`"000001"` 在不同接口中含义不同：
- `ak.stock_zh_a_hist(symbol="000001")` → 平安银行
- `ak.stock_zh_index_daily(symbol="sh000001")` → 上证指数（需加市场前缀）

### 4. 接口返回空 DataFrame
常见原因：日期范围无数据、symbol 格式错误、数据源暂时不可用。
```python
df = ak.stock_zh_a_hist(symbol="000001", start_date="20230101", end_date="20231231")
if df.empty:
    print("无数据，检查 symbol 格式或日期范围")
```

### 5. 雪球接口需要 token
```python
# 雪球接口（stock_individual_basic_info_xq 等）需要登录后的 cookie token
# 可从浏览器 F12 → Network → 请求头中提取 token 字段
```

---

## 典型使用场景速查

### 场景：获取单只A股日K线（含复权）
```python
df = ak.stock_zh_a_hist(symbol="600519", period="daily",
                         start_date="20200101", end_date="20241231", adjust="qfq")
```

### 场景：获取沪深300成分股列表
```python
df = ak.index_stock_cons(symbol="000300")
```

### 场景：北向资金今日净流入
```python
df = ak.stock_hsgt_fund_flow_summary_em()
```

### 场景：获取某概念板块所有成分股
```python
# 先获取概念板块列表
concepts = ak.stock_board_concept_name_em()
# 再获取成分股
cons = ak.stock_board_concept_cons_em(symbol="ChatGPT")
```

### 场景：A股全量实时行情
```python
df = ak.stock_zh_a_spot_em()  # 东方财富源，稳定
# 或
df = ak.stock_zh_a_spot()     # 新浪源，注意封IP
```

### 场景：获取财务三大报表
```python
# 利润表（按报告期）
df = ak.stock_profit_sheet_by_report_em(symbol="000001")
# 资产负债表（按年度）
df = ak.stock_balance_sheet_by_yearly_em(symbol="000001")
# 现金流量表（按季度）
df = ak.stock_cash_flow_sheet_by_quarterly_em(symbol="000001")
```

### 场景：中国宏观 CPI/PPI 数据
```python
cpi = ak.macro_china_cpi()       # 东方财富源，月度
ppi = ak.macro_china_ppi()       # 东方财富源，月度
cpi_yr = ak.macro_china_cpi_yearly()  # 年度数据，更长历史
```

### 场景：期货主力合约日线
```python
df = ak.futures_main_sina(symbol="RB0", start_date="20230101", end_date="20241231")
# 或使用东方财富（更稳定）
df = ak.futures_hist_em(symbol="螺纹钢主连", period="daily",
                         start_date="20230101", end_date="20241231")
```

### 场景：可转债实时行情
```python
df = ak.bond_zh_cov()             # 东方财富可转债列表+行情
df_spot = ak.bond_zh_hs_cov_spot()  # 新浪实时行情（注意封IP）
```

---

## 版本与更新

- AKShare 更新频繁，接口可能随时变动
- 遇到报错优先检查：`pip install akshare --upgrade`
- 官方文档：https://akshare.akfamily.xyz/
- 接口变更日志：https://akshare.akfamily.xyz/changelog.html
