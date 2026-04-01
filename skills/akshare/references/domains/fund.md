# Fund 域接口详情

> 共 73 个接口，覆盖ETF/LOF/开放式/货币基金 净值、持仓、评级、规模、基金经理等。

## 接口列表

### `fund_announcement_dividend_em(symbol: str = '000001') -> pandas.DataFrame`

东方财富网站-天天基金网-基金档案-基金公告-分红配送
https://fundf10.eastmoney.com/jjgg_000001_2.html
:param symbol: 基金代码; 可以通过调用 ak.fund_name_em() 接口获取
:type symbol: str
:return: 分红配送-公告列表
:rtype: pandas.DataFrame

---

### `fund_announcement_personnel_em(symbol: str = '000001') -> pandas.DataFrame`

东方财富网站-天天基金网-基金档案-基金公告-人事调整
https://fundf10.eastmoney.com/jjgg_000001_4.html
:param symbol: 基金代码; 可以通过调用 ak.fund_name_em() 接口获取
:type symbol: str
:return: 人事调整-公告列表
:rtype: pandas.DataFrame

---

### `fund_announcement_report_em(symbol: str = '000001') -> pandas.DataFrame`

东方财富网站-天天基金网-基金档案-基金公告-定期报告
https://fundf10.eastmoney.com/jjgg_000001_3.html
:param symbol: 基金代码; 可以通过调用 ak.fund_name_em() 接口获取
:type symbol: str
:return: 定期报告-公告列表
:rtype: pandas.DataFrame

---

### `fund_aum_em() -> pandas.DataFrame`

东方财富-基金-基金公司排名列表
https://fund.eastmoney.com/Company/lsgm.html
:return: 基金公司排名列表
:rtype: pandas.DataFrame

---

### `fund_aum_hist_em(year: str = '2023') -> pandas.DataFrame`

东方财富-基金-基金公司历年管理规模排行列表
https://fund.eastmoney.com/Company/lsgm.html
:param year: query year
:type year: str
:return: 基金公司历年管理规模排行列表
:rtype: pandas.DataFrame

---

### `fund_aum_trend_em() -> pandas.DataFrame`

东方财富-基金-基金市场管理规模走势图
https://fund.eastmoney.com/Company/default.html
:return: 基金市场管理规模走势图
:rtype: pandas.DataFrame

---

### `fund_balance_position_lg() -> pandas.DataFrame`

乐咕乐股-基金仓位-平衡混合型基金仓位
https://legulegu.com/stockdata/fund-position/pos-pingheng
:return: 平衡混合型基金仓位
:rtype: pandas.DataFrame

---

### `fund_cf_em(year: str = '2025', typ: str = '', rank: str = 'FSRQ', sort: str = 'desc', page: int = -1) -> pandas.DataFrame`

天天基金网-基金数据-分红送配-基金拆分
https://fund.eastmoney.com/data/fundchaifen.html#FSRQ,desc,1,,,
:param year: 查询年份
:type year: str
:param typ: 基金类型；空串表示全部; choice of {"", "指数型-其他", "指数型-海外股票", "指数型-固收", "指数型-股票",
"债券型-中短债", "债券型-长债", "债券型-可转债", "债券型-混合债", "债券型-混合一级", "债券型-混合二级",
"商品（不含QDII）", "货币型", "混合型-平衡", "混合型-偏债", "混合型-偏股", "混合型-灵活", "股票型", "QDII", "FOF"}
:type typ: str
:param rank: 排序字段；choice of {"BZDM", "ABBNAME", "FSRQ", "FHFCZ"}; "BZDM": 基金代码,
"ABBNAME": 基金简称, "FSRQ": 拆分折算日, "FHFCZ": 拆分折算(每份)
:type rank: str
:param sort: 排序方向；choice of {"asc", "desc"}
:type sort: str
:param page: 查询页数；请求第page页数据; -1 表示全部页面
:type page: int
:return: 基金拆分
:rtype: pandas.DataFrame

---

### `fund_etf_category_sina(symbol: str = 'LOF基金') -> pandas.DataFrame`

新浪财经-基金列表
https://vip.stock.finance.sina.com.cn/fund_center/index.html#jjhqetf
:param symbol: choice of {"封闭式基金", "ETF基金", "LOF基金"}
:type symbol: str
:return: 指定 symbol 的基金列表
:rtype: pandas.DataFrame

---

### `fund_etf_category_ths(symbol: str = 'ETF', date: str = '') -> pandas.DataFrame`

同花顺理财-基金数据-每日净值-实时行情
https://fund.10jqka.com.cn/datacenter/jz/
:param symbol: 基金类型; choice of {"股票型", "债券型", "混合型", "ETF", "LOF", "QDII", "保本型", "指数型", ""}; "" 表示全部
:type symbol: str
:param date: 查询日期
:type date: str
:return: 基金实时行情
:rtype: pandas.DataFrame

---

### `fund_etf_dividend_sina(symbol: str = 'sh510050') -> pandas.DataFrame`

新浪财经-基金-ETF 基金-累计分红
https://finance.sina.com.cn/fund/quotes/510050/bc.shtml
:param symbol: 基金名称, 可以通过 ak.fund_etf_category_sina() 函数获取
:type symbol: str
:return: 累计分红
:rtype: pandas.DataFrame

---

### `fund_etf_fund_daily_em() -> pandas.DataFrame`

东方财富网-天天基金网-基金数据-场内交易基金
https://fund.eastmoney.com/cnjy_dwjz.html
:return: 当前交易日的所有场内交易基金数据
:rtype: pandas.DataFrame

---

### `fund_etf_fund_info_em(fund: str = '511280', start_date: str = '20000101', end_date: str = '20500101') -> pandas.DataFrame`

东方财富网站-天天基金网-基金数据-场内交易基金-历史净值明细
https://fundf10.eastmoney.com/jjjz_511280.html
:param fund: 场内交易基金代码, 可以通过 fund_etf_fund_daily_em 来获取
:type fund: str
:param start_date: 开始统计时间
:type start_date: str
:param end_date: 结束统计时间
:type end_date: str
:return: 东方财富网站-天天基金网-基金数据-场内交易基金-历史净值明细
:rtype: pandas.DataFrame

---

### `fund_etf_hist_em(symbol: str = '159707', period: str = 'daily', start_date: str = '19700101', end_date: str = '20500101', adjust: str = '') -> pandas.DataFrame`

东方财富-ETF行情
https://quote.eastmoney.com/sz159707.html
:param symbol: ETF 代码
:type symbol: str
:param period: choice of {'daily', 'weekly', 'monthly'}
:type period: str
:param start_date: 开始日期
:type start_date: str
:param end_date: 结束日期
:type end_date: str
:param adjust: choice of {"qfq": "前复权", "hfq": "后复权", "": "不复权"}
:type adjust: str
:return: 每日行情
:rtype: pandas.DataFrame

---

### `fund_etf_hist_min_em(symbol: str = '159707', start_date: str = '1979-09-01 09:32:00', end_date: str = '2222-01-01 09:32:00', period: str = '5', adjust: str = '') -> pandas.DataFrame`

东方财富-ETF 行情
https://quote.eastmoney.com/sz159707.html
:param symbol: ETF 代码
:type symbol: str
:param start_date: 开始日期
:type start_date: str
:param end_date: 结束日期
:type end_date: str
:param period: choice of {"1", "5", "15", "30", "60"}
:type period: str
:param adjust: choice of {'', 'qfq', 'hfq'}
:type adjust: str
:return: 每日分时行情
:rtype: pandas.DataFrame

---

### `fund_etf_hist_sina(symbol: str = 'sh510050') -> pandas.DataFrame`

新浪财经-基金-ETF 基金-日行情数据
https://finance.sina.com.cn/fund/quotes/159996/bc.shtml
:param symbol: 基金名称, 可以通过 ak.fund_etf_category_sina() 函数获取
:type symbol: str
:return: 日行情数据
:rtype: pandas.DataFrame

---

### `fund_etf_scale_sse(date: str = '20250115') -> pandas.DataFrame`

上海证券交易所-产品-基金产品-ETF产品-ETF产品列表-基金规模
https://www.sse.com.cn/assortment/fund/etf/list/scale/
:param date: 统计日期, 默认为空返回最新数据, 格式如 "20250115"
:type date: str
:return: ETF基金份额数据
:rtype: pandas.DataFrame

---

### `fund_etf_scale_szse() -> pandas.DataFrame`

深圳证券交易所-基金产品-基金列表-ETF基金份额
https://fund.szse.cn/marketdata/fundslist/index.html
:return: ETF基金份额数据
:rtype: pandas.DataFrame

---

### `fund_etf_spot_em() -> pandas.DataFrame`

东方财富-ETF 实时行情
https://quote.eastmoney.com/center/gridlist.html#fund_etf
:return: ETF 实时行情
:rtype: pandas.DataFrame

---

### `fund_etf_spot_ths(date: str = '') -> pandas.DataFrame`

同花顺理财-基金数据-每日净值-ETF-实时行情
https://fund.10jqka.com.cn/datacenter/jz/kfs/etf/
:param date: 查询日期
:type date: str
:return: ETF 实时行情
:rtype: pandas.DataFrame

---

### `fund_exchange_rank_em() -> pandas.DataFrame`

东方财富网-数据中心-场内交易基金排行
https://fund.eastmoney.com/data/fbsfundranking.html
:return: 场内交易基金数据
:rtype: pandas.DataFrame

---

### `fund_fee_em(symbol: str = '015641', indicator: str = '认购费率') -> pandas.DataFrame`

天天基金-基金档案-购买信息
https://fundf10.eastmoney.com/jjfl_015641.html
:param symbol: 基金代码
:type symbol: str
:param indicator: choice of {"交易状态", "申购与赎回金额", "交易确认日", "运作费用", "认购费率（前端）", "认购费率（后端）","申购费率（前端）", "赎回费率"}
:type indicator: str
:return: 交易规则
:rtype: pandas.DataFrame

---

### `fund_fh_em(year: str = '2025', typ: str = '', rank: str = 'BZDM', sort: str = 'asc', page: int = -1) -> pandas.DataFrame`

天天基金网-基金数据-分红送配-基金分红
https://fund.eastmoney.com/data/fundfenhong.html#DJR,desc,1,,,
:param year: 查询年份
:type year: str
:param typ: 基金类型；空串表示全部; choice of {"指数型-其他", "指数型-海外股票", "指数型-固收", "指数型-股票", "债券型-中短债",
"债券型-长债", "债券型-理财", "债券型-混合债", "债券型-混合一级", "债券型-混合二级", "货币型-普通货币", "货币型-浮动净值",
"混合型-平衡", "混合型-偏债", "混合型-偏股", "混合型-灵活", "混合型-绝对收益", "股票型", "REITs", "Reits", "QDII-商品",
"QDII-普通股票", "QDII-混合债", "QDII-混合偏股", "QDII-纯债", "QDII-REITs", "FOF"}
:type typ: str
:param rank: 排序字段；choice of {"BZDM", "ABBNAME", "DJR", "FSRQ", "FHFCZ", "FFR"}; "BZDM": 基金代码,
"ABBNAME": 基金简称, "DJR": 权益登记日, "FSRQ": 除息日期, "FHFCZ": 分红(元/份), "FFR": 分红发放日
:type rank: str
:param sort: 排序方向；排序方式; choice of {"asc", "desc"}
:type sort: str
:param page: 查询页数；请求第page页数据; -1 表示全部页面
:type page: int
:return: 基金分红
:rtype: pandas.DataFrame

---

### `fund_fh_rank_em() -> pandas.DataFrame`

天天基金网-基金数据-分红送配-基金分红排行
https://fund.eastmoney.com/data/fundleijifenhong.html
:return: 基金分红排行
:rtype: pandas.DataFrame

---

### `fund_financial_fund_daily_em() -> pandas.DataFrame`

东方财富网站-天天基金网-基金数据-理财型基金收益
# 该接口暂无数据
https://fund.eastmoney.com/lcjj.html#1_1__0__ljjz,desc_1_os1
:return: 当前交易日的所有理财型基金收益
:rtype: pandas.DataFrame

---

### `fund_financial_fund_info_em(symbol: str = '000134') -> pandas.DataFrame`

东方财富网站-天天基金网-基金数据-理财型基金收益-历史净值明细
https://fundf10.eastmoney.com/jjjz_000791.html
:param symbol: 理财型基金代码, 可以通过 ak.fund_financial_fund_daily_em() 来获取
:type symbol: str
:return: 东方财富网站-天天基金网-基金数据-理财型基金收益-历史净值明细
:rtype: pandas.DataFrame

---

### `fund_graded_fund_daily_em() -> pandas.DataFrame`

东方财富网站-天天基金网-基金数据-分级基金净值
https://fund.eastmoney.com/fjjj.html#1_1__0__zdf,desc_1
:return: 当前交易日的所有分级基金净值
:rtype: pandas.DataFrame

---

### `fund_graded_fund_info_em(symbol: str = '150232') -> pandas.DataFrame`

东方财富网站-天天基金网-基金数据-分级基金净值-历史净值明细
https://fundf10.eastmoney.com/jjjz_150232.html
:param symbol: 分级基金代码, 可以通过 ak.fund_money_fund_daily_em() 来获取
:type symbol: str
:return: 东方财富网站-天天基金网-基金数据-分级基金净值-历史净值明细
:rtype: pandas.DataFrame

---

### `fund_hk_fund_hist_em(code: str = '1002200683', symbol: str = '历史净值明细') -> pandas.DataFrame`

东方财富网-天天基金网-基金数据-香港基金-历史净值明细(分红送配详情)
https://overseas.1234567.com.cn/f10/FundJz/968092#FHPS
:param code: 通过 ak.fund_em_hk_rank() 获取
:type code: str
:param symbol: choice of {"历史净值明细", "分红送配详情"}
:type symbol: str
:return: 香港基金-历史净值明细(分红送配详情)
:rtype: pandas.DataFrame

---

### `fund_hk_rank_em() -> pandas.DataFrame`

东方财富网-数据中心-香港基金排行
https://overseas.1234567.com.cn/FundList
:return: 香港基金排行
:rtype: pandas.DataFrame

---

### `fund_hold_structure_em() -> pandas.DataFrame`

天天基金网-基金数据-规模份额-持有人结构
https://fund.eastmoney.com/data/cyrjglist.html
:return: 持有人结构
:rtype: pandas.DataFrame

---

### `fund_individual_achievement_xq(symbol: str = '000001', timeout: float = None) -> pandas.DataFrame`

雪球基金-基金业绩
https://danjuanfunds.com/djapi/fundx/base/fund/achievement/675091
:param symbol: 基金代码
:type symbol: str
:param timeout: choice of None or a positive float number
:type timeout: float
:return: 基金业绩
:rtype: pandas.DataFrame

---

### `fund_individual_analysis_xq(symbol: str = '000001', timeout: float = None) -> pandas.DataFrame`

雪球基金-基金数据分析
https://danjuanfunds.com/djapi/fund/base/quote/data/index/analysis/675091
:param symbol: 基金代码
:type symbol: str
:param timeout: choice of None or a positive float number
:type timeout: float
:return: 基金数据分析
:rtype: pandas.DataFrame

---

### `fund_individual_basic_info_xq(symbol: str = '000001', timeout: float = None) -> pandas.DataFrame`

雪球基金-基金详情
https://danjuanfunds.com/djapi/fund/675091
:param symbol: 基金代码
:type symbol: str
:param timeout: choice of None or a positive float number
:type timeout: float
:return: 基金信息
:rtype: pandas.DataFrame

---

### `fund_individual_detail_hold_xq(symbol: str = '002804', date: str = '20231231', timeout: float = None) -> pandas.DataFrame`

雪球基金-持仓
https://danjuanfunds.com/rn/fund-detail/archive?id=103&code=002804
:param symbol: 基金代码
:type symbol: str
:param date: 财报日期
:type date: str
:param timeout: choice of None or a positive float number
:type timeout: float
:return: 雪球基金-持仓
:rtype: pandas.DataFrame

---

### `fund_individual_detail_info_xq(symbol: str = '000001', timeout: float = None) -> pandas.DataFrame`

雪球基金-交易规则
https://danjuanfunds.com/djapi/fund/detail/675091
:param symbol: 基金代码
:type symbol: str
:param timeout: choice of None or a positive float number
:type timeout: float
:return: 交易规则
:rtype: pandas.DataFrame

---

### `fund_individual_profit_probability_xq(symbol: str = '000001', timeout: float = None) -> pandas.DataFrame`

雪球基金-盈利概率-历史任意时点买入，持有满 X 年，盈利概率 Y%
https://danjuanfunds.com/djapi/fundx/base/fund/profit/ratio/675091
:param symbol: 基金代码
:type symbol: str
:param timeout: choice of None or a positive float number
:type timeout: float
:return: 盈利概率
:rtype: pandas.DataFrame

---

### `fund_info_index_em(symbol: str = '沪深指数', indicator: str = '被动指数型') -> pandas.DataFrame`

东方财富网站-天天基金网-基金数据-基金信息-指数型
https://fund.eastmoney.com/trade/zs.html
:param symbol: choice of {"全部", "沪深指数", "行业主题", "大盘指数", "中盘指数", "小盘指数", "股票指数", "债券指数"}
:type symbol: str
:param indicator: choice of {"全部", "被动指数型", "增强指数型"}
:type indicator: str
:return: 基金信息-指数型
:rtype: pandas.DataFrame

---

### `fund_lcx_rank_em() -> pandas.DataFrame`

东方财富网-数据中心-理财基金排行
# 该接口暂时没有数据
https://fund.eastmoney.com/data/lcxfundranking.html#t;c0;r;sSYL_Z;ddesc;pn50;f;os1;
:return: 理财基金排行
:rtype: pandas.DataFrame

---

### `fund_linghuo_position_lg() -> pandas.DataFrame`

乐咕乐股-基金仓位-灵活配置型基金仓位
https://legulegu.com/stockdata/fund-position/pos-linghuo
:return: 灵活配置型基金仓位
:rtype: pandas.DataFrame

---

### `fund_lof_hist_em(symbol: str = '166009', period: str = 'daily', start_date: str = '19700101', end_date: str = '20500101', adjust: str = '') -> pandas.DataFrame`

东方财富-LOF 行情
https://quote.eastmoney.com/sz166009.html
:param symbol: LOF 代码
:type symbol: str
:param period: choice of {'daily', 'weekly', 'monthly'}
:type period: str
:param start_date: 开始日期
:type start_date: str
:param end_date: 结束日期
:type end_date: str
:param adjust: choice of {"qfq": "前复权", "hfq": "后复权", "": "不复权"}
:type adjust: str
:return: 每日行情
:rtype: pandas.DataFrame

---

### `fund_lof_hist_min_em(symbol: str = '166009', start_date: str = '1979-09-01 09:32:00', end_date: str = '2222-01-01 09:32:00', period: str = '5', adjust: str = '') -> pandas.DataFrame`

东方财富-LOF 分时行情
https://quote.eastmoney.com/sz166009.html
:param symbol: LOF 代码
:type symbol: str
:param start_date: 开始日期时间
:type start_date: str
:param end_date: 结束日期时间
:type end_date: str
:param period: choice of {"1", "5", "15", "30", "60"}
:type period: str
:param adjust: choice of {'', 'qfq', 'hfq'}
:type adjust: str
:return: 每日分时行情
:rtype: pandas.DataFrame

---

### `fund_lof_spot_em() -> pandas.DataFrame`

东方财富-LOF 实时行情
https://quote.eastmoney.com/center/gridlist.html#fund_lof
:return: LOF 实时行情
:rtype: pandas.DataFrame

---

### `fund_manager_em() -> pandas.DataFrame`

天天基金网-基金数据-基金经理大全
https://fund.eastmoney.com/manager/default.html
:return: 基金经理大全
:rtype: pandas.DataFrame

---

### `fund_money_fund_daily_em() -> pandas.DataFrame`

东方财富网-天天基金网-基金数据-货币型基金收益
https://fund.eastmoney.com/HBJJ_pjsyl.html
:return: 当前交易日的所有货币型基金收益数据
:rtype: pandas.DataFrame

---

### `fund_money_fund_info_em(symbol: str = '000009') -> pandas.DataFrame`

东方财富网-天天基金网-基金数据-货币型基金收益-历史净值数据
https://fundf10.eastmoney.com/jjjz_004186.html
:param symbol: 货币型基金代码, 可以通过 fund_money_fund_daily_em 来获取
:type symbol: str
:return: 东方财富网站-天天基金网-基金数据-货币型基金收益-历史净值数据
:rtype: pandas.DataFrame

---

### `fund_money_rank_em() -> pandas.DataFrame`

东方财富网-数据中心-货币型基金排行
https://fund.eastmoney.com/data/hbxfundranking.html
:return: 货币型基金排行
:rtype: pandas.DataFrame

---

### `fund_name_em() -> pandas.DataFrame`

东方财富网站-天天基金网-基金数据-所有基金的名称和类型
https://fund.eastmoney.com/manager/default.html#dt14;mcreturnjson;ftall;pn20;pi1;scabbname;stasc
:return: 所有基金的名称和类型
:rtype: pandas.DataFrame

---

### `fund_new_found_em() -> pandas.DataFrame`

基金数据-新发基金-新成立基金
https://fund.eastmoney.com/data/xinfound.html
:return: 新成立基金
:rtype: pandas.DataFrame

---

### `fund_new_found_ths(symbol: str = '全部') -> pandas.DataFrame`

同花顺-基金数据-新发基金
https://fund.10jqka.com.cn/datacenter/xfjj/
:param symbol: 选择基金类型; choice of {"全部", "发行中", "将发行"}
:type symbol: str
:return: 新发基金数据
:rtype: pandas.DataFrame

---

### `fund_open_fund_daily_em() -> pandas.DataFrame`

东方财富网-天天基金网-基金数据-开放式基金净值
https://fund.eastmoney.com/fund.html#os_0;isall_0;ft_;pt_1
:return: 当前交易日的所有开放式基金净值数据
:rtype: pandas.DataFrame

---

### `fund_open_fund_info_em(symbol: str = '710001', indicator: str = '单位净值走势', period: str = '成立来') -> pandas.DataFrame`

东方财富网-天天基金网-基金数据-开放式基金净值
https://fund.eastmoney.com/fund.html
:param symbol: 基金代码; 可以通过调用 ak.fund_open_fund_daily_em() 获取所有开放式基金代码
:type symbol: str
:param indicator: 需要获取的指标
:type indicator: str
:param period: "成立来"; choice of {"1月", "3月", "6月", "1年", "3年", "5年", "今年来", "成立来"}
:type period: str
:return: 指定基金指定指标的数据
:rtype: pandas.DataFrame

---

### `fund_open_fund_rank_em(symbol: str = '全部') -> pandas.DataFrame`

东方财富网-数据中心-开放基金排行
https://fund.eastmoney.com/data/fundranking.html
:param symbol: choice of {"全部", "股票型", "混合型", "债券型", "指数型", "QDII", "FOF"}
:type symbol: str
:return: 开放基金排行
:rtype: pandas.DataFrame

---

### `fund_overview_em(symbol: str = '015641') -> pandas.DataFrame`

天天基金-基金档案-基本概况
https://fundf10.eastmoney.com/jbgk_015641.html
:param symbol: 基金代码
:type symbol: str
:return: 基本概况
:rtype: pandas.DataFrame

---

### `fund_portfolio_bond_hold_em(symbol: str = '000001', date: str = '2023') -> pandas.DataFrame`

天天基金网-基金档案-投资组合-债券持仓
https://fundf10.eastmoney.com/ccmx1_000001.html
:param symbol: 基金代码
:type symbol: str
:param date: 查询年份
:type date: str
:return: 债券持仓
:rtype: pandas.DataFrame

---

### `fund_portfolio_change_em(symbol: str = '003567', indicator: str = '累计买入', date: str = '2023') -> pandas.DataFrame`

天天基金网-基金档案-投资组合-重大变动
https://fundf10.eastmoney.com/ccbd_000001.html
:param symbol: 基金代码
:type symbol: str
:param indicator: choice of {"累计买入", "累计卖出"}
:type indicator: str
:param date: 查询年份
:type date: str
:return: 重大变动
:rtype: pandas.DataFrame

---

### `fund_portfolio_hold_em(symbol: str = '000001', date: str = '2024') -> pandas.DataFrame`

天天基金网-基金档案-投资组合-基金持仓
https://fundf10.eastmoney.com/ccmx_000001.html
:param symbol: 基金代码
:type symbol: str
:param date: 查询年份
:type date: str
:return: 基金持仓
:rtype: pandas.DataFrame

---

### `fund_portfolio_industry_allocation_em(symbol: str = '000001', date: str = '2023') -> pandas.DataFrame`

天天基金网-基金档案-投资组合-行业配置
https://fundf10.eastmoney.com/hytz_000001.html
:param symbol: 基金代码
:type symbol: str
:param date: 查询年份
:type date: str
:return: 行业配置
:rtype: pandas.DataFrame

---

### `fund_purchase_em() -> pandas.DataFrame`

东方财富网站-天天基金网-基金数据-基金申购状态
https://fund.eastmoney.com/Fund_sgzt_bzdm.html#fcode,asc_1
:return: 基金申购状态
:rtype: pandas.DataFrame

---

### `fund_rating_all() -> pandas.DataFrame`

天天基金网-基金评级-基金评级总汇
https://fund.eastmoney.com/data/fundrating.html
:return: 基金评级总汇
:rtype: pandas.DataFrame

---

### `fund_rating_ja(date: str = '20230331') -> pandas.DataFrame`

天天基金网-基金评级-济安金信评级
https://fund.eastmoney.com/data/fundrating_4.html
:param date: 日期; https://fund.eastmoney.com/data/fundrating_4.html 获取查询日期
:type date: str
:return: 济安金信评级
:rtype: pandas.DataFrame

---

### `fund_rating_sh(date: str = '20230630') -> pandas.DataFrame`

天天基金网-基金评级-上海证券评级
https://fund.eastmoney.com/data/fundrating_3.html
:param date: 日期; https://fund.eastmoney.com/data/fundrating_3.html 获取查询日期
:type date: str
:return: 上海证券评级
:rtype: pandas.DataFrame

---

### `fund_rating_zs(date: str = '20230331') -> pandas.DataFrame`

天天基金网-基金评级-招商证券评级
https://fund.eastmoney.com/data/fundrating_2.html
:param date: 日期; https://fund.eastmoney.com/data/fundrating_2.html 获取查询日期
:type date: str
:return: 招商证券评级-混合型
:rtype: pandas.DataFrame

---

### `fund_report_asset_allocation_cninfo() -> pandas.DataFrame`

巨潮资讯-数据中心-专题统计-基金报表-基金资产配置
https://webapi.cninfo.com.cn/#/thematicStatistics
:return: 基金资产配置
:rtype: pandas.DataFrame

---

### `fund_report_industry_allocation_cninfo(date: str = '20210630') -> pandas.DataFrame`

巨潮资讯-数据中心-专题统计-基金报表-基金行业配置
https://webapi.cninfo.com.cn/#/thematicStatistics
:param date: 报告时间; choice of {"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"}, 从 2017 年开始
:type date: str
:return: 基金行业配置
:rtype: pandas.DataFrame

---

### `fund_report_stock_cninfo(date: str = '20210630') -> pandas.DataFrame`

巨潮资讯-数据中心-专题统计-基金报表-基金重仓股
https://webapi.cninfo.com.cn/#/thematicStatistics
:param date: 报告时间; choice of {"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"}
:type date: str
:return: 基金重仓股
:rtype: pandas.DataFrame

---

### `fund_scale_change_em() -> pandas.DataFrame`

天天基金网-基金数据-规模份额-规模变动
https://fund.eastmoney.com/data/gmbdlist.html
:return: 规模变动
:rtype: pandas.DataFrame

---

### `fund_scale_close_sina() -> pandas.DataFrame`

新浪财经-基金数据中心-基金规模-封闭式基金
https://vip.stock.finance.sina.com.cn/fund_center/index.html#jjhqetf
:return: 基金规模
:rtype: pandas.DataFrame

---

### `fund_scale_open_sina(symbol: str = '股票型基金') -> pandas.DataFrame`

新浪财经-基金数据中心-基金规模-开放式基金
https://vip.stock.finance.sina.com.cn/fund_center/index.html#jjhqetf
:param symbol: choice of {"股票型基金", "混合型基金", "债券型基金", "货币型基金", "QDII基金"}
:type symbol: str
:return: 基金规模
:rtype: pandas.DataFrame

---

### `fund_scale_structured_sina() -> pandas.DataFrame`

新浪财经-基金数据中心-基金规模-分级子基金
https://vip.stock.finance.sina.com.cn/fund_center/index.html#jjgmfjall
:return: 基金规模
:rtype: pandas.DataFrame

---

### `fund_stock_position_lg() -> pandas.DataFrame`

乐咕乐股-基金仓位-股票型基金仓位
https://legulegu.com/stockdata/fund-position/pos-stock
:return: 股票型基金仓位
:rtype: pandas.DataFrame

---

### `fund_value_estimation_em(symbol: str = '全部') -> pandas.DataFrame`

东方财富网-数据中心-净值估算
https://fund.eastmoney.com/fundguzhi.html
:param symbol: choice of {'全部', '股票型', '混合型', '债券型', '指数型', 'QDII', 'ETF联接', 'LOF', '场内交易基金'}
:type symbol: str
:return: 近期净值估算数据
:rtype: pandas.DataFrame

---

