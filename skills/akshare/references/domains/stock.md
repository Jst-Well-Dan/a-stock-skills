# Stock 域接口详情

> 共 403 个接口，按主题分为 9 个分区。

## 目录
- [A股行情](#A股行情)
- [港股行情](#港股行情)
- [美股行情](#美股行情)
- [财务数据](#财务数据)
- [估值与市场宽度](#估值市场宽度)
- [资金流向与北向](#资金流向北向)
- [股东与机构](#股东机构)
- [板块与行业](#板块行业)
- [龙虎榜与特色](#龙虎榜特色)

---

## A股行情

### `stock_zh_a_hist(symbol: str = '000001', period: str = 'daily', start_date: str = '19700101', end_date: str = '20500101', adjust: str = '', timeout: float = None) -> pandas.DataFrame`

东方财富网-行情首页-沪深京 A 股-每日行情
https://quote.eastmoney.com/concept/sh603777.html?from=classic
:param symbol: 股票代码
:type symbol: str
:param period: choice of {'daily', 'weekly', 'monthly'}
:type period: str
:param start_date: 开始日期
:type start_date: str
:param end_date: 结束日期
:type end_date: str
:param adjust: choice of {"qfq": "前复权", "hfq": "后复权", "": "不复权"}
:type adjust: str
:param timeout: choice of None or a positive float number
:type timeout: float
:return: 每日行情
:rtype: pandas.DataFrame

---

### `stock_zh_a_hist_min_em(symbol: str = '000001', start_date: str = '1979-09-01 09:32:00', end_date: str = '2222-01-01 09:32:00', period: str = '5', adjust: str = '') -> pandas.DataFrame`

东方财富网-行情首页-沪深京 A 股-每日分时行情
https://quote.eastmoney.com/concept/sh603777.html?from=classic
:param symbol: 股票代码
:type symbol: str
:param start_date: 开始日期
:type start_date: str
:param end_date: 结束日期
:type end_date: str
:param period: choice of {'1', '5', '15', '30', '60'}
:type period: str
:param adjust: choice of {'', 'qfq', 'hfq'}
:type adjust: str
:return: 每日分时行情
:rtype: pandas.DataFrame

---

### `stock_zh_a_hist_pre_min_em(symbol: str = '000001', start_time: str = '09:00:00', end_time: str = '15:50:00') -> pandas.DataFrame`

东方财富网-行情首页-沪深京 A 股-每日分时行情包含盘前数据
https://quote.eastmoney.com/concept/sh603777.html?from=classic
:param symbol: 股票代码
:type symbol: str
:param start_time: 开始时间
:type start_time: str
:param end_time: 结束时间
:type end_time: str
:return: 每日分时行情包含盘前数据
:rtype: pandas.DataFrame

---

### `stock_zh_a_hist_tx(symbol: str = 'sz000001', start_date: str = '19000101', end_date: str = '20500101', adjust: str = '', timeout: float = None) -> pandas.DataFrame`

腾讯证券-日频-股票历史数据
https://gu.qq.com/sh000919/zs
:param symbol: 带市场标识的股票或者指数代码
:type symbol: str
:param start_date: 开始日期
:type start_date: str
:param end_date: 结束日期
:type end_date: str
:param adjust: choice of {"qfq": "前复权", "hfq": "后复权", "": "不复权"}
:type adjust: str
:param timeout: choice of None or a positive float number
:type timeout: float
:return: 前复权的股票和指数数据
:rtype: pandas.DataFrame

---

### `stock_zh_a_minute(symbol: str = 'sh600519', period: str = '1', adjust: str = '') -> pandas.DataFrame`

股票及股票指数历史行情数据-分钟数据
https://finance.sina.com.cn/realstock/company/sh600519/nc.shtml
:param symbol: sh000300
:type symbol: str
:param period: 1, 5, 15, 30, 60 分钟的数据
:type period: str
:param adjust: 默认为空: 返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据;
:type adjust: str
:return: specific data
:rtype: pandas.DataFrame

---

### `stock_zh_a_spot() -> pandas.DataFrame`

新浪财经-所有 A 股的实时行情数据; 重复运行本函数会被新浪暂时封 IP
https://vip.stock.finance.sina.com.cn/mkt/#hs_a
:return: 所有股票的实时行情数据
:rtype: pandas.DataFrame

---

### `stock_zh_a_spot_em() -> pandas.DataFrame`

东方财富网-沪深京 A 股-实时行情
https://quote.eastmoney.com/center/gridlist.html#hs_a_board
:return: 实时行情
:rtype: pandas.DataFrame

---

### `stock_zh_a_daily(symbol: str = 'sh603843', start_date: str = '19900101', end_date: str = '21000118', adjust: str = '') -> pandas.DataFrame`

新浪财经-A 股-个股的历史行情数据, 大量抓取容易封 IP
https://finance.sina.com.cn/realstock/company/sh603843/nc.shtml
:param symbol: sh600000
:type symbol: str
:param start_date: 20201103; 开始日期
:type start_date: str
:param end_date: 20201103; 结束日期
:type end_date: str
:param adjust: 默认为空: 返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据; hfq-factor: 返回后复权因子; qfq-factor: 返回前复权因子
:type adjust: str
:return: 行情数据
:rtype: pandas.DataFrame

---

### `stock_intraday_em(symbol: str = '000001') -> pandas.DataFrame`

东方财富-分时数据
https://quote.eastmoney.com/f1.html?newcode=0.000001
:param symbol: 股票代码
:type symbol: str
:return: 分时数据
:rtype: pandas.DataFrame

---

### `stock_intraday_sina(symbol: str = 'sz000001', date: str = '20240321') -> pandas.DataFrame`

新浪财经-日内分时数据
https://vip.stock.finance.sina.com.cn/quotes_service/view/cn_bill.php?symbol=sz000001
:param symbol: 股票代码
:type symbol: str
:param date: 交易日
:type date: str
:return: 分时数据
:rtype: pandas.DataFrame

---

### `stock_bid_ask_em(symbol: str = '000001') -> pandas.DataFrame`

东方财富-行情报价
https://quote.eastmoney.com/sz000001.html
:param symbol: 股票代码
:type symbol: str
:return: 行情报价
:rtype: pandas.DataFrame

---

### `stock_zh_a_cdr_daily(symbol: str = 'sh689009', start_date: str = '19900101', end_date: str = '22201116') -> pandas.DataFrame`

新浪财经-A股-CDR个股的历史行情数据, 大量抓取容易封 IP
https://finance.sina.com.cn/realstock/company/sh689009/nc.shtml
:param start_date: 20201103; 开始日期
:type start_date: str
:param end_date: 20201103; 结束日期
:type end_date: str
:param symbol: sh689009
:type symbol: str
:return: specific data
:rtype: pandas.DataFrame

---

### `stock_zh_kcb_daily(symbol: str = 'sh688399', adjust: str = '') -> pandas.DataFrame`

新浪财经-科创板股票的历史行情数据, 大量抓取容易封IP
https://finance.sina.com.cn/realstock/company/sh688005/nc.shtml
:param symbol: 股票代码; 带市场标识的股票代码
:type symbol: str
:param adjust: 默认不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据; hfq-factor: 返回后复权因子; qfq-factor: 返回前复权因子
:type adjust: str
:return: 科创板股票的历史行情数据
:rtype: pandas.DataFrame

---

### `stock_zh_kcb_spot() -> pandas.DataFrame`

新浪财经-科创板实时行情数据, 大量抓取容易封IP
https://vip.stock.finance.sina.com.cn/mkt/#kcb
:return: 科创板实时行情数据
:rtype: pandas.DataFrame

---

### `stock_zh_b_daily(symbol: str = 'sh900901', start_date: str = '19900101', end_date: str = '21000118', adjust: str = '') -> pandas.DataFrame`

新浪财经-B 股-个股的历史行情数据, 大量抓取容易封 IP
https://finance.sina.com.cn/realstock/company/sh900901/nc.shtml
:param start_date: 20201103; 开始日期
:type start_date: str
:param end_date: 20201103; 结束日期
:type end_date: str
:param symbol: sh600000
:type symbol: str
:param adjust: 默认为空: 返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据; hfq-factor: 返回后复权因子; qfq-factor: 返回前复权因子
:type adjust: str
:return: specific data
:rtype: pandas.DataFrame

---

### `stock_zh_b_spot() -> pandas.DataFrame`

新浪财经-所有 B 股的实时行情数据; 重复运行本函数会被新浪暂时封 IP
https://vip.stock.finance.sina.com.cn/mkt/#hs_b
:return: 所有股票的实时行情数据
:rtype: pandas.DataFrame

---

### `stock_zh_b_spot_em() -> pandas.DataFrame`

东方财富网- B 股-实时行情
https://quote.eastmoney.com/center/gridlist.html#hs_a_board
:return: 实时行情
:rtype: pandas.DataFrame

---

### `stock_zh_b_minute(symbol: str = 'sh900901', period: str = '1', adjust: str = '') -> pandas.DataFrame`

股票及股票指数历史行情数据-分钟数据
https://finance.sina.com.cn/realstock/company/sh900901/nc.shtml
:param symbol: sh900901
:type symbol: str
:param period: 1, 5, 15, 30, 60 分钟的数据
:type period: str
:param adjust: 默认为空: 返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据;
:type adjust: str
:return: specific data
:rtype: pandas.DataFrame

---

### `stock_zh_ah_daily(symbol: str = '02318', start_year: str = '2000', end_year: str = '2019', adjust: str = '') -> pandas.DataFrame`

腾讯财经-港股-AH-股票历史行情
https://gu.qq.com/hk01033/gp
:param symbol: 股票代码
:type symbol: str
:param start_year: 开始年份; e.g., “2000”
:type start_year: str
:param end_year: 结束年份; e.g., “2019”
:type end_year: str
:param adjust: 'qfq': 前复权, 'hfq': 后复权
:type adjust: str
:return: 指定股票在指定年份的日频率历史行情数据
:rtype: pandas.DataFrame

---

### `stock_zh_ah_spot() -> pandas.DataFrame`

腾讯财经-港股-AH-实时行情
https://stockapp.finance.qq.com/mstats/#mod=list&id=hk_ah&module=HK&type=AH&sort=3&page=3&max=20
:return: 腾讯财经-港股-AH-实时行情
:rtype: pandas.DataFrame

---

### `stock_zh_ah_spot_em() -> pandas.DataFrame`

东方财富网-行情中心-沪深港通-AH股比价-实时行情
https://quote.eastmoney.com/center/gridlist.html#ah_comparison
:return: 东方财富网-行情中心-沪深港通-AH股比价-实时行情
:rtype: pandas.DataFrame

---

### `stock_zh_ah_name() -> pandas.DataFrame`

腾讯财经-港股-AH-股票名称
https://stockapp.finance.qq.com/mstats/#mod=list&id=hk_ah&module=HK&type=AH
:return: 股票代码和股票名称的字典
:rtype: pandas.DataFrame

---

### `stock_bj_a_spot_em() -> pandas.DataFrame`

东方财富网-京 A 股-实时行情
https://quote.eastmoney.com/center/gridlist.html#hs_a_board
:return: 实时行情
:rtype: pandas.DataFrame

---

### `stock_sh_a_spot_em() -> pandas.DataFrame`

东方财富网-沪 A 股-实时行情
https://quote.eastmoney.com/center/gridlist.html#hs_a_board
:return: 实时行情
:rtype: pandas.DataFrame

---

### `stock_sz_a_spot_em() -> pandas.DataFrame`

东方财富网-深 A 股-实时行情
https://quote.eastmoney.com/center/gridlist.html#hs_a_board
:return: 实时行情
:rtype: pandas.DataFrame

---

### `stock_kc_a_spot_em() -> pandas.DataFrame`

东方财富网-科创板-实时行情
https://quote.eastmoney.com/center/gridlist.html#kcb_board
:return: 实时行情
:rtype: pandas.DataFrame

---

### `stock_cy_a_spot_em() -> pandas.DataFrame`

东方财富网-创业板-实时行情
https://quote.eastmoney.com/center/gridlist.html#gem_board
:return: 实时行情
:rtype: pandas.DataFrame

---

### `stock_new_a_spot_em() -> pandas.DataFrame`

东方财富网-新股-实时行情
https://quote.eastmoney.com/center/gridlist.html#newshares
:return: 实时行情
:rtype: pandas.DataFrame

---

### `stock_zh_a_new() -> pandas.DataFrame`

新浪财经-行情中心-沪深股市-次新股
https://vip.stock.finance.sina.com.cn/mkt/#new_stock
:return: 次新股行情数据
:rtype: pandas.DataFrame

---

### `stock_zh_a_new_em() -> pandas.DataFrame`

东方财富网-行情中心-沪深个股-新股
https://quote.eastmoney.com/center/gridlist.html#newshares
:return: 新股
:rtype: pandas.DataFrame

---

### `stock_zh_a_st_em() -> pandas.DataFrame`

东方财富网-行情中心-沪深个股-风险警示板
https://quote.eastmoney.com/center/gridlist.html#st_board
:return: 风险警示板
:rtype: pandas.DataFrame

---

### `stock_zh_a_stop_em() -> pandas.DataFrame`

东方财富网-行情中心-沪深个股-两网及退市
https://quote.eastmoney.com/center/gridlist.html#staq_net_board
:return: 两网及退市
:rtype: pandas.DataFrame

---

### `stock_zh_ab_comparison_em() -> pandas.DataFrame`

东方财富网-行情中心-沪深京个股-AB股比价-全部AB股比价
https://quote.eastmoney.com/center/gridlist.html#ab_comparison
:return: 实时行情
:rtype: pandas.DataFrame

---

### `stock_staq_net_stop() -> pandas.DataFrame`

东方财富网-行情中心-沪深个股-两网及退市
https://quote.eastmoney.com/center/gridlist.html#staq_net_board
:return: 两网及退市
:rtype: pandas.DataFrame

---

## 港股行情

### `stock_hk_hist(symbol: str = '00593', period: str = 'daily', start_date: str = '19700101', end_date: str = '22220101', adjust: str = '') -> pandas.DataFrame`

东方财富网-行情-港股-每日行情
https://quote.eastmoney.com/hk/08367.html
:param symbol: 港股-每日行情
:type symbol: str
:param period: choice of {'daily', 'weekly', 'monthly'}
:type period: str
:param start_date: 开始日期
:type start_date: str
:param end_date: 结束日期
:type end_date: str
:param adjust: choice of {"qfq": "1", "hfq": "2", "": "不复权"}
:type adjust: str
:return: 每日行情
:rtype: pandas.DataFrame

---

### `stock_hk_hist_min_em(symbol: str = '01611', period: str = '1', adjust: str = '', start_date: str = '1979-09-01 09:32:00', end_date: str = '2222-01-01 09:32:00') -> pandas.DataFrame`

东方财富网-行情-港股-每日分时行情
https://quote.eastmoney.com/hk/00948.html
:param symbol: 股票代码
:type symbol: str
:param period: choice of {'1', '5', '15', '30', '60'}
:type period: str
:param adjust: choice of {'', 'qfq', 'hfq'}
:type adjust: str
:param start_date: 开始日期
:type start_date: str
:param end_date: 结束日期
:type end_date: str
:return: 每日分时行情
:rtype: pandas.DataFrame

---

### `stock_hk_spot() -> pandas.DataFrame`

新浪财经-港股的所有港股的实时行情数据
https://vip.stock.finance.sina.com.cn/mkt/#qbgg_hk
:return: 实时行情数据
:rtype: pandas.DataFrame

---

### `stock_hk_spot_em() -> pandas.DataFrame`

东方财富网-港股-实时行情
https://quote.eastmoney.com/center/gridlist.html#hk_stocks
:return: 港股-实时行情
:rtype: pandas.DataFrame

---

### `stock_hk_daily(symbol: str = '00981', adjust: str = '') -> pandas.DataFrame`

新浪财经-港股-个股的历史行情数据
https://stock.finance.sina.com.cn/hkstock/quotes/02912.html
:param symbol: 可以使用 ak.stock_hk_spot() 获取
:type symbol: str
:param adjust: "": 返回未复权的数据 ; qfq: 返回前复权后的数据; qfq-factor: 返回前复权因子和调整;
:type adjust: str
:return: 指定 adjust 的数据
:rtype: pandas.DataFrame

---

### `stock_hk_main_board_spot_em() -> pandas.DataFrame`

东方财富网-港股-主板-实时行情
https://quote.eastmoney.com/center/gridlist.html#hk_mainboard
:return: 港股-主板-实时行情
:rtype: pandas.DataFrame

---

### `stock_hk_famous_spot_em() -> pandas.DataFrame`

东方财富网-行情中心-港股市场-知名港股
https://quote.eastmoney.com/center/gridlist.html#hk_wellknown
:return: 知名美股实时行情
:rtype: pandas.DataFrame

---

### `stock_hk_ggt_components_em() -> pandas.DataFrame`

东方财富网-行情中心-港股市场-港股通成份股
https://quote.eastmoney.com/center/gridlist.html#hk_components
:return: 港股通成份股
:rtype: pandas.DataFrame

---

### `stock_hk_index_daily_em(symbol: str = 'HSTECF2L') -> pandas.DataFrame`

东方财富网-港股-股票指数数据
https://quote.eastmoney.com/gb/zsHSTECF2L.html
:param symbol: 港股指数代码; 可以通过 ak.stock_hk_index_spot_em() 获取
:type symbol: str
:return: 指数数据
:rtype: pandas.DataFrame

---

### `stock_hk_index_daily_sina(symbol: str = 'CES100') -> pandas.DataFrame`

新浪财经-港股指数-历史行情数据
https://stock.finance.sina.com.cn/hkstock/quotes/CES100.html
:param symbol: CES100, 港股指数代码
:type symbol: str
:return: 历史行情数据
:rtype: pandas.DataFrame

---

### `stock_hk_index_spot_em() -> pandas.DataFrame`

东方财富网-行情中心-港股-指数实时行情
https://quote.eastmoney.com/center/gridlist.html#hk_index
:return: 指数行情
:rtype: pandas.DataFrame

---

### `stock_hk_index_spot_sina() -> pandas.DataFrame`

新浪财经-行情中心-港股指数
大量采集会被目标网站服务器封禁 IP, 如果被封禁 IP, 请 10 分钟后再试
https://vip.stock.finance.sina.com.cn/mkt/#zs_hk
:return: 所有指数的实时行情数据
:rtype: pandas.DataFrame

---

### `stock_hsgt_sh_hk_spot_em() -> pandas.DataFrame`

东方财富网-行情中心-沪深港通-港股通(沪>港)-股票
https://quote.eastmoney.com/center/gridlist.html#hk_sh_stocks
:return: 东方财富网-行情中心-沪深港通-港股通(沪>港)-股票
:rtype: pandas.DataFrame

---

## 美股行情

### `stock_us_hist(symbol: str = '105.MSFT', period: str = 'daily', start_date: str = '19700101', end_date: str = '22220101', adjust: str = '') -> pandas.DataFrame`

东方财富网-行情-美股-每日行情
https://quote.eastmoney.com/us/ENTX.html#fullScreenChart
:param symbol: 股票代码; 此股票代码需要通过调用 ak.stock_us_spot_em() 的 `代码` 字段获取
:type symbol: str
:param period: choice of {'daily', 'weekly', 'monthly'}
:type period: str
:param start_date: 开始日期
:type start_date: str
:param end_date: 结束日期
:type end_date: str
:param adjust: choice of {"qfq": "1", "hfq": "2", "": "不复权"}
:type adjust: str
:return: 每日行情
:rtype: pandas.DataFrame

---

### `stock_us_hist_min_em(symbol: str = '105.ATER', start_date: str = '1979-09-01 09:32:00', end_date: str = '2222-01-01 09:32:00') -> pandas.DataFrame`

东方财富网-行情首页-美股-每日分时行情
https://quote.eastmoney.com/us/ATER.html
:param symbol: 股票代码
:type symbol: str
:param start_date: 开始日期
:type start_date: str
:param end_date: 结束日期
:type end_date: str
:return: 每日分时行情
:rtype: pandas.DataFrame

---

### `stock_us_spot() -> pandas.DataFrame`

新浪财经-所有美股的数据, 注意延迟 15 分钟
https://finance.sina.com.cn/stock/usstock/sector.shtml
:return: 美股所有股票实时行情
:rtype: pandas.DataFrame

---

### `stock_us_spot_em() -> pandas.DataFrame`

东方财富网-美股-实时行情
https://quote.eastmoney.com/center/gridlist.html#us_stocks
:return: 美股-实时行情; 延迟 15 min
:rtype: pandas.DataFrame

---

### `stock_us_daily(symbol: str = 'FB', adjust: str = '') -> pandas.DataFrame`

新浪财经-美股
https://finance.sina.com.cn/stock/usstock/sector.shtml
备注：
1. CIEN 新浪复权因子错误
2. AI 新浪复权因子错误, 该股票刚上市未发生复权, 但是返回复权因子
:param symbol: 可以使用 get_us_stock_name 获取
:type symbol: str
:param adjust: "": 返回未复权的数据 ; qfq: 返回前复权后的数据; qfq-factor: 返回前复权因子和调整;
:type adjust: str
:return: 指定 adjust 的数据
:rtype: pandas.DataFrame

---

### `stock_us_famous_spot_em(symbol: str = '科技类') -> pandas.DataFrame`

东方财富网-行情中心-美股市场-知名美股
https://quote.eastmoney.com/center/gridlist.html#us_wellknown
:param symbol: choice of {'科技类', '金融类', '医药食品类', '媒体类', '汽车能源类', '制造零售类'}
:type: str
:return: 知名美股实时行情
:rtype: pandas.DataFrame

---

### `stock_us_pink_spot_em() -> pandas.DataFrame`

东方财富网-行情中心-美股市场-粉单市场
https://quote.eastmoney.com/center/gridlist.html#us_pinksheet
:return: 粉单市场实时行情
:rtype: pandas.DataFrame

---

## 财务数据

### `stock_balance_sheet_by_report_em(symbol: str = 'SH600519') -> pandas.DataFrame`

东方财富-股票-财务分析-资产负债表-按报告期
https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0
:param symbol: 股票代码; 带市场标识
:type symbol: str
:return: 资产负债表-按报告期
:rtype: pandas.DataFrame

---

### `stock_balance_sheet_by_yearly_em(symbol: str = 'SH600036') -> pandas.DataFrame`

东方财富-股票-财务分析-资产负债表-按年度
https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0
:param symbol: 股票代码; 带市场标识
:type symbol: str
:return: 资产负债表-按年度
:rtype: pandas.DataFrame

---

### `stock_balance_sheet_by_report_delisted_em(symbol: str = 'SZ000013') -> pandas.DataFrame`

东方财富-股票-财务分析-资产负债表-已退市股票-按报告期
https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=SZ000013#/cwfx/zcfzb
:param symbol: 已退市股票代码; 带市场标识
:type symbol: str
:return: 资产负债表-按报告期
:rtype: pandas.DataFrame

---

### `stock_profit_sheet_by_report_em(symbol: str = 'SH600519') -> pandas.DataFrame`

东方财富-股票-财务分析-利润表-报告期
https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0
:param symbol: 股票代码; 带市场标识
:type symbol: str
:return: 利润表-报告期
:rtype: pandas.DataFrame

---

### `stock_profit_sheet_by_yearly_em(symbol: str = 'SH600519') -> pandas.DataFrame`

东方财富-股票-财务分析-利润表-按年度
https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0
:param symbol: 股票代码; 带市场标识
:type symbol: str
:return: 利润表-按年度
:rtype: pandas.DataFrame

---

### `stock_profit_sheet_by_quarterly_em(symbol: str = 'SH600519') -> pandas.DataFrame`

东方财富-股票-财务分析-利润表-按单季度
https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0
:param symbol: 股票代码; 带市场标识
:type symbol: str
:return: 利润表-按单季度
:rtype: pandas.DataFrame

---

### `stock_profit_sheet_by_report_delisted_em(symbol: str = 'SZ000013') -> pandas.DataFrame`

东方财富-股票-财务分析-利润表-已退市股票-按报告期
https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=SZ000013#/cwfx/lrb
:param symbol: 已退市股票代码; 带市场标识
:type symbol: str
:return: 利润表-按报告期
:rtype: pandas.DataFrame

---

### `stock_cash_flow_sheet_by_report_em(symbol: str = 'SH600519') -> pandas.DataFrame`

东方财富-股票-财务分析-现金流量表-按报告期
https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0
:param symbol: 股票代码; 带市场标识
:type symbol: str
:return: 现金流量表-按报告期
:rtype: pandas.DataFrame

---

### `stock_cash_flow_sheet_by_yearly_em(symbol: str = 'SH600519') -> pandas.DataFrame`

东方财富-股票-财务分析-现金流量表-按年度
https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0
:param symbol: 股票代码; 带市场标识
:type symbol: str
:return: 现金流量表-按年度
:rtype: pandas.DataFrame

---

### `stock_cash_flow_sheet_by_quarterly_em(symbol: str = 'SH600519') -> pandas.DataFrame`

东方财富-股票-财务分析-现金流量表-按单季度
https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0
:param symbol: 股票代码; 带市场标识
:type symbol: str
:return: 现金流量表-按单季度
:rtype: pandas.DataFrame

---

### `stock_cash_flow_sheet_by_report_delisted_em(symbol: str = 'SZ000013') -> pandas.DataFrame`

东方财富-股票-财务分析-现金流量表-已退市股票-按报告期
https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=SZ000013#/cwfx/xjllb
:param symbol: 已退市股票代码; 带市场标识
:type symbol: str
:return: 现金流量表-按报告期
:rtype: pandas.DataFrame

---

### `stock_financial_abstract(symbol: str = '600004') -> pandas.DataFrame`

新浪财经-财务报表-关键指标
https://vip.stock.finance.sina.com.cn/corp/go.php/vFD_FinanceSummary/stockid/600004.phtml
:param symbol: 股票代码
:type symbol: str
:return: 新浪财经-财务报表-关键指标
:rtype: pandas.DataFrame

---

### `stock_financial_abstract_ths(symbol: str = '000063', indicator: str = '按报告期') -> pandas.DataFrame`

同花顺-财务指标-主要指标
https://basic.10jqka.com.cn/new/000063/finance.html
:param symbol: 股票代码
:type symbol: str
:param indicator: 指标; choice of {"按报告期", "按年度", "按单季度"}
:type indicator: str
:return: 同花顺-财务指标-主要指标
:rtype: pandas.DataFrame

---

### `stock_financial_abstract_new_ths(symbol: str = '000063', indicator: str = '按报告期') -> pandas.DataFrame`

同花顺-财务指标-重要指标
https://basic.10jqka.com.cn/new/000063/finance.html
:param symbol: 股票代码
:type symbol: str
:param indicator: 指标; choice of {"按报告期", "一季度", "二季度", "三季度", "四季度", "按年度"}
:type indicator: str
:return: 同花顺-财务指标-主要指标
:rtype: pandas.DataFrame

---

### `stock_financial_analysis_indicator(symbol: str = '600004', start_year: str = '1900') -> pandas.DataFrame`

新浪财经-财务分析-财务指标
https://money.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/stockid/600004/ctrl/2019/displaytype/4.phtml
:param symbol: 股票代码
:type symbol: str
:param start_year: 开始年份
:type start_year: str
:return: 新浪财经-财务分析-财务指标
:rtype: pandas.DataFrame

---

### `stock_financial_analysis_indicator_em(symbol: str = '301389.SZ', indicator: str = '按报告期') -> pandas.DataFrame`

东方财富-A股-财务分析-主要指标
https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=SZ301389&color=b#/cwfx
:param symbol: 股票代码（带市场标识）
:type symbol: str
:param indicator: choice of {"按报告期", "按单季度"}
:type indicator: str
:return: 东方财富-A股-财务分析-主要指标
:rtype: pandas.DataFrame

---

### `stock_financial_benefit_ths(symbol: str = '000063', indicator: str = '按报告期') -> pandas.DataFrame`

同花顺-财务指标-利润表
https://basic.10jqka.com.cn/new/000063/finance.html
https://basic.10jqka.com.cn/api/stock/finance/000063_benefit.json
:param symbol: 股票代码
:type symbol: str
:param indicator: 指标; choice of {"按报告期","按单季度", "按年度"}
:type indicator: str
:return: 同花顺-财务指标-利润表
:rtype: pandas.DataFrame

---

### `stock_financial_benefit_new_ths(symbol: str = '000063', indicator: str = '按报告期') -> pandas.DataFrame`

同花顺-财务指标-利润表
https://basic.10jqka.com.cn/astockpc/astockmain/index.html#/financen?code=000063
:param symbol: 股票代码
:type symbol: str
:param indicator: 指标; choice of {"按报告期", "一季度", "二季度", "三季度", "四季度", "按年度"}
:type indicator: str
:return: 同花顺-财务指标-利润表
:rtype: pandas.DataFrame

---

### `stock_financial_debt_ths(symbol: str = '000063', indicator: str = '按报告期') -> pandas.DataFrame`

同花顺-财务指标-资产负债表
https://basic.10jqka.com.cn/new/000063/finance.html
https://basic.10jqka.com.cn/api/stock/finance/000063_debt.json
:param symbol: 股票代码
:type symbol: str
:param indicator: 指标; choice of {"按报告期", "按年度"}
:type indicator: str
:return: 同花顺-财务指标-资产负债表
:rtype: pandas.DataFrame

---

### `stock_financial_debt_new_ths(symbol: str = '000063', indicator: str = '按报告期') -> pandas.DataFrame`

同花顺-财务指标-资产负债表
https://basic.10jqka.com.cn/astockpc/astockmain/index.html#/financen?code=000063
:param symbol: 股票代码
:type symbol: str
:param indicator: 指标; choice of {"按报告期", "按年度"}
:type indicator: str
:return: 同花顺-财务指标-资产负债表
:rtype: pandas.DataFrame

---

### `stock_financial_cash_ths(symbol: str = '000063', indicator: str = '按报告期') -> pandas.DataFrame`

同花顺-财务指标-现金流量表
https://basic.10jqka.com.cn/new/000063/finance.html
https://basic.10jqka.com.cn/api/stock/finance/000063_cash.json
:param symbol: 股票代码
:type symbol: str
:param indicator: 指标; choice of {"按报告期","按单季度", "按年度"}
:type indicator: str
:return: 同花顺-财务指标-现金流量表
:rtype: pandas.DataFrame

---

### `stock_financial_cash_new_ths(symbol: str = '000063', indicator: str = '按报告期') -> pandas.DataFrame`

同花顺-财务指标-现金流量表
https://basic.10jqka.com.cn/astockpc/astockmain/index.html#/financen?code=000063
:param symbol: 股票代码
:type symbol: str
:param indicator: 指标; choice of {"按报告期", "一季度", "二季度", "三季度", "四季度", "按年度"}
:type indicator: str
:return: 同花顺-财务指标-现金流量表
:rtype: pandas.DataFrame

---

### `stock_financial_report_sina(stock: str = 'sh600600', symbol: str = '资产负债表') -> pandas.DataFrame`

新浪财经-财务报表-三大报表
https://vip.stock.finance.sina.com.cn/corp/go.php/vFD_FinanceSummary/stockid/600600/displaytype/4.phtml?source=fzb&qq-pf-to=pcqq.group
:param stock: 股票代码
:type stock: str
:param symbol: choice of {"资产负债表", "利润表", "现金流量表"}
:type symbol: str
:return: 新浪财经-财务报表-三大报表
:rtype: pandas.DataFrame

---

### `stock_financial_hk_report_em(stock: str = '00700', symbol: str = '资产负债表', indicator: str = '年度') -> pandas.DataFrame`

东方财富-港股-财务报表-三大报表
https://emweb.securities.eastmoney.com/PC_HKF10/FinancialAnalysis/index?type=web&code=00700
:param stock: 股票代码
:type stock: str
:param symbol: choice of {"资产负债表", "利润表", "现金流量表"}
:type symbol: str
:param indicator: choice of {"年度", "报告期"}
:type indicator: str
:return: 东方财富-港股-财务报表-三大报表
:rtype: pandas.DataFrame

---

### `stock_financial_hk_analysis_indicator_em(symbol: str = '00853', indicator: str = '年度') -> pandas.DataFrame`

东方财富-港股-财务分析-主要指标
https://emweb.securities.eastmoney.com/PC_HKF10/NewFinancialAnalysis/index?type=web&code=00700
:param symbol: 股票代码
:type symbol: str
:param indicator: choice of {"年度", "报告期"}
:type indicator: str
:return: 东方财富-港股-财务分析-主要指标
:rtype: pandas.DataFrame

---

### `stock_financial_us_report_em(stock: str = 'TSLA', symbol: str = '资产负债表', indicator: str = '年报') -> pandas.DataFrame`

东方财富-美股-财务分析-三大报表
https://emweb.eastmoney.com/PC_USF10/pages/index.html?code=TSLA&type=web&color=w#/cwfx
:param stock: 股票代码
:type stock: str
:param symbol: choice of {"资产负债表", "综合损益表", "现金流量表"}
:type symbol: str
:param indicator: choice of {"年报", "单季报", "累计季报"}
:type indicator: str
:return: 东方财富-美股-财务分析-三大报表
:rtype: pandas.DataFrame

---

### `stock_financial_us_analysis_indicator_em(symbol: str = 'TSLA', indicator: str = '年报') -> pandas.DataFrame`

东方财富-美股-财务分析-主要指标
https://emweb.eastmoney.com/PC_USF10/pages/index.html?code=TSLA&type=web&color=w#/cwfx
:param symbol: 股票代码
:type symbol: str
:param indicator: choice of {"年报", "单季报", "累计季报"}
:type indicator: str
:return: 东方财富-美股-财务分析-主要指标
:rtype: pandas.DataFrame

---

### `stock_lrb_em(date: str = '20240331') -> pandas.DataFrame`

东方财富-数据中心-年报季报-业绩快报-利润表
https://data.eastmoney.com/bbsj/202003/lrb.html
:param date: choice of {"20200331", "20200630", "20200930", "20201231", "..."}; 从 20100331 开始
:type date: str
:return: 利润表
:rtype: pandas.DataFrame

---

### `stock_zcfz_em(date: str = '20240331') -> pandas.DataFrame`

东方财富-数据中心-年报季报-业绩快报-资产负债表
https://data.eastmoney.com/bbsj/202003/zcfz.html
:param date: choice of {"20200331", "20200630", "20200930", "20201231", "..."}; 从 20100331 开始
:type date: str
:return: 资产负债表
:rtype: pandas.DataFrame

---

### `stock_zcfz_bj_em(date: str = '20240331') -> pandas.DataFrame`

东方财富-数据中心-年报季报-业绩快报-资产负债表
https://data.eastmoney.com/bbsj/202003/zcfz.html
:param date: choice of {"20200331", "20200630", "20200930", "20201231", "..."}; 从 20100331 开始
:type date: str
:return: 资产负债表
:rtype: pandas.DataFrame

---

### `stock_xjll_em(date: str = '20240331') -> pandas.DataFrame`

东方财富-数据中心-年报季报-业绩快报-现金流量表
https://data.eastmoney.com/bbsj/202003/xjll.html
:param date: choice of {"20200331", "20200630", "20200930", "20201231", "..."}; 从 20100331 开始
:type date: str
:return: 现金流量表
:rtype: pandas.DataFrame

---

### `stock_yjbb_em(date: str = '20200331') -> pandas.DataFrame`

东方财富-数据中心-年报季报-业绩快报-业绩报表
https://data.eastmoney.com/bbsj/202003/yjbb.html
:param date: "20200331", "20200630", "20200930", "20201231"; 从 20100331 开始
:type date: str
:return: 业绩报表
:rtype: pandas.DataFrame

---

### `stock_yjkb_em(date: str = '20211231') -> pandas.DataFrame`

东方财富-数据中心-年报季报-业绩快报
https://data.eastmoney.com/bbsj/202003/yjkb.html
:param date: 财报发布日期; choice of {"20200331", "20200630", "20200930", "20201231", ...}; 从 20100331 开始
:type date: str
:return: 业绩快报
:rtype: pandas.DataFrame

---

### `stock_yjyg_em(date: str = '20200331') -> pandas.DataFrame`

东方财富-数据中心-年报季报-业绩预告
https://data.eastmoney.com/bbsj/202003/yjyg.html
:param date: 财报发布日期; choice of {"20200331", "20200630", "20200930", "20201231", ...}; 从 20081231 开始
:type date: str
:return: 业绩预告
:rtype: pandas.DataFrame

---

### `stock_profit_forecast_em(symbol: str = '') -> pandas.DataFrame`

东方财富网-数据中心-研究报告-盈利预测
https://data.eastmoney.com/report/profitforecast.jshtml
:param symbol: "", 默认为获取全部数据; symbol="船舶制造", 则获取具体行业板块的数据;
行业板块可以通过 ak.stock_board_industry_name_em() 接口获取
:type symbol: str
:return: 盈利预测
:rtype: pandas.DataFrame

---

### `stock_profit_forecast_ths(symbol: str = '600519', indicator: str = '预测年报每股收益') -> pandas.DataFrame`

同花顺-盈利预测
https://basic.10jqka.com.cn/new/600519/worth.html
:param symbol: 股票代码
:type symbol: str
:param indicator: choice of {"预测年报每股收益", "预测年报净利润", "业绩预测详表-机构", "业绩预测详表-详细指标预测"}
:type indicator: str
:return: 盈利预测
:rtype: pandas.DataFrame

---

## 估值与市场宽度

### `stock_a_all_pb() -> pandas.DataFrame`

全部A股-等权重市净率、中位数市净率
https://legulegu.com/stockdata/all-pb
:return: 全部A股-等权重市盈率、中位数市盈率
:rtype: pandas.DataFrame

---

### `stock_a_ttm_lyr() -> pandas.DataFrame`

全部 A 股-等权重市盈率、中位数市盈率
:return: 全部A股-等权重市盈率、中位数市盈率
:rtype: pandas.DataFrame

---

### `stock_a_below_net_asset_statistics(symbol: str = '全部A股') -> pandas.DataFrame`

破净股统计历史走势
https://www.legulegu.com/stockdata/below-net-asset-statistics
:param symbol: choice of {"全部A股", "沪深300", "上证50", "中证500"}
:type symbol: str
:return: 破净股统计历史走势
:rtype: pandas.DataFrame

---

### `stock_a_congestion_lg() -> pandas.DataFrame`

乐咕乐股-大盘拥挤度
https://legulegu.com/stockdata/ashares-congestion
:return: 大盘拥挤度
:rtype: pandas.DataFrame

---

### `stock_a_gxl_lg(symbol: str = '上证A股') -> pandas.DataFrame`

乐咕乐股-股息率-A 股股息率
https://legulegu.com/stockdata/guxilv
:param symbol: choice of {"上证A股", "深证A股", "创业板", "科创板"}
:type symbol: str
:return: A 股股息率
:rtype: pandas.DataFrame

---

### `stock_a_high_low_statistics(symbol: str = 'all') -> pandas.DataFrame`

乐咕乐股-创新高、新低的股票数量
https://www.legulegu.com/stockdata/high-low-statistics
:param symbol: choice of {"all", "sz50", "hs300", "zz500"}
:type symbol: str
:return: 创新高、新低的股票数量
:rtype: pandas.DataFrame

---

### `stock_index_pe_lg(symbol: str = '沪深300') -> pandas.DataFrame`

乐咕乐股-指数市盈率
https://legulegu.com/stockdata/sz50-ttm-lyr
:param symbol: choice of {"上证50", "沪深300", "上证380", "创业板50", "中证500", "上证180", "深证红利", "深证100", "中证1000", "上证红利", "中证100", "中证800"}
:type symbol: str
:return: 指定指数的市盈率数据
:rtype: pandas.DataFrame

---

### `stock_index_pb_lg(symbol: str = '上证50') -> pandas.DataFrame`

乐咕乐股-指数市净率
https://legulegu.com/stockdata/sz50-pb
:param symbol: choice of {"上证50", "沪深300", "上证380", "创业板50", "中证500", "上证180", "深证红利", "深证100", "中证1000", "上证红利", "中证100", "中证800"}
:type symbol: str
:return: 指定指数的市净率数据
:rtype: pandas.DataFrame

---

### `stock_market_pe_lg(symbol: str = '深证') -> pandas.DataFrame`

乐咕乐股-主板市盈率
https://legulegu.com/stockdata/shanghaiPE
:param symbol: choice of {"上证", "深证", "创业板", "科创版"}
:type symbol: str
:return: 指定市场的市盈率数据
:rtype: pandas.DataFrame

---

### `stock_market_pb_lg(symbol: str = '上证') -> pandas.DataFrame`

乐咕乐股-主板市净率
https://legulegu.com/stockdata/shanghaiPB
:param symbol: choice of {"上证", "深证", "创业板", "科创版"}
:type symbol: str
:return: 指定市场的市净率数据
:rtype: pandas.DataFrame

---

### `stock_buffett_index_lg() -> pandas.DataFrame`

乐估乐股-底部研究-巴菲特指标
https://legulegu.com/stockdata/marketcap-gdp
:return: 巴菲特指标
:rtype: pandas.DataFrame

---

### `stock_ebs_lg() -> pandas.DataFrame`

乐咕乐股-股债利差
https://legulegu.com/stockdata/equity-bond-spread
:return: 股债利差
:rtype: pandas.DataFrame

---

### `stock_zh_valuation_baidu(symbol: str = '002044', indicator: str = '总市值', period: str = '近一年') -> pandas.DataFrame`

百度股市通-A股-财务报表-估值数据
https://gushitong.baidu.com/stock/ab-002044
:param symbol: 股票代码
:type symbol: str
:param indicator: choice of {"总市值", "市盈率(TTM)", "市盈率(静)", "市净率", "市现率"}
:type indicator: str
:param period: choice of {"近一年", "近三年", "近五年", "近十年", "全部"}
:type period: str
:return: 估值数据
:rtype: pandas.DataFrame

---

### `stock_hk_valuation_baidu(symbol: str = '06969', indicator: str = '总市值', period: str = '近一年') -> pandas.DataFrame`

百度股市通-港股-财务报表-估值数据
https://gushitong.baidu.com/stock/hk-06969
:param symbol: 股票代码
:type symbol: str
:param indicator: choice of {"总市值", "市盈率(TTM)", "市盈率(静)", "市净率", "市现率"}
:type indicator: str
:param period: choice of {"近一年", "近三年", "全部"}
:type period: str
:return: 估值数据
:rtype: pandas.DataFrame

---

### `stock_us_valuation_baidu(symbol: str = 'NVDA', indicator: str = '总市值', period: str = '近一年') -> pandas.DataFrame`

百度股市通-美股-财务报表-估值数据
https://gushitong.baidu.com/stock/us-NVDA
:param symbol: 股票代码
:type symbol: str
:param indicator: choice of {"总市值", "市盈率(TTM)", "市盈率(静)", "市净率", "市现率"}
:type indicator: str
:param period: choice of {"近一年", "近三年", "全部"}
:type period: str
:return: 估值数据
:rtype: pandas.DataFrame

---

### `stock_zh_valuation_comparison_em(symbol: str = 'SZ000895') -> pandas.DataFrame`

东方财富-行情中心-同行比较-估值比较
https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=000895&color=b#/thbj/gzbj
:param symbol: 股票代码
:type symbol: str
:return: 估值比较
:rtype: pandas.DataFrame

---

### `stock_hk_valuation_comparison_em(symbol: str = '03900') -> pandas.DataFrame`

东方财富-港股-行业对比-估值对比
https://emweb.securities.eastmoney.com/PC_HKF10/pages/home/index.html?code=03900&type=web&color=w#/IndustryComparison
:param symbol: 股票代码
:type symbol: str
:return: 估值对比
:rtype: pandas.DataFrame

---

### `stock_value_em(symbol: str = '300766') -> pandas.DataFrame`

东方财富网-数据中心-估值分析-每日互动-每日互动-估值分析
https://data.eastmoney.com/gzfx/detail/300766.html
:param symbol: 股票代码
:type symbol: str
:return: 估值分析
:rtype: pandas.DataFrame

---

### `stock_cyq_em(symbol: str = '000001', adjust: str = '') -> pandas.DataFrame`

东方财富网-概念板-行情中心-日K-筹码分布
https://quote.eastmoney.com/concept/sz000001.html
:param symbol: 股票代码
:type symbol: str
:param adjust: choice of {"qfq": "前复权", "hfq": "后复权", "": "不复权"}
:type adjust: str
:return: 筹码分布
:rtype: pandas.DataFrame

---

### `stock_zh_dupont_comparison_em(symbol: str = 'SZ000895') -> pandas.DataFrame`

东方财富-行情中心-同行比较-杜邦分析比较
https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=000895&color=b#/thbj/dbfxbj
:param symbol: 股票代码
:type symbol: str
:return: 杜邦分析比较
:rtype: pandas.DataFrame

---

### `stock_zh_growth_comparison_em(symbol: str = 'SZ000895') -> pandas.DataFrame`

东方财富-行情中心-同行比较-成长性比较
https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=000895&color=b#/thbj/czxbj
:param symbol: 股票代码
:type symbol: str
:return: 成长性比较
:rtype: pandas.DataFrame

---

### `stock_zh_scale_comparison_em(symbol: str = 'SZ000895') -> pandas.DataFrame`

东方财富-行情中心-同行比较-公司规模
https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=000895&color=b#/thbj/gsgm
:type symbol: str
:return: 公司规模
:rtype: pandas.DataFrame

---

### `stock_hk_growth_comparison_em(symbol: str = '03900') -> pandas.DataFrame`

东方财富-港股-行业对比-成长性对比
https://emweb.securities.eastmoney.com/PC_HKF10/pages/home/index.html?code=03900&type=web&color=w#/IndustryComparison
:param symbol: 股票代码
:type symbol: str
:return: 成长性对比
:rtype: pandas.DataFrame

---

### `stock_hk_scale_comparison_em(symbol: str = '03900') -> pandas.DataFrame`

东方财富-港股-行业对比-规模对比
https://emweb.securities.eastmoney.com/PC_HKF10/pages/home/index.html?code=03900&type=web&color=w#/IndustryComparison
:param symbol: 股票代码
:type symbol: str
:return: 规模对比
:rtype: pandas.DataFrame

---

## 资金流向与北向

### `stock_individual_fund_flow(stock: str = '600094', market: str = 'sh') -> pandas.DataFrame`

东方财富网-数据中心-资金流向-个股
https://data.eastmoney.com/zjlx/detail.html
:param stock: 股票代码
:type stock: str
:param market: 股票市场; 上海证券交易所: sh, 深证证券交易所: sz, 北京证券交易所: bj;
:type market: str
:return: 近期个股的资金流数据
:rtype: pandas.DataFrame

---

### `stock_individual_fund_flow_rank(indicator: str = '5日') -> pandas.DataFrame`

东方财富网-数据中心-资金流向-排名
https://data.eastmoney.com/zjlx/detail.html
:param indicator: choice of {"今日", "3日", "5日", "10日"}
:type indicator: str
:return: 指定 indicator 资金流向排行
:rtype: pandas.DataFrame

---

### `stock_main_fund_flow(symbol: str = '全部股票') -> pandas.DataFrame`

东方财富网-数据中心-资金流向-主力净流入排名
https://data.eastmoney.com/zjlx/list.html
:param symbol: 全部股票; choice of {"全部股票", "沪深A股", "沪市A股", "科创板", "深市A股", "创业板", "沪市B股", "深市B股"}
:type symbol: str
:return: 主力净流入排名
:rtype: pandas.DataFrame

---

### `stock_market_fund_flow() -> pandas.DataFrame`

东方财富网-数据中心-资金流向-大盘
https://data.eastmoney.com/zjlx/dpzjlx.html
:return: 近期大盘的资金流数据
:rtype: pandas.DataFrame

---

### `stock_fund_flow_individual(symbol: str = '即时') -> pandas.DataFrame`

同花顺-数据中心-资金流向-个股资金流
https://data.10jqka.com.cn/funds/ggzjl/#refCountId=data_55f13c2c_254
:param symbol: choice of {“即时”, "3日排行", "5日排行", "10日排行", "20日排行"}
:type symbol: str
:return: 个股资金流
:rtype: pandas.DataFrame

---

### `stock_fund_flow_industry(symbol: str = '即时') -> pandas.DataFrame`

同花顺-数据中心-资金流向-行业资金流
https://data.10jqka.com.cn/funds/hyzjl/#refCountId=data_55f13c2c_254
:param symbol: choice of {“即时”, "3日排行", "5日排行", "10日排行", "20日排行"}
:type symbol: str
:return: 行业资金流
:rtype: pandas.DataFrame

---

### `stock_fund_flow_concept(symbol: str = '即时') -> pandas.DataFrame`

同花顺-数据中心-资金流向-概念资金流
https://data.10jqka.com.cn/funds/gnzjl/#refCountId=data_55f13c2c_254
:param symbol: choice of {“即时”, "3日排行", "5日排行", "10日排行", "20日排行"}
:type symbol: str
:return: 概念资金流
:rtype: pandas.DataFrame

---

### `stock_fund_flow_big_deal() -> pandas.DataFrame`

同花顺-数据中心-资金流向-大单追踪
https://data.10jqka.com.cn/funds/ddzz
:return: 大单追踪
:rtype: pandas.DataFrame

---

### `stock_sector_fund_flow_rank(indicator: str = '今日', sector_type: str = '行业资金流') -> pandas.DataFrame`

东方财富网-数据中心-资金流向-板块资金流-排名
https://data.eastmoney.com/bkzj/hy.html
:param indicator: choice of {"今日", "5日", "10日"}
:type indicator: str
:param sector_type: choice of {"行业资金流", "概念资金流", "地域资金流"}
:type sector_type: str
:return: 指定参数的资金流排名数据
:rtype: pandas.DataFrame

---

### `stock_sector_fund_flow_hist(symbol: str = '汽车服务') -> pandas.DataFrame`

东方财富网-数据中心-资金流向-行业资金流-行业历史资金流
https://data.eastmoney.com/bkzj/BK1034.html
:param symbol: 行业名称
:type symbol: str
:return: xx行业个股资金流
:rtype: pandas.DataFrame

---

### `stock_sector_fund_flow_summary(symbol: str = '电源设备', indicator: str = '今日') -> pandas.DataFrame`

东方财富网-数据中心-资金流向-行业资金流-xx行业个股资金流
https://data.eastmoney.com/bkzj/BK1034.html
:param symbol: 行业名称
:type symbol: str
:param indicator: choice of {"今日", "5日", "10日"}
:type indicator: str
:return: xx行业个股资金流
:rtype: pandas.DataFrame

---

### `stock_concept_fund_flow_hist(symbol: str = '数据要素') -> pandas.DataFrame`

东方财富网-数据中心-资金流向-概念资金流-概念历史资金流
https://data.eastmoney.com/bkzj/BK0574.html
:param symbol: 概念名称
:type symbol: str
:return: 概念历史资金流
:rtype: pandas.DataFrame

---

### `stock_hsgt_fund_flow_summary_em() -> pandas.DataFrame`

东方财富网-数据中心-资金流向-沪深港通资金流向
https://data.eastmoney.com/hsgt/index.html#lssj
:return: 沪深港通资金流向
:rtype: pandas.DataFrame

---

### `stock_hsgt_hist_em(symbol: str = '北向资金') -> pandas.DataFrame`

东方财富网-数据中心-资金流向-沪深港通资金流向-沪深港通历史数据
https://data.eastmoney.com/hsgt/index.html
:param symbol: choice of {"北向资金", "沪股通", "深股通", "南向资金", "港股通沪", "港股通深"}
:type symbol: str
:return: 沪深港通历史数据
:rtype: pandas.DataFrame

---

### `stock_hsgt_fund_min_em(symbol: str = '北向资金') -> pandas.DataFrame`

东方财富-数据中心-沪深港通-市场概括-分时数据
https://data.eastmoney.com/hsgt/hsgtDetail/scgk.html
:param symbol: 北向资金; choice of {"北向资金", "南向资金"}
:type symbol: str
:return: 沪深港通持股-分时数据
:rtype: pandas.DataFrame

---

### `stock_hsgt_hold_stock_em(market: str = '沪股通', indicator: str = '5日排行') -> pandas.DataFrame`

东方财富-数据中心-沪深港通持股-个股排行
https://data.eastmoney.com/hsgtcg/list.html
:param market: choice of {"北向", "沪股通", "深股通"}
:type market: str
:param indicator: choice of {"今日排行", "3日排行", "5日排行", "10日排行", "月排行", "季排行", "年排行"}
:type indicator: str
:return: 指定 sector 和 indicator 的数据
:rtype: pandas.DataFrame

---

### `stock_hsgt_individual_em(symbol: str = '002008') -> pandas.DataFrame`

东方财富-数据中心-沪深港通-沪深港通持股-具体股票
https://data.eastmoney.com/hsgt/StockHdDetail/002008.html
:param symbol: 股票代码
:type symbol: str
:return: 具体股票-沪深港通持股
:rtype: pandas.DataFrame

---

### `stock_hsgt_individual_detail_em(symbol: str = '002008', start_date: str = '20220130', end_date: str = '20220330') -> pandas.DataFrame`

东方财富-数据中心-沪深港通-沪深港通持股-具体股票详情
https://data.eastmoney.com/hsgtcg/StockHdStatistics/002008.html
:param symbol: 股票代码
:type symbol: str
:param start_date: 开始时间
:type start_date: str
:param end_date: 结束时间
:type end_date: str
:return: 沪深港通持股-具体股票详情
:rtype: pandas.DataFrame

---

### `stock_hsgt_institution_statistics_em(market: str = '北向持股', start_date: str = '20220601', end_date: str = '20220609')`

东方财富网-数据中心-沪深港通-沪深港通持股-每日机构统计
https://data.eastmoney.com/hsgtcg/InstitutionStatistics.aspx
:param market: choice of {"北向持股", "南向持股", "沪股通持股", "深股通持股"}
:type market: str
:param start_date: 指定数据获取开始的时间, e.g., "20200713"
:type start_date: str
:param end_date: 指定数据获取结束的时间, e.g., "20200715"
:type end_date:str
:return: 指定市场和指定时间段的每日个股统计数据
:rtype: pandas.DataFrame

---

### `stock_hsgt_stock_statistics_em(symbol: str = '北向持股', start_date: str = '20240110', end_date: str = '20240110')`

东方财富网-数据中心-沪深港通-沪深港通持股-每日个股统计
https://data.eastmoney.com/hsgtcg/StockStatistics.aspx
market=001, 沪股通持股
market=003, 深股通持股
:param symbol: choice of {"北向持股", "南向持股"}
:type symbol: str
:param start_date: 指定数据获取开始的时间, e.g., "20200713"
:type start_date: str
:param end_date: 指定数据获取结束的时间, e.g., "20200715"
:type end_date:str
:return: 指定市场和指定时间段的每日个股统计数据
:rtype: pandas.DataFrame

---

### `stock_hsgt_board_rank_em(symbol: str = '北向资金增持行业板块排行', indicator: str = '今日') -> pandas.DataFrame`

东方财富网-数据中心-沪深港通持股-行业板块排行-北向资金增持行业板块排行
https://data.eastmoney.com/hsgtcg/bk.html
:param symbol: choice of {"北向资金增持行业板块排行", "北向资金增持概念板块排行", "北向资金增持地域板块排行"}
:type symbol: str
:param indicator: choice of {"今日", "3日", "5日", "10日", "1月", "1季", "1年"}
:type indicator: str
:return: 北向资金增持行业板块排行
:rtype: pandas.DataFrame

---

### `stock_margin_sse(start_date: str = '20010106', end_date: str = '20230922') -> pandas.DataFrame`

上海证券交易所-融资融券数据-融资融券汇总
https://www.sse.com.cn/market/othersdata/margin/sum/
:param start_date: 交易开始日期
:type start_date: str
:param end_date: 交易结束日期
:type end_date: str
:return: 融资融券汇总
:rtype: pandas.DataFrame

---

### `stock_margin_szse(date: str = '20240411') -> pandas.DataFrame`

深圳证券交易所-融资融券数据-融资融券汇总
https://www.szse.cn/disclosure/margin/margin/index.html
:param date: 交易日
:type date: str
:return: 融资融券汇总
:rtype: pandas.DataFrame

---

### `stock_margin_detail_sse(date: str = '20230922') -> pandas.DataFrame`

上海证券交易所-融资融券数据-融资融券明细
https://www.sse.com.cn/market/othersdata/margin/detail/
:param date: 交易日期
:type date: str
:return: 融资融券明细
:rtype: pandas.DataFrame

---

### `stock_margin_detail_szse(date: str = '20230925') -> pandas.DataFrame`

深证证券交易所-融资融券数据-融资融券交易明细
https://www.szse.cn/disclosure/margin/margin/index.html
:param date: 交易日期
:type date: str
:return: 融资融券明细
:rtype: pandas.DataFrame

---

### `stock_margin_account_info() -> pandas.DataFrame`

东方财富网-数据中心-融资融券-融资融券账户统计-两融账户信息
https://data.eastmoney.com/rzrq/zhtjday.html
:return: 融资融券账户统计
:rtype: pandas.DataFrame

---

### `stock_margin_ratio_pa(symbol: str = '深市', date: str = '20260113') -> pandas.DataFrame`

融资融券-标的证券名单及保证金比例查询
https://stock.pingan.com/static/webinfo/margin/business.html?businessType=0
:param symbol: choice of {"深市", "沪市", "北交所"}
:type symbol: str
:param date: 交易日期
:type date: str
:return: 标的证券名单及保证金比例查询
:rtype: pandas.DataFrame

---

### `stock_margin_underlying_info_szse(date: str = '20221129') -> pandas.DataFrame`

深圳证券交易所-融资融券数据-标的证券信息
https://www.szse.cn/disclosure/margin/object/index.html
:param date: 交易日
:type date: str
:return: 标的证券信息
:rtype: pandas.DataFrame

---

## 股东与机构

### `stock_gdfx_top_10_em(symbol: str = 'sh688686', date: str = '20210630') -> pandas.DataFrame`

东方财富网-个股-十大股东
https://emweb.securities.eastmoney.com/PC_HSF10/ShareholderResearch/Index?type=web&code=SH688686#sdgd-0
:param symbol: 带市场标识的股票代码
:type symbol: str
:param date: 报告期
:type date: str
:return: 十大股东
:rtype: pandas.DataFrame

---

### `stock_gdfx_free_top_10_em(symbol: str = 'sh688686', date: str = '20240930') -> pandas.DataFrame`

东方财富网-个股-十大流通股东
https://emweb.securities.eastmoney.com/PC_HSF10/ShareholderResearch/Index?type=web&code=SH688686#sdltgd-0
:param symbol: 带市场标识的股票代码
:type symbol: str
:param date: 报告期
:type date: str
:return: 十大股东
:rtype: pandas.DataFrame

---

### `stock_gdfx_holding_detail_em(date: str = '20230331', indicator: str = '个人', symbol: str = '新进') -> pandas.DataFrame`

东方财富网-数据中心-股东分析-股东持股明细-十大股东
https://data.eastmoney.com/gdfx/HoldingAnalyse.html
:param date: 报告期
:type date: str
:param indicator: 股东类型; choice of {"个人", "基金", "QFII", "社保", "券商", "信托"}
:type indicator: str
:param symbol: 持股变动; choice of {"新进", "增加", "不变", "减少"}
:type symbol: str
:return: 十大股东
:rtype: pandas.DataFrame

---

### `stock_gdfx_holding_analyse_em(date: str = '20230331') -> pandas.DataFrame`

东方财富网-数据中心-股东分析-股东持股分析-十大股东
https://data.eastmoney.com/gdfx/HoldingAnalyse.html
:param date: 报告期
:type date: str
:return: 十大股东
:rtype: pandas.DataFrame

---

### `stock_gdfx_holding_change_em(date: str = '20210930') -> pandas.DataFrame`

东方财富网-数据中心-股东分析-股东持股变动统计-十大股东
https://data.eastmoney.com/gdfx/HoldingAnalyse.html
:param date: 报告期
:type date: str
:return: 十大流通股东
:rtype: pandas.DataFrame

---

### `stock_gdfx_holding_statistics_em(date: str = '20210930') -> pandas.DataFrame`

东方财富网-数据中心-股东分析-股东持股统计-十大股东
https://data.eastmoney.com/gdfx/HoldingAnalyse.html
:param date: 报告期
:type date: str
:return: 十大股东
:rtype: pandas.DataFrame

---

### `stock_gdfx_holding_teamwork_em(symbol: str = '社保') -> pandas.DataFrame`

东方财富网-数据中心-股东分析-股东协同-十大股东
https://data.eastmoney.com/gdfx/HoldingAnalyse.html
:param symbol: 全部; choice of {"全部", "个人", "基金", "QFII", "社保", "券商", "信托"}
:type symbol: str
:return: 十大股东
:rtype: pandas.DataFrame

---

### `stock_gdfx_free_holding_detail_em(date: str = '20210930') -> pandas.DataFrame`

东方财富网-数据中心-股东分析-股东持股明细-十大流通股东
https://data.eastmoney.com/gdfx/HoldingAnalyse.html
:param date: 报告期
:type date: str
:return: 十大流通股东
:rtype: pandas.DataFrame

---

### `stock_gdfx_free_holding_analyse_em(date: str = '20230930') -> pandas.DataFrame`

东方财富网-数据中心-股东分析-股东持股分析-十大流通股东
https://data.eastmoney.com/gdfx/HoldingAnalyse.html
:param date: 报告期
:type date: str
:return: 十大流通股东
:rtype: pandas.DataFrame

---

### `stock_gdfx_free_holding_change_em(date: str = '20210930') -> pandas.DataFrame`

东方财富网-数据中心-股东分析-股东持股变动统计-十大流通股东
https://data.eastmoney.com/gdfx/HoldingAnalyse.html
:param date: 报告期
:type date: str
:return: 十大流通股东
:rtype: pandas.DataFrame

---

### `stock_gdfx_free_holding_statistics_em(date: str = '20210630') -> pandas.DataFrame`

东方财富网-数据中心-股东分析-股东持股统计-十大流通股东
https://data.eastmoney.com/gdfx/HoldingAnalyse.html
:param date: 报告期
:type date: str
:return: 十大流通股东
:rtype: pandas.DataFrame

---

### `stock_gdfx_free_holding_teamwork_em(symbol: str = '社保') -> pandas.DataFrame`

东方财富网-数据中心-股东分析-股东协同-十大流通股东
https://data.eastmoney.com/gdfx/HoldingAnalyse.html
:param symbol: 全部; choice of {"全部", "个人", "基金", "QFII", "社保", "券商", "信托"}
:type symbol: str
:return: 十大流通股东
:rtype: pandas.DataFrame

---

### `stock_zh_a_gdhs(symbol: str = '20230930') -> pandas.DataFrame`

东方财富网-数据中心-特色数据-股东户数
https://data.eastmoney.com/gdhs/
:param symbol: choice of {"最新", "每个季度末"}, 其中 每个季度末需要写成 `20230930` 格式
:type symbol: str
:return: 股东户数
:rtype: pandas.DataFrame

---

### `stock_zh_a_gdhs_detail_em(symbol: str = '000001') -> pandas.DataFrame`

东方财富网-数据中心-特色数据-股东户数详情
https://data.eastmoney.com/gdhs/detail/000002.html
:param symbol: 股票代码
:type symbol: str
:return: 股东户数
:rtype: pandas.DataFrame

---

### `stock_circulate_stock_holder(symbol: str = '600000') -> pandas.DataFrame`

新浪财经-股东股本-流通股东
P.S. 特定股票特定时间只有前 5 个; e.g., 000002
https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CirculateStockHolder/stockid/600000.phtml
:param symbol: 股票代码
:type symbol: str
:return: 新浪财经-股东股本-流通股东
:rtype: pandas.DataFrame

---

### `stock_main_stock_holder(stock: str = '600004') -> pandas.DataFrame`

新浪财经-股本股东-主要股东
P.S. 特定股票特定时间只有前 5 个; e.g., 000002
https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_StockHolder/stockid/600004.phtml
:param stock: 股票代码
:type stock: str
:return: 新浪财经-股本股东-主要股东
:rtype: pandas.DataFrame

---

### `stock_fund_stock_holder(symbol: str = '600004') -> pandas.DataFrame`

新浪财经-股本股东-基金持股
https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_FundStockHolder/stockid/600004.phtml
:param symbol: 股票代码
:type symbol: str
:return: 新浪财经-股本股东-基金持股
:rtype: pandas.DataFrame

---

### `stock_institute_hold(symbol: str = '20051') -> pandas.DataFrame`

新浪财经-股票-机构持股一览表
https://vip.stock.finance.sina.com.cn/q/go.php/vComStockHold/kind/jgcg/index.phtml
:param symbol: 从 2005 年开始, {"一季报":1, "中报":2 "三季报":3 "年报":4}, e.g., "20191", 其中的 1 表示一季报; "20193", 其中的 3 表示三季报;
:type symbol: str
:return: 机构持股一览表
:rtype: pandas.DataFrame

---

### `stock_institute_hold_detail(stock: str = '600433', quarter: str = '20201') -> pandas.DataFrame`

新浪财经-股票-机构持股详情
https://vip.stock.finance.sina.com.cn/q/go.php/vComStockHold/kind/jgcg/index.phtml
:param stock: 股票代码
:type stock: str
:param quarter: 从 2005 年开始, {"一季报":1, "中报":2 "三季报":3 "年报":4}, e.g., "20191", 其中的 1 表示一季报; "20193", 其中的 3 表示三季报;
:type quarter: str
:return: 指定股票和财报时间的机构持股数据
:rtype: pandas.DataFrame

---

### `stock_institute_recommend(symbol: str = '投资评级选股') -> pandas.DataFrame`

新浪财经-机构推荐池-最新投资评级
http://stock.finance.sina.com.cn/stock/go.php/vIR_RatingNewest/index.phtml
:param symbol: choice of {'最新投资评级', '上调评级股票', '下调评级股票', '股票综合评级', '首次评级股票', '目标涨幅排名', '机构关注度', '行业关注度', '投资评级选股'}
:type symbol: str
:return: 最新投资评级数据
:rtype: pandas.DataFrame

---

### `stock_institute_recommend_detail(symbol: str = '000001') -> pandas.DataFrame`

新浪财经-机构推荐池-股票评级记录
http://stock.finance.sina.com.cn/stock/go.php/vIR_StockSearch/key/sz000001.phtml
:param symbol: 股票代码
:type symbol: str
:return: 具体股票的股票评级记录
:rtype: pandas.DataFrame

---

### `stock_hold_change_cninfo(symbol: str = '全部') -> pandas.DataFrame`

巨潮资讯-数据中心-专题统计-股东股本-股本变动
https://webapi.cninfo.com.cn/#/thematicStatistics
:param symbol: choice of {"深市主板", "沪市", "创业板", "科创板", "北交所", "全部"}
:type symbol: str
:return: 股本变动
:rtype: pandas.DataFrame

---

### `stock_hold_control_cninfo(symbol: str = '全部') -> pandas.DataFrame`

巨潮资讯-数据中心-专题统计-股东股本-实际控制人持股变动
https://webapi.cninfo.com.cn/#/thematicStatistics
:param symbol: choice of {"单独控制", "实际控制人", "一致行动人", "家族控制", "全部"}; 从 2010 开始
:type symbol: str
:return: 实际控制人持股变动
:rtype: pandas.DataFrame

---

### `stock_hold_management_detail_cninfo(symbol: str = '增持') -> pandas.DataFrame`

巨潮资讯-数据中心-专题统计-股东股本-高管持股变动明细
https://webapi.cninfo.com.cn/#/thematicStatistics
:param symbol: choice of {"增持", "减持"}
:type symbol: str
:return: 高管持股变动明细
:rtype: pandas.DataFrame

---

### `stock_hold_management_detail_em() -> pandas.DataFrame`

东方财富网-数据中心-特色数据-高管持股-董监高及相关人员持股变动明细
https://data.eastmoney.com/executive/list.html
:return: 董监高及相关人员持股变动明细
:rtype: pandas.DataFrame

---

### `stock_hold_management_person_em(symbol: str = '001308', name: str = '吴远') -> pandas.DataFrame`

东方财富网-数据中心-特色数据-高管持股-人员增减持股变动明细
https://data.eastmoney.com/executive/personinfo.html?name=%E5%90%B4%E8%BF%9C&code=001308
:param symbol: 股票代码
:type name: str
:param name: 高管名称
:type symbol: str
:return: 人员增减持股变动明细
:rtype: pandas.DataFrame

---

### `stock_hold_num_cninfo(date: str = '20210630') -> pandas.DataFrame`

巨潮资讯-数据中心-专题统计-股东股本-股东人数及持股集中度
https://webapi.cninfo.com.cn/#/thematicStatistics
:param date: choice of {"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"}; 从 20170331 开始
:type date: str
:return: 股东人数及持股集中度
:rtype: pandas.DataFrame

---

### `stock_ggcg_em(symbol: str = '全部') -> pandas.DataFrame`

东方财富网-数据中心-特色数据-高管持股
https://data.eastmoney.com/executive/gdzjc.html
:param symbol: choice of {"全部", "股东增持", "股东减持"}
:type symbol: str
:return: 高管持股
:rtype: pandas.DataFrame

---

### `stock_inner_trade_xq() -> pandas.DataFrame`

雪球-行情中心-沪深股市-内部交易
https://xueqiu.com/hq/insider
:return: 内部交易
:rtype: pandas.DataFrame

---

### `stock_report_fund_hold(symbol: str = '基金持仓', date: str = '20210331') -> pandas.DataFrame`

东方财富网-数据中心-主力数据-基金持仓
http://data.eastmoney.com/zlsj/2020-12-31-1-2.html
:param symbol: choice of {"基金持仓", "QFII持仓", "社保持仓", "券商持仓", "保险持仓", "信托持仓"}
:type symbol: str
:param date: 财报发布日期, xxxx-03-31, xxxx-06-30, xxxx-09-30, xxxx-12-31
:type date: str
:return: 基金持仓数据
:rtype: pandas.DataFrame

---

### `stock_report_fund_hold_detail(symbol: str = '008286', date: str = '20220331') -> pandas.DataFrame`

东方财富网-数据中心-主力数据-基金持仓-明细
http://data.eastmoney.com/zlsj/ccjj/2020-12-31-008286.html
:param symbol: 基金代码
:type symbol: str
:param date: 财报发布日期, xxxx-03-31, xxxx-06-30, xxxx-09-30, xxxx-12-31
:type date: str
:return: 基金持仓-明细数据
:rtype: pandas.DataFrame

---

### `stock_jgdy_detail_em(date: str = '20241211') -> pandas.DataFrame`

东方财富网-数据中心-特色数据-机构调研-机构调研详细
https://data.eastmoney.com/jgdy/xx.html
:param date: 开始时间
:type date: str
:return: 机构调研详细
:rtype: pandas.DataFrame

---

### `stock_jgdy_tj_em(date: str = '20220101') -> pandas.DataFrame`

东方财富网-数据中心-特色数据-机构调研-机构调研统计
https://data.eastmoney.com/jgdy/tj.html
:param date: 开始时间
:type date: str
:return: 机构调研统计
:rtype: pandas.DataFrame

---

## 板块与行业

### `stock_board_concept_name_em() -> pandas.DataFrame`

东方财富网-行情中心-沪深京板块-概念板块-名称
https://quote.eastmoney.com/center/boardlist.html#concept_board
:return: 概念板块-名称
:rtype: pandas.DataFrame

---

### `stock_board_concept_name_ths() -> pandas.DataFrame`

同花顺-板块-概念板块-概念
http://q.10jqka.com.cn/thshy/
:return: 所有概念板块的名称和链接
:rtype: pandas.DataFrame

---

### `stock_board_concept_spot_em(symbol: str = '可燃冰') -> pandas.DataFrame`

东方财富网-行情中心-沪深京板块-概念板块-实时行情
https://quote.eastmoney.com/bk/90.BK0818.html
:param symbol: 概念板块代码
:type symbol: str
:return: 概念板块-实时行情
:rtype: pandas.DataFrame

---

### `stock_board_concept_hist_em(symbol: str = '绿色电力', period: str = 'daily', start_date: str = '20220101', end_date: str = '20221128', adjust: str = '') -> pandas.DataFrame`

东方财富网-沪深板块-概念板块-历史行情
https://quote.eastmoney.com/bk/90.BK0715.html
:param symbol: 板块名称
:type symbol: str
:type period: 周期; choice of {"daily", "weekly", "monthly"}
:param period: 板块名称
:param start_date: 开始时间
:type start_date: str
:param end_date: 结束时间
:type end_date: str
:param adjust: choice of {'': 不复权, "qfq": 前复权, "hfq": 后复权}
:type adjust: str
:return: 历史行情
:rtype: pandas.DataFrame

---

### `stock_board_concept_hist_min_em(symbol: str = '长寿药', period: str = '5') -> pandas.DataFrame`

东方财富网-沪深板块-概念板块-分时历史行情
https://quote.eastmoney.com/bk/90.BK0715.html
:param symbol: 板块名称
:type symbol: str
:param period: choice of {"1", "5", "15", "30", "60"}
:type period: str
:return: 分时历史行情
:rtype: pandas.DataFrame

---

### `stock_board_concept_cons_em(symbol: str = '融资融券') -> pandas.DataFrame`

东方财富-沪深板块-概念板块-板块成份
https://quote.eastmoney.com/center/boardlist.html#boards-BK06551
:param symbol: 板块名称或者板块代码
:type symbol: str
:return: 板块成份
:rtype: pandas.DataFrame

---

### `stock_board_concept_info_ths(symbol: str = '阿里巴巴概念') -> pandas.DataFrame`

同花顺-板块-概念板块-板块简介
http://q.10jqka.com.cn/gn/detail/code/301558/
:param symbol: 板块简介
:type symbol: str
:return: 板块简介
:rtype: pandas.DataFrame

---

### `stock_board_concept_index_ths(symbol: str = '阿里巴巴概念', start_date: str = '20200101', end_date: str = '20250228') -> pandas.DataFrame`

同花顺-板块-概念板块-指数数据
https://q.10jqka.com.cn/gn/detail/code/301558/
:param start_date: 开始时间
:type start_date: str
:param end_date: 结束时间
:type end_date: str
:param symbol: 指数数据
:type symbol: str
:return: 指数数据
:rtype: pandas.DataFrame

---

### `stock_board_concept_summary_ths() -> pandas.DataFrame`

同花顺-数据中心-概念板块-概念时间表
https://q.10jqka.com.cn/gn/
:return: 概念时间表
:rtype: pandas.DataFrame

---

### `stock_board_industry_name_em() -> pandas.DataFrame`

东方财富网-沪深板块-行业板块-名称
https://quote.eastmoney.com/center/boardlist.html#industry_board
:return: 行业板块-名称
:rtype: pandas.DataFrame

---

### `stock_board_industry_name_ths() -> pandas.DataFrame`

同花顺-板块-行业板块-行业
http://q.10jqka.com.cn/thshy/
:return: 所有行业板块的名称和链接
:rtype: pandas.DataFrame

---

### `stock_board_industry_spot_em(symbol: str = '小金属') -> pandas.DataFrame`

东方财富网-沪深板块-行业板块-实时行情
https://quote.eastmoney.com/bk/90.BK1027.html
:param symbol: 板块名称 or 东财板块代码
:type symbol: str
:return: 实时行情
:rtype: pandas.DataFrame

---

### `stock_board_industry_hist_em(symbol: str = '小金属', start_date: str = '20211201', end_date: str = '20220401', period: str = '日k', adjust: str = '') -> pandas.DataFrame`

东方财富网-沪深板块-行业板块-历史行情
https://quote.eastmoney.com/bk/90.BK1027.html
:param symbol: 板块名称
:type symbol: str
:param start_date: 开始时间
:type start_date: str
:param end_date: 结束时间
:type end_date: str
:param period: 周期; choice of {"日k", "周k", "月k"}
:type period: str
:param adjust: choice of {'': 不复权, "qfq": 前复权, "hfq": 后复权}
:type adjust: str
:return: 历史行情
:rtype: pandas.DataFrame

---

### `stock_board_industry_hist_min_em(symbol: str = '小金属', period: str = '5') -> pandas.DataFrame`

东方财富网-沪深板块-行业板块-分时历史行情
https://quote.eastmoney.com/bk/90.BK1027.html
:param symbol: 板块名称
:type symbol: str
:param period: choice of {"1", "5", "15", "30", "60"}
:type period: str
:return: 分时历史行情
:rtype: pandas.DataFrame

---

### `stock_board_industry_cons_em(symbol: str = '小金属') -> pandas.DataFrame`

东方财富网-沪深板块-行业板块-板块成份
https://data.eastmoney.com/bkzj/BK1027.html
:param symbol: 板块名称或者板块代码
:type symbol: str
:return: 板块成份
:rtype: pandas.DataFrame

---

### `stock_board_industry_info_ths(symbol: str = '半导体') -> pandas.DataFrame`

同花顺-板块-行业板块-板块简介
http://q.10jqka.com.cn/gn/detail/code/301558/
:param symbol: 板块简介
:type symbol: str
:return: 板块简介
:rtype: pandas.DataFrame

---

### `stock_board_industry_index_ths(symbol: str = '元件', start_date: str = '20200101', end_date: str = '20240108') -> pandas.DataFrame`

同花顺-板块-行业板块-指数数据
https://q.10jqka.com.cn/thshy/detail/code/881270/
:param start_date: 开始时间
:type start_date: str
:param end_date: 结束时间
:type end_date: str
:param symbol: 指数数据
:type symbol: str
:return: 指数数据
:rtype: pandas.DataFrame

---

### `stock_board_industry_summary_ths() -> pandas.DataFrame`

同花顺-数据中心-行业板块-同花顺行业一览表
https://q.10jqka.com.cn/thshy/
:return: 同花顺行业一览表
:rtype: pandas.DataFrame

---

### `stock_board_change_em() -> pandas.DataFrame`

东方财富-行情中心-当日板块异动详情
https://quote.eastmoney.com/changes/
:return: 当日板块异动详情页
:rtype: pandas.DataFrame

---

### `stock_sector_spot(indicator: str = '新浪行业') -> pandas.DataFrame`

新浪行业-板块行情
http://finance.sina.com.cn/stock/sl/
:param indicator: choice of {"新浪行业", "启明星行业", "概念", "地域", "行业"}
:type indicator: str
:return: 指定 indicator 的数据
:rtype: pandas.DataFrame

---

### `stock_sector_detail(sector: str = 'gn_gfgn') -> pandas.DataFrame`

新浪行业-板块行情-成份详情
http://finance.sina.com.cn/stock/sl/#area_1
:param sector: stock_sector_spot 返回的 label 值, choice of {"新浪行业", "概念", "地域", "行业"}; "启明星行业" 无详情
:type sector: str
:return: 指定 sector 的板块详情
:rtype: pandas.DataFrame

---

### `stock_industry_category_cninfo(symbol: str = '巨潮行业分类标准') -> pandas.DataFrame`

巨潮资讯-行业分类数据
https://webapi.cninfo.com.cn/#/apiDoc
查询 p_public0002 接口
:param symbol: 行业类型; choice of {"证监会行业分类标准", "巨潮行业分类标准", "申银万国行业分类标准",
"新财富行业分类标准", "国资委行业分类标准", "巨潮产业细分标准", "天相行业分类标准", "全球行业分类标准"}
:type symbol: str
:return: 行业分类数据
:rtype: pandas.DataFrame

---

### `stock_industry_change_cninfo(symbol: str = '002594', start_date: str = '20091227', end_date: str = '20220713') -> pandas.DataFrame`

巨潮资讯-上市公司行业归属的变动情况
https://webapi.cninfo.com.cn/#/apiDoc
查询 p_stock2110 接口
:param symbol: 股票代码
:type symbol: str
:param start_date: 开始变动日期
:type start_date: str
:param end_date: 结束变动日期
:type end_date: str
:return: 行业归属的变动情况
:rtype: pandas.DataFrame

---

### `stock_industry_clf_hist_sw() -> pandas.DataFrame`

申万宏源研究-行业分类-全部行业分类
https://www.swsresearch.com/swindex/pdf/SwClass2021/StockClassifyUse_stock.xls
:return: 个股行业分类变动历史
:rtype: pandas.DataFrame

---

### `stock_industry_pe_ratio_cninfo(symbol: str = '证监会行业分类', date: str = '20210910') -> pandas.DataFrame`

巨潮资讯-数据中心-行业分析-行业市盈率
http://webapi.cninfo.com.cn/#/thematicStatistics
:param symbol: choice of {"证监会行业分类", "国证行业分类"}
:type symbol: str
:param date: 查询日期
:type date: str
:return: 行业市盈率
:rtype: pandas.DataFrame

---

### `stock_esg_rate_sina() -> pandas.DataFrame`

新浪财经-ESG评级中心-ESG评级-ESG评级数据
https://finance.sina.com.cn/esg/grade.shtml
:return: ESG评级数据
:rtype: pandas.DataFrame

---

### `stock_esg_hz_sina() -> pandas.DataFrame`

新浪财经-ESG评级中心-ESG评级-华证指数
https://finance.sina.com.cn/esg/grade.shtml
:return: 华证指数
:rtype: pandas.DataFrame

---

### `stock_esg_msci_sina() -> pandas.DataFrame`

新浪财经-ESG评级中心-ESG评级-MSCI
https://finance.sina.com.cn/esg/grade.shtml
:return: MSCI
:rtype: pandas.DataFrame

---

### `stock_esg_rft_sina() -> pandas.DataFrame`

新浪财经-ESG评级中心-ESG评级-路孚特
https://finance.sina.com.cn/esg/grade.shtml
:return: 路孚特
:rtype: pandas.DataFrame

---

### `stock_esg_zd_sina() -> pandas.DataFrame`

新浪财经-ESG评级中心-ESG评级-秩鼎
https://finance.sina.com.cn/esg/grade.shtml
:return: 秩鼎
:rtype: pandas.DataFrame

---

## 龙虎榜与特色

### `stock_lhb_detail_em(start_date: str = '20230403', end_date: str = '20230417') -> pandas.DataFrame`

东方财富网-数据中心-龙虎榜单-龙虎榜详情
https://data.eastmoney.com/stock/tradedetail.html
:param start_date: 开始日期
:type start_date: str
:param end_date: 结束日期
:type end_date: str
:return: 龙虎榜详情
:rtype: pandas.DataFrame

---

### `stock_lhb_detail_daily_sina(date: str = '20240222') -> pandas.DataFrame`

龙虎榜-每日详情
https://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/lhb/index.phtml
:param date: 交易日
:type date: str
:return: 龙虎榜-每日详情
:rtype: pandas.DataFrame

---

### `stock_lhb_stock_detail_em(symbol: str = '000788', date: str = '20220315', flag: str = '卖出') -> pandas.DataFrame`

东方财富网-数据中心-龙虎榜单-个股龙虎榜详情
https://data.eastmoney.com/stock/lhb/600077.html
:param symbol: 股票代码
:type symbol: str
:param date: 查询日期; 需要通过 ak.stock_lhb_stock_detail_date_em(symbol="600077") 接口获取相应股票的有龙虎榜详情数据的日期
:type date: str
:param flag: choice of {"买入", "卖出"}
:type flag: str
:return: 个股龙虎榜详情
:rtype: pandas.DataFrame

---

### `stock_lhb_stock_detail_date_em(symbol: str = '600077') -> pandas.DataFrame`

东方财富网-数据中心-龙虎榜单-个股龙虎榜详情-日期
https://data.eastmoney.com/stock/tradedetail.html
:param symbol: 股票代码
:type symbol: str
:return: 个股龙虎榜详情-日期
:rtype: pandas.DataFrame

---

### `stock_lhb_stock_statistic_em(symbol: str = '近一月') -> pandas.DataFrame`

东方财富网-数据中心-龙虎榜单-个股上榜统计
https://data.eastmoney.com/stock/tradedetail.html
:param symbol: choice of {"近一月", "近三月", "近六月", "近一年"}
:type symbol: str
:return: 个股上榜统计
:rtype: pandas.DataFrame

---

### `stock_lhb_jgmmtj_em(start_date: str = '20240417', end_date: str = '20240430') -> pandas.DataFrame`

东方财富网-数据中心-龙虎榜单-机构买卖每日统计
https://data.eastmoney.com/stock/jgmmtj.html
:param start_date: 开始日期
:type start_date: str
:param end_date: 结束日期
:type end_date: str
:return: 机构买卖每日统计
:rtype: pandas.DataFrame

---

### `stock_lhb_jgstatistic_em(symbol: str = '近一月') -> pandas.DataFrame`

东方财富网-数据中心-龙虎榜单-机构席位追踪
https://data.eastmoney.com/stock/jgstatistic.html
:param symbol: choice of {"近一月", "近三月", "近六月", "近一年"}
:type symbol: str
:return: 机构席位追踪
:rtype: pandas.DataFrame

---

### `stock_lhb_traderstatistic_em(symbol: str = '近一月') -> pandas.DataFrame`

东方财富网-数据中心-龙虎榜单-营业部统计
https://data.eastmoney.com/stock/traderstatistic.html
:param symbol: choice of {"近一月", "近三月", "近六月", "近一年"}
:type symbol: str
:return: 营业部统计
:rtype: pandas.DataFrame

---

### `stock_lhb_yybph_em(symbol: str = '近一月') -> pandas.DataFrame`

东方财富网-数据中心-龙虎榜单-营业部排行
https://data.eastmoney.com/stock/yybph.html
:param symbol: choice of {"近一月", "近三月", "近六月", "近一年"}
:type symbol: str
:return: 营业部排行
:rtype: pandas.DataFrame

---

### `stock_lhb_yyb_detail_em(symbol: str = '10188715') -> pandas.DataFrame`

东方财富网-数据中心-龙虎榜单-营业部历史交易明细-营业部交易明细
https://data.eastmoney.com/stock/lhb/yyb/10188715.html
:param symbol: 营业部代码, 如 "10188715", 通过 ak.stock_lhb_hyyyb_em() 接口获取
:type symbol: str
:return: 营业部交易明细数据
:rtype: pandas.DataFrame

---

### `stock_lhb_hyyyb_em(start_date: str = '20220324', end_date: str = '20220324') -> pandas.DataFrame`

东方财富网-数据中心-龙虎榜单-每日活跃营业部
https://data.eastmoney.com/stock/hyyyb.html
:param start_date: 开始日期
:type start_date: str
:param end_date: 结束日期
:type end_date: str
:return: 每日活跃营业部
:rtype: pandas.DataFrame

---

### `stock_lhb_ggtj_sina(symbol: str = '5') -> pandas.DataFrame`

龙虎榜-个股上榜统计
https://vip.stock.finance.sina.com.cn/q/go.php/vLHBData/kind/ggtj/index.phtml
:param symbol: choice of {"5": 最近 5 天; "10": 最近 10 天; "30": 最近 30 天; "60": 最近 60 天;}
:type symbol: str
:return: 龙虎榜-个股上榜统计
:rtype: pandas.DataFrame

---

### `stock_lhb_jgmx_sina() -> pandas.DataFrame`

龙虎榜-机构席位成交明细
https://vip.stock.finance.sina.com.cn/q/go.php/vLHBData/kind/jgmx/index.phtml
:return: 龙虎榜-机构席位成交明细
:rtype: pandas.DataFrame

---

### `stock_lhb_jgzz_sina(symbol: str = '5') -> pandas.DataFrame`

龙虎榜-机构席位追踪
https://vip.stock.finance.sina.com.cn/q/go.php/vLHBData/kind/jgzz/index.phtml
:param symbol: choice of {"5": 最近 5 天; "10": 最近 10 天; "30": 最近 30 天; "60": 最近 60 天;}
:type symbol: str
:return: 龙虎榜-机构席位追踪
:rtype: pandas.DataFrame

---

### `stock_lhb_yytj_sina(symbol: str = '5') -> pandas.DataFrame`

龙虎榜-营业部上榜统计
https://vip.stock.finance.sina.com.cn/q/go.php/vLHBData/kind/yytj/index.phtml
:param symbol: choice of {"5": 最近 5 天; "10": 最近 10 天; "30": 最近 30 天; "60": 最近 60 天;}
:type symbol: str
:return: 龙虎榜-营业部上榜统计
:rtype: pandas.DataFrame

---

### `stock_lh_yyb_capital() -> pandas.DataFrame`

同花顺-数据中心-营业部排名-资金实力最强
https://data.10jqka.com.cn/market/longhu/
:return: 资金实力最强
:rtype: pandas.DataFrame

---

### `stock_lh_yyb_most() -> pandas.DataFrame`

同花顺-数据中心-营业部排名-上榜次数最多
https://data.10jqka.com.cn/market/longhu/
:return: 上榜次数最多
:rtype: pandas.DataFrame

---

### `stock_lh_yyb_control() -> pandas.DataFrame`

同花顺-数据中心-营业部排名-抱团操作实力
https://data.10jqka.com.cn/market/longhu/
:return: 抱团操作实力
:rtype: pandas.DataFrame

---

### `stock_dzjy_mrmx(symbol: str = '基金', start_date: str = '20220104', end_date: str = '20220104') -> pandas.DataFrame`

东方财富网-数据中心-大宗交易-每日明细
https://data.eastmoney.com/dzjy/dzjy_mrmx.html
:param symbol: choice of {'A股', 'B股', '基金', '债券'}
:type symbol: str
:param start_date: 开始日期
:type start_date: str
:param end_date: 结束日期
:type end_date: str
:return: 每日明细
:rtype: pandas.DataFrame

---

### `stock_dzjy_mrtj(start_date: str = '20220105', end_date: str = '20220105') -> pandas.DataFrame`

东方财富网-数据中心-大宗交易-每日统计
https://data.eastmoney.com/dzjy/dzjy_mrtj.html
:param start_date: 开始日期
:type start_date: str
:param end_date: 结束日期
:type end_date: str
:return: 每日统计
:rtype: pandas.DataFrame

---

### `stock_dzjy_sctj() -> pandas.DataFrame`

东方财富网-数据中心-大宗交易-市场统计
https://data.eastmoney.com/dzjy/dzjy_sctj.html
:return: 市场统计表
:rtype: pandas.DataFrame

---

### `stock_dzjy_hygtj(symbol: str = '近三月') -> pandas.DataFrame`

东方财富网-数据中心-大宗交易-活跃 A 股统计
https://data.eastmoney.com/dzjy/dzjy_hygtj.html
:param symbol: choice of {'近一月', '近三月', '近六月', '近一年'}
:type symbol: str
:return: 活跃 A 股统计
:rtype: pandas.DataFrame

---

### `stock_dzjy_hyyybtj(symbol: str = '近3日') -> pandas.DataFrame`

东方财富网-数据中心-大宗交易-活跃营业部统计
https://data.eastmoney.com/dzjy/dzjy_hyyybtj.html
:param symbol: choice of {'当前交易日', '近3日', '近5日', '近10日', '近30日'}
:type symbol: str
:return: 活跃营业部统计
:rtype: pandas.DataFrame

---

### `stock_dzjy_yybph(symbol: str = '近三月') -> pandas.DataFrame`

东方财富网-数据中心-大宗交易-营业部排行
https://data.eastmoney.com/dzjy/dzjy_yybph.html
:param symbol: choice of {'近一月', '近三月', '近六月', '近一年'}
:type symbol: str
:return: 营业部排行
:rtype: pandas.DataFrame

---

### `stock_zt_pool_em(date: str = '20241008') -> pandas.DataFrame`

东方财富网-行情中心-涨停板行情-涨停股池
https://quote.eastmoney.com/ztb/detail#type=ztgc
:param date: 交易日
:type date: str
:return: 涨停股池
:rtype: pandas.DataFrame

---

### `stock_zt_pool_previous_em(date: str = '20240415') -> pandas.DataFrame`

东方财富网-行情中心-涨停板行情-昨日涨停股池
https://quote.eastmoney.com/ztb/detail#type=zrzt
:param date: 交易日
:type date: str
:return: 昨日涨停股池
:rtype: pandas.DataFrame

---

### `stock_zt_pool_strong_em(date: str = '20241231') -> pandas.DataFrame`

东方财富网-行情中心-涨停板行情-强势股池
https://quote.eastmoney.com/ztb/detail#type=qsgc
:param date: 交易日
:type date: str
:return: 强势股池
:rtype: pandas.DataFrame

---

### `stock_zt_pool_sub_new_em(date: str = '20241231') -> pandas.DataFrame`

东方财富网-行情中心-涨停板行情-次新股池
https://quote.eastmoney.com/ztb/detail#type=cxgc
:param date: 交易日
:type date: str
:return: 次新股池
:rtype: pandas.DataFrame

---

### `stock_zt_pool_dtgc_em(date: str = '20241011') -> pandas.DataFrame`

东方财富网-行情中心-涨停板行情-跌停股池
https://quote.eastmoney.com/ztb/detail#type=dtgc
:param date: 交易日
:type date: str
:return: 跌停股池
:rtype: pandas.DataFrame

---

### `stock_zt_pool_zbgc_em(date: str = '20241011') -> pandas.DataFrame`

东方财富网-行情中心-涨停板行情-炸板股池
https://quote.eastmoney.com/ztb/detail#type=zbgc
:param date: 交易日
:type date: str
:return: 炸板股池
:rtype: pandas.DataFrame

---

### `stock_market_activity_legu() -> pandas.DataFrame`

乐咕乐股网-赚钱效应分析
https://www.legulegu.com/stockdata/market-activity
:return: 乐咕乐股网-赚钱效应分析
:rtype: pandas.DataFrame

---

### `stock_comment_em() -> pandas.DataFrame`

东方财富网-数据中心-特色数据-千股千评
https://data.eastmoney.com/stockcomment/
:return: 千股千评数据
:rtype: pandas.DataFrame

---

### `stock_hot_rank_em() -> pandas.DataFrame`

东方财富-个股人气榜-人气榜
https://guba.eastmoney.com/rank/
:return: 人气榜
:rtype: pandas.DataFrame

---

### `stock_hot_up_em() -> pandas.DataFrame`

东方财富-个股人气榜-飙升榜
https://guba.eastmoney.com/rank/
:return: 飙升榜
:rtype: pandas.DataFrame

---

### `stock_gpzy_profile_em() -> pandas.DataFrame`

东方财富网-数据中心-特色数据-股权质押-股权质押市场概况
https://data.eastmoney.com/gpzy/marketProfile.aspx
:return: 股权质押市场概况
:rtype: pandas.DataFrame

---

### `stock_gpzy_pledge_ratio_em(date: str = '20240906') -> pandas.DataFrame`

东方财富网-数据中心-特色数据-股权质押-上市公司质押比例
https://data.eastmoney.com/gpzy/pledgeRatio.aspx
:param date: 指定交易日, 访问 https://data.eastmoney.com/gpzy/pledgeRatio.aspx 查询
:type date: str
:return: 上市公司质押比例
:rtype: pandas.DataFrame

---

### `stock_sy_profile_em() -> pandas.DataFrame`

东方财富网-数据中心-特色数据-商誉-A股商誉市场概况
https://data.eastmoney.com/sy/scgk.html
:return: A股商誉市场概况
:rtype: pandas.DataFrame

---

### `stock_sy_em(date: str = '20231231') -> pandas.DataFrame`

东方财富网-数据中心-特色数据-商誉-个股商誉明细
https://data.eastmoney.com/sy/list.html
:param date: 参考网站指定的数据日期
:type date: str
:return: 个股商誉明细
:rtype: pandas.DataFrame

---

## 其他接口

### `stock_a_code_to_symbol(symbol: str = '000300') -> str`

输入股票代码判断股票市场
:param symbol: 股票代码
:type symbol: str
:return: 股票市场
:rtype: str

---

### `stock_account_statistics_em() -> pandas.DataFrame`

东方财富网-数据中心-特色数据-股票账户统计
https://data.eastmoney.com/cjsj/gpkhsj.html
:return: 股票账户统计数据
:rtype: pandas.DataFrame

---

### `stock_add_stock(symbol: str = '688166') -> pandas.DataFrame`

新浪财经-发行与分配-增发
https://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_AddStock/stockid/600004.phtml
:param symbol: 股票代码
:type symbol: str
:return: 返回增发详情
:rtype: pandas.DataFrame

---

### `stock_allotment_cninfo(symbol: str = '600030', start_date: str = '19700101', end_date: str = '22220222') -> pandas.DataFrame`

巨潮资讯-个股-配股实施方案
https://webapi.cninfo.com.cn/#/dataBrowse
:param symbol: 股票代码
:type symbol: str
:param start_date: 开始查询的日期
:type symbol: str
:param end_date: 结束查询的日期
:type symbol: str
:return: 配股实施方案
:rtype: pandas.DataFrame

---

### `stock_analyst_detail_em(analyst_id: str = '11000200926', indicator: str = '最新跟踪成分股') -> pandas.DataFrame`

东方财富网-数据中心-研究报告-东方财富分析师指数-东方财富分析师指数2020最新排行-分析师详情
https://data.eastmoney.com/invest/invest/11000257131.html
:param analyst_id: 分析师 ID, 从 ak.stock_analyst_rank_em() 获取
:type analyst_id: str
:param indicator: choice of {"最新跟踪成分股", "历史跟踪成分股", "历史指数"}
:type indicator: str
:return: 具体指标的数据
:rtype: pandas.DataFrame

---

### `stock_analyst_rank_em(year: str = '2024') -> pandas.DataFrame`

东方财富网-数据中心-研究报告-东方财富分析师指数-东方财富分析师指数
https://data.eastmoney.com/invest/invest/list.html
:param year: 从 2015 年至今
:type year: str
:return: 东方财富分析师指数
:rtype: pandas.DataFrame

---

### `stock_cg_equity_mortgage_cninfo(date: str = '20210930') -> pandas.DataFrame`

巨潮资讯-数据中心-专题统计-公司治理-股权质押
https://webapi.cninfo.com.cn/#/thematicStatistics
:param date: 开始统计时间
:type date: str
:return: 股权质押
:rtype: pandas.DataFrame

---

### `stock_cg_guarantee_cninfo(symbol: str = '全部', start_date: str = '20180630', end_date: str = '20210927') -> pandas.DataFrame`

巨潮资讯-数据中心-专题统计-公司治理-对外担保
https://webapi.cninfo.com.cn/#/thematicStatistics
:param symbol: choice of {"全部", "深市主板", "沪市", "创业板", "科创板"}
:type symbol: str
:param start_date: 开始统计时间
:type start_date: str
:param end_date: 结束统计时间
:type end_date: str
:return: 对外担保
:rtype: pandas.DataFrame

---

### `stock_cg_lawsuit_cninfo(symbol: str = '全部', start_date: str = '20180630', end_date: str = '20210927') -> pandas.DataFrame`

巨潮资讯-数据中心-专题统计-公司治理-公司诉讼
http://webapi.cninfo.com.cn/#/thematicStatistics
:param symbol: choice of {"全部", "深市主板", "沪市", "创业板", "科创板"}
:type symbol: str
:param start_date: 开始统计时间
:type start_date: str
:param end_date: 结束统计时间
:type end_date: str
:return: 对外担保
:rtype: pandas.DataFrame

---

### `stock_changes_em(symbol: str = '大笔买入') -> pandas.DataFrame`

东方财富-行情中心-盘口异动
https://quote.eastmoney.com/changes/
:param symbol: choice of {'火箭发射', '快速反弹', '大笔买入', '封涨停板', '打开跌停板', '有大买盘',
'竞价上涨', '高开5日线', '向上缺口', '60日新高', '60日大幅上涨', '加速下跌', '高台跳水',
'大笔卖出', '封跌停板', '打开涨停板', '有大卖盘', '竞价下跌', '低开5日线', '向下缺口', '60日新低', '60日大幅下跌'}
:type symbol: str
:return: 盘口异动
:rtype: pandas.DataFrame

---

### `stock_classify_sina(symbol: str = '热门概念') -> pandas.DataFrame`

按 symbol 分类后的股票
http://vip.stock.finance.sina.com.cn/mkt/
:param symbol: choice of {'申万行业', '申万二级', '热门概念', '地域板块'}
:type symbol: str
:return: 分类后的股票
:rtype: pandas.DataFrame

---

### `stock_comment_detail_scrd_desire_em(symbol: str = '600000') -> pandas.DataFrame`

东方财富网-数据中心-特色数据-千股千评-市场热度-市场参与意愿
https://data.eastmoney.com/stockcomment/stock/600000.html
:param symbol: 股票代码
:type symbol: str
:return: 市场热度-市场参与意愿
:rtype: pandas.DataFrame

---

### `stock_comment_detail_scrd_focus_em(symbol: str = '600000') -> pandas.DataFrame`

东方财富网-数据中心-特色数据-千股千评-市场热度-用户关注指数
https://data.eastmoney.com/stockcomment/stock/600000.html
:param symbol: 股票代码
:type symbol: str
:return: 市场热度-用户关注指数
:rtype: pandas.DataFrame

---

### `stock_comment_detail_zhpj_lspf_em(symbol: str = '600000') -> pandas.DataFrame`

东方财富网-数据中心-特色数据-千股千评-综合评价-历史评分
https://data.eastmoney.com/stockcomment/stock/600000.html
:param symbol: 股票代码
:type symbol: str
:return: 综合评价-历史评分
:rtype: pandas.DataFrame

---

### `stock_comment_detail_zlkp_jgcyd_em(symbol: str = '600000') -> pandas.DataFrame`

东方财富网-数据中心-特色数据-千股千评-主力控盘-机构参与度
https://data.eastmoney.com/stockcomment/stock/600000.html
:param symbol: 股票代码
:type symbol: str
:return: 主力控盘-机构参与度
:rtype: pandas.DataFrame

---

### `stock_concept_cons_futu(symbol: str = '特朗普概念股') -> pandas.DataFrame`

富途牛牛-主题投资-概念板块-成分股
https://www.futunn.com/quote/sparks-us
:param symbol: 板块名称; choice of {"巴菲特持仓", "佩洛西持仓", "特朗普概念股"}
:type symbol: str
:return: 概念板块
:rtype: pandas.DataFrame

---

### `stock_dividend_cninfo(symbol: str = '600009') -> pandas.DataFrame`

巨潮资讯-个股-历史分红
https://webapi.cninfo.com.cn/#/company?companyid=600009
:param symbol: 股票代码
:type symbol: str
:return: 历史分红
:rtype: pandas.DataFrame

---

### `stock_dxsyl_em() -> pandas.DataFrame`

东方财富网-数据中心-新股申购-打新收益率
https://data.eastmoney.com/xg/xg/dxsyl.html
:return: 打新收益率数据
:rtype: pandas.DataFrame

---

### `stock_fhps_detail_em(symbol: str = '300073') -> pandas.DataFrame`

东方财富网-数据中心-分红送配-分红送配详情
https://data.eastmoney.com/yjfp/detail/300073.html
:param symbol: 股票代码
:type symbol: str
:return: 分红送配详情
:rtype: pandas.DataFrame

---

### `stock_fhps_detail_ths(symbol: str = '603444') -> pandas.DataFrame`

同花顺-分红情况
https://basic.10jqka.com.cn/new/603444/bonus.html
:param symbol: 股票代码
:type symbol: str
:return: 分红融资
:rtype: pandas.DataFrame

---

### `stock_fhps_em(date: str = '20231231') -> pandas.DataFrame`

东方财富网-数据中心-年报季报-分红送配
https://data.eastmoney.com/yjfp/
:param date: 分红送配报告期
:type date: str
:return: 分红送配
:rtype: pandas.DataFrame

---

### `stock_gddh_em() -> pandas.DataFrame`

东方财富网-数据中心-股东大会
https://data.eastmoney.com/gddh/
:return: 股东大会
:rtype: pandas.DataFrame

---

### `stock_gpzy_distribute_statistics_bank_em() -> pandas.DataFrame`

东方财富网-数据中心-特色数据-股权质押-质押机构分布统计-银行
https://data.eastmoney.com/gpzy/distributeStatistics.aspx
:return: 质押机构分布统计-银行
:rtype: pandas.DataFrame

---

### `stock_gpzy_distribute_statistics_company_em() -> pandas.DataFrame`

东方财富网-数据中心-特色数据-股权质押-质押机构分布统计-证券公司
https://data.eastmoney.com/gpzy/distributeStatistics.aspx
:return: 质押机构分布统计-证券公司
:rtype: pandas.DataFrame

---

### `stock_gpzy_industry_data_em() -> pandas.DataFrame`

东方财富网-数据中心-特色数据-股权质押-上市公司质押比例-行业数据
https://data.eastmoney.com/gpzy/industryData.aspx
:return: pandas.DataFrame

---

### `stock_gpzy_pledge_ratio_detail_em() -> pandas.DataFrame`

东方财富网-数据中心-特色数据-股权质押-重要股东股权质押明细
https://data.eastmoney.com/gpzy/pledgeDetail.aspx
:return: pandas.DataFrame

---

### `stock_gsrl_gsdt_em(date: str = '20230808') -> pandas.DataFrame`

东方财富网-数据中心-股市日历-公司动态
https://data.eastmoney.com/gsrl/gsdt.html
:param date: 交易日
:type date: str
:return: 公司动态
:rtype: pandas.DataFrame

---

### `stock_history_dividend() -> pandas.DataFrame`

新浪财经-发行与分配-历史分红
https://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/lsfh/index.phtml
:return: 所有股票的历史分红数据
:rtype: pandas.DataFrame

---

### `stock_history_dividend_detail(symbol: str = '000002', indicator: str = '分红', date: str = '') -> pandas.DataFrame`

新浪财经-发行与分配-分红配股详情
https://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_ShareBonus/stockid/300670.phtml
:param indicator: choice of {"分红", "配股"}
:type indicator: str
:param symbol: 股票代码
:type symbol: str
:param date: 分红配股的具体日期, e.g., "1994-12-24"
:type date: str
:return: 指定 indicator, stock, date 的数据
:rtype: pandas.DataFrame

---

### `stock_hk_company_profile_em(symbol: str = '03900') -> pandas.DataFrame`

东方财富-港股-公司资料
https://emweb.securities.eastmoney.com/PC_HKF10/pages/home/index.html?code=03900&type=web&color=w#/CompanyProfile
:param symbol: 股票代码
:type symbol: str
:return: 公司资料
:rtype: pandas.DataFrame

---

### `stock_hk_dividend_payout_em(symbol: str = '03900') -> pandas.DataFrame`

东方财富-港股-核心必读-分红派息
https://emweb.securities.eastmoney.com/PC_HKF10/pages/home/index.html?code=03900&type=web&color=w#/CoreReading
:param symbol: 股票代码
:type symbol: str
:return: 分红派息
:rtype: pandas.DataFrame

---

### `stock_hk_fhpx_detail_ths(symbol: str = '0700') -> pandas.DataFrame`

同花顺-港股-分红派息
https://stockpage.10jqka.com.cn/HK0700/bonus/
:param symbol: 港股代码
:type symbol: str
:return: 分红派息
:rtype: pandas.DataFrame

---

### `stock_hk_financial_indicator_em(symbol: str = '03900') -> pandas.DataFrame`

东方财富-港股-核心必读-最新指标
https://emweb.securities.eastmoney.com/PC_HKF10/pages/home/index.html?code=03900&type=web&color=w#/CoreReading
:param symbol: 股票代码
:type symbol: str
:return: 财务指标
:rtype: pandas.DataFrame

---

### `stock_hk_gxl_lg() -> pandas.DataFrame`

乐咕乐股-股息率-恒生指数股息率
https://legulegu.com/stockdata/market/hk/dv/hsi
:return: 恒生指数股息率
:rtype: pandas.DataFrame

---

### `stock_hk_hot_rank_detail_em(symbol: str = '00700') -> pandas.DataFrame`

东方财富-个股人气榜-历史趋势
https://guba.eastmoney.com/rank/stock?code=HK_00700
:param symbol: 带市场表示的证券代码
:type symbol: str
:return: 个股的历史趋势
:rtype: pandas.DataFrame

---

### `stock_hk_hot_rank_detail_realtime_em(symbol: str = '00700') -> pandas.DataFrame`

东方财富-个股人气榜-实时变动
https://guba.eastmoney.com/rank/stock?code=HK_00700
:param symbol: 带市场表示的证券代码
:type symbol: str
:return: 实时变动
:rtype: pandas.DataFrame

---

### `stock_hk_hot_rank_em() -> pandas.DataFrame`

东方财富-个股人气榜-人气榜-港股市场
https://guba.eastmoney.com/rank/
:return: 人气榜
:rtype: pandas.DataFrame

---

### `stock_hk_hot_rank_latest_em(symbol: str = '00700') -> pandas.DataFrame`

东方财富-个股人气榜-最新排名
https://guba.eastmoney.com/rank/stock?code=HK_00700
:param symbol: 带市场表示的证券代码
:type symbol: str
:return: 最新排名
:rtype: pandas.DataFrame

---

### `stock_hk_indicator_eniu(symbol: str = 'hk01093', indicator: str = '市盈率') -> pandas.DataFrame`

亿牛网-港股指标
https://eniu.com/gu/hk01093/roe
:param symbol: 港股代码
:type symbol: str
:param indicator: 需要获取的指标, choice of {"港股", "市盈率", "市净率", "股息率", "ROE", "市值"}
:type indicator: str
:return: 指定 symbol 和 indicator 的数据
:rtype: pandas.DataFrame

---

### `stock_hk_profit_forecast_et(symbol: str = '09999', indicator: str = '盈利预测概览') -> pandas.DataFrame`

经济通-公司资料-盈利预测
https://www.etnet.com.hk/www/sc/stocks/realtime/quote_profit.php?code=9999
:param symbol: 股票代码
:type symbol: str
:param indicator: "盈利预测概览"; choice of {"评级总览", "去年度业绩表现", "综合盈利预测", "盈利预测概览"}
:type indicator: str
:return: 盈利预测
:rtype: pandas.DataFrame

---

### `stock_hk_security_profile_em(symbol: str = '03900') -> pandas.DataFrame`

东方财富-港股-证券资料
https://emweb.securities.eastmoney.com/PC_HKF10/pages/home/index.html?code=03900&type=web&color=w#/CompanyProfile
:param symbol: 股票代码
:type symbol: str
:return: 证券资料
:rtype: pandas.DataFrame

---

### `stock_hot_deal_xq(symbol: str = '最热门') -> pandas.DataFrame`

雪球-沪深股市-热度排行榜-分享交易排行榜
https://xueqiu.com/hq
:param symbol: choice of {"本周新增", "最热门"}
:type symbol: str
:return: 分享交易排行榜
:rtype: pandas.DataFrame

---

### `stock_hot_follow_xq(symbol: str = '最热门') -> pandas.DataFrame`

雪球-沪深股市-热度排行榜-关注排行榜
https://xueqiu.com/hq
:param symbol: choice of {"本周新增", "最热门"}
:type symbol: str
:return: 关注排行榜
:rtype: pandas.DataFrame

---

### `stock_hot_keyword_em(symbol: str = 'SZ000665') -> pandas.DataFrame`

东方财富-个股人气榜-热门关键词
https://guba.eastmoney.com/rank/stock?code=000665
:param symbol: 带市场表示的证券代码
:type symbol: str
:return: 热门关键词
:rtype: pandas.DataFrame

---

### `stock_hot_rank_detail_em(symbol: str = 'SZ000665') -> pandas.DataFrame`

东方财富-个股人气榜-历史趋势及粉丝特征
https://guba.eastmoney.com/rank/stock?code=000665
:param symbol: 带市场表示的证券代码
:type symbol: str
:return: 个股的历史趋势及粉丝特征
:rtype: pandas.DataFrame

---

### `stock_hot_rank_detail_realtime_em(symbol: str = 'SZ000665') -> pandas.DataFrame`

东方财富-个股人气榜-实时变动
https://guba.eastmoney.com/rank/stock?code=000665
:param symbol: 带市场表示的证券代码
:type symbol: str
:return: 实时变动
:rtype: pandas.DataFrame

---

### `stock_hot_rank_latest_em(symbol: str = 'SZ000665') -> pandas.DataFrame`

东方财富-个股人气榜-最新排名
https://guba.eastmoney.com/rank/stock?code=000665
:param symbol: 带市场表示的证券代码
:type symbol: str
:return: 最新排名
:rtype: pandas.DataFrame

---

### `stock_hot_rank_relate_em(symbol: str = 'SZ000665') -> pandas.DataFrame`

东方财富-个股人气榜-相关股票
https://guba.eastmoney.com/rank/stock?code=000665
:param symbol: 带市场表示的证券代码
:type symbol: str
:return: 相关股票
:rtype: pandas.DataFrame

---

### `stock_hot_search_baidu(symbol: str = 'A股', date: str = '20250616', time: str = '今日')`

百度股市通-热搜股票
https://gushitong.baidu.com/hotlist?mainTab=hotSearch&market=all
:param symbol: choice of {"全部", "A股", "港股", "美股"}
:type symbol: str
:param date: 日期
:type date: str
:param time: time="今日"；choice of {"今日", "1小时"}
:type time: str
:return: 热搜股票
:rtype: pandas.DataFrame

---

### `stock_hot_tweet_xq(symbol: str = '最热门') -> pandas.DataFrame`

雪球-沪深股市-热度排行榜-讨论排行榜
https://xueqiu.com/hq
:param symbol: choice of {"本周新增", "最热门"}
:type symbol: str
:return: 讨论排行榜
:rtype: pandas.DataFrame

---

### `stock_individual_basic_info_hk_xq(symbol: str = '02097', token: str = None, timeout: float = None) -> pandas.DataFrame`

雪球-个股-公司概况-公司简介
https://xueqiu.com/S/00700
:param symbol: 证券代码
:type symbol: str
:param token: 雪球财经的 token
:type token: str
:param timeout: 设置超时时间
:type timeout: float
:return: 公司简介
:rtype: pandas.DataFrame

---

### `stock_individual_basic_info_us_xq(symbol: str = 'NVDA', token: str = None, timeout: float = None) -> pandas.DataFrame`

雪球-个股-公司概况-公司简介
https://xueqiu.com/snowman/S/NVDA/detail#/GSJJ
:param symbol: 证券代码
:type symbol: str
:param token: 雪球财经的 token
:type token: str
:param timeout: 设置超时时间
:type timeout: float
:return: 公司简介
:rtype: pandas.DataFrame

---

### `stock_individual_basic_info_xq(symbol: str = 'SH601127', token: str = None, timeout: float = None) -> pandas.DataFrame`

雪球-个股-公司概况-公司简介
https://xueqiu.com/snowman/S/SH601127/detail#/GSJJ
:param symbol: 证券代码
:type symbol: str
:param token: 雪球财经的 token
:type token: str
:param timeout: 设置超时时间
:type timeout: float
:return: 公司简介
:rtype: pandas.DataFrame

---

### `stock_individual_info_em(symbol: str = '603777', timeout: float = None) -> pandas.DataFrame`

东方财富-个股-股票信息
https://quote.eastmoney.com/concept/sh603777.html?from=classic
:param symbol: 股票代码
:type symbol: str
:param timeout: choice of None or a positive float number
:type timeout: float
:return: 股票信息
:rtype: pandas.DataFrame

---

### `stock_individual_spot_xq(symbol: str = 'SH600000', token: str = None, timeout: float = None) -> pandas.DataFrame`

雪球-行情中心-个股
https://xueqiu.com/S/SH600000
:param symbol: 证券代码，可以是 A 股代码，A 股场内基金代码，A 股指数，美股代码, 美股指数
:type symbol: str
:param token: set xueqiu token
:type token: str
:param timeout: choice of None or a positive float number
:type timeout: float
:return: 证券最新行情
:rtype: pandas.DataFrame

---

### `stock_info_a_code_name() -> pandas.DataFrame`

沪深京 A 股列表
:return: 沪深京 A 股数据
:rtype: pandas.DataFrame

---

### `stock_info_bj_name_code() -> pandas.DataFrame`

北京证券交易所-股票列表
https://www.bse.cn/nq/listedcompany.html
:return: 股票列表
:rtype: pandas.DataFrame

---

### `stock_info_change_name(symbol: str = '000503') -> pandas.DataFrame`

新浪财经-股票曾用名
https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpInfo/stockid/300378.phtml
:param symbol: 股票代码
:type symbol: str
:return: 股票曾用名
:rtype: list

---

### `stock_info_cjzc_em() -> pandas.DataFrame`

东方财富-财经早餐
https://stock.eastmoney.com/a/czpnc.html
:return: 财经早餐
:rtype: pandas.DataFrame

---

### `stock_info_global_cls(symbol: str = '全部') -> pandas.DataFrame`

财联社-电报
https://www.cls.cn/telegraph
:param symbol: choice of {"全部", "重点"}
:type symbol: str
:return: 财联社-电报
:rtype: pandas.DataFrame

---

### `stock_info_global_em() -> pandas.DataFrame`

东方财富-全球财经快讯
https://kuaixun.eastmoney.com/7_24.html
:return: 全球财经快讯
:rtype: pandas.DataFrame

---

### `stock_info_global_futu() -> pandas.DataFrame`

富途牛牛-快讯
https://news.futunn.com/main/live
:return: 快讯
:rtype: pandas.DataFrame

---

### `stock_info_global_sina() -> pandas.DataFrame`

新浪财经-全球财经快讯
https://finance.sina.com.cn/7x24
:return: 全球财经快讯
:rtype: pandas.DataFrame

---

### `stock_info_global_ths() -> pandas.DataFrame`

同花顺财经-全球财经直播
https://news.10jqka.com.cn/realtimenews.html
:return: 全球财经直播
:rtype: pandas.DataFrame

---

### `stock_info_sh_delist(symbol: str = '全部') -> pandas.DataFrame`

上海证券交易所-终止上市公司
https://www.sse.com.cn/assortment/stock/list/delisting/
:param symbol: choice of {"全部", "沪市", "科创板"}
:type symbol: str
:return: 终止上市公司
:rtype: pandas.DataFrame

---

### `stock_info_sh_name_code(symbol: str = '主板A股') -> pandas.DataFrame`

上海证券交易所-股票列表
https://www.sse.com.cn/assortment/stock/list/share/
:param symbol: choice of {"主板A股": "1", "主板B股": "2", "科创板": "8"}
:type symbol: str
:return: 指定 indicator 的数据
:rtype: pandas.DataFrame

---

### `stock_info_sz_change_name(symbol: str = '全称变更') -> pandas.DataFrame`

深证证券交易所-市场数据-股票数据-名称变更
https://www.szse.cn/www/market/stock/changename/index.html
:param symbol: choice of {"全称变更": "tab1", "简称变更": "tab2"}
:type symbol: str
:return: 名称变更数据
:rtype: pandas.DataFrame

---

### `stock_info_sz_delist(symbol: str = '终止上市公司') -> pandas.DataFrame`

深证证券交易所-暂停上市公司-终止上市公司
https://www.szse.cn/market/stock/suspend/index.html
:param symbol: choice of {"暂停上市公司", "终止上市公司"}
:type symbol: str
:return: 暂停上市公司 or 终止上市公司 的数据
:rtype: pandas.DataFrame

---

### `stock_info_sz_name_code(symbol: str = 'A股列表') -> pandas.DataFrame`

深圳证券交易所-股票列表
https://www.szse.cn/market/product/stock/list/index.html
:param symbol: choice of {"A股列表", "B股列表", "CDR列表", "AB股列表"}
:type symbol: str
:return: 指定 indicator 的数据
:rtype: pandas.DataFrame

---

### `stock_ipo_benefit_ths() -> pandas.DataFrame`

同花顺-数据中心-新股数据-IPO受益股
https://data.10jqka.com.cn/ipo/syg/
:return: IPO受益股
:rtype: pandas.DataFrame

---

### `stock_ipo_declare_em() -> pandas.DataFrame`

东方财富网-数据中心-新股数据-首发申报企业信息
https://data.eastmoney.com/xg/xg/sbqy.html
:return: 首发申报企业信息
:rtype: pandas.DataFrame

---

### `stock_ipo_hk_ths() -> pandas.DataFrame`

同花顺-数据中心-新股申购与中签-港股
https://data.10jqka.com.cn/ipo/xgsgyzq/
:return: 港股新股申购与中签数据
:rtype: pandas.DataFrame

---

### `stock_ipo_info(stock: str = '600004') -> pandas.DataFrame`

新浪财经-发行与分配-新股发行
https://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_NewStock/stockid/600004.phtml
:param stock: 股票代码
:type stock: str
:return: 返回新股发行详情
:rtype: pandas.DataFrame

---

### `stock_ipo_review_em() -> pandas.DataFrame`

东方财富网-数据中心-新股申购-新股上会信息
https://data.eastmoney.com/xg/gh/default.html
:return: 新股上会信息
:rtype: pandas.DataFrame

---

### `stock_ipo_summary_cninfo(symbol: str = '600030') -> pandas.DataFrame`

巨潮资讯-个股-上市相关
https://webapi.cninfo.com.cn/#/company
:param symbol: 股票代码
:type symbol: str
:return: 上市相关
:rtype: pandas.DataFrame

---

### `stock_ipo_ths(symbol: str = '全部A股') -> pandas.DataFrame`

同花顺-数据中心-新股申购与中签
https://data.10jqka.com.cn/ipo/xgsgyzq/
:param symbol: choice of {"全部A股", "沪市主板", "深市主板", "创业板", "科创板", "京市主板"}
:type symbol: str
:return: 新股申购与中签数据
:rtype: pandas.DataFrame

---

### `stock_ipo_tutor_em() -> pandas.DataFrame`

东方财富网-数据中心-新股数据-IPO辅导信息
https://data.eastmoney.com/xg/ipo/fd.html
:return: IPO辅导信息
:rtype: pandas.DataFrame

---

### `stock_irm_ans_cninfo(symbol: str = '1513586704097333248') -> pandas.DataFrame`

互动易-回答
https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=1515236357817618432
:param symbol: 提问者编号; 通过 ak.stock_irm_cninfo() 来获取具体的提问者编号
:type symbol: str
:return: 回答
:rtype: str

---

### `stock_irm_cninfo(symbol: str = '002594') -> pandas.DataFrame`

互动易-提问
https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=1515236357817618432
:param symbol: 股票代码
:type symbol: str
:return: 提问
:rtype: str

---

### `stock_js_weibo_nlp_time() -> Dict`

https://datacenter.jin10.com/market
:return: 特定时间表示的字典
:rtype: dict

---

### `stock_js_weibo_report(time_period: str = 'CNHOUR12') -> pandas.DataFrame`

金十数据中心-实时监控-微博舆情报告
https://datacenter.jin10.com/market
:param time_period: {'CNHOUR2': '2小时', 'CNHOUR6': '6小时', 'CNHOUR12': '12小时', 'CNHOUR24': '1天', 'CNDAY7': '1周', 'CNDAY30': '1月'}
:type time_period: str
:return: 指定时间段的微博舆情报告
:rtype: pandas.DataFrame

---

### `stock_management_change_ths(symbol: str = '688981') -> pandas.DataFrame`

同花顺-公司大事-高管持股变动
https://basic.10jqka.com.cn/new/688981/event.html
:param symbol: 股票代码
:type symbol: str
:return: 同花顺-公司大事-高管持股变动
:rtype: pandas.DataFrame

---

### `stock_new_gh_cninfo() -> pandas.DataFrame`

巨潮资讯-数据中心-新股数据-新股过会
https://webapi.cninfo.com.cn/#/xinguList
:return: 新股过会
:rtype: pandas.DataFrame

---

### `stock_new_ipo_cninfo() -> pandas.DataFrame`

巨潮资讯-数据中心-新股数据-新股发行
https://webapi.cninfo.com.cn/#/xinguList
:return: 新股发行
:rtype: pandas.DataFrame

---

### `stock_news_em(symbol: str = '603777') -> pandas.DataFrame`

东方财富-个股新闻-最近 100 条新闻
https://so.eastmoney.com/news/s?keyword=603777
:param symbol: 股票代码
:type symbol: str
:return: 个股新闻
:rtype: pandas.DataFrame

---

### `stock_news_main_cx() -> pandas.DataFrame`

财新网-财新数据通
https://cxdata.caixin.com/pc/
:return: 特定时间表示的字典
:rtype: pandas.DataFrame

---

### `stock_notice_report(symbol: str = '全部', date: str = '20220511') -> pandas.DataFrame`

东方财富网-数据中心-公告大全-沪深京 A 股公告
https://data.eastmoney.com/notices/hsa/5.html
:param symbol: 报告类型; choice of {"全部", "重大事项", "财务报告", "融资公告", "风险提示", "资产重组", "信息变更", "持股变动"}
:type symbol: str
:param date: 制定日期
:type date: str
:return: 沪深京 A 股公告
:rtype: pandas.DataFrame

---

### `stock_pg_em() -> pandas.DataFrame`

东方财富网-数据中心-新股数据-配股
https://data.eastmoney.com/xg/pg/
:return: 配股
:rtype: pandas.DataFrame

---

### `stock_price_js(symbol: str = 'us') -> pandas.DataFrame`

美股目标价 or 港股目标价
https://www.ushknews.com/report.html
:param symbol: choice of {"us", "hk"}
:type symbol: str
:return: 美股目标价 or 港股目标价
:rtype: pandas.DataFrame

---

### `stock_profile_cninfo(symbol: str = '600030') -> pandas.DataFrame`

巨潮资讯-个股-公司概况
https://webapi.cninfo.com.cn/#/company
:param symbol: 股票代码
:type symbol: str
:return: 公司概况
:rtype: pandas.DataFrame
:raise: Exception，如果服务器返回的数据无法被解析

---

### `stock_qbzf_em() -> pandas.DataFrame`

东方财富网-数据中心-新股数据-增发-全部增发
https://data.eastmoney.com/other/gkzf.html
:return: 全部增发
:rtype: pandas.DataFrame

---

### `stock_qsjy_em(date: str = '20200731') -> pandas.DataFrame`

东方财富网-数据中心-特色数据-券商业绩月报
http://data.eastmoney.com/other/qsjy.html
:param date: 数据月份，从 2010-06-01 开始, e.g., 需要 2011 年 7 月, 则输入 2011-07-01
:type date: str
:return: 券商业绩月报
:rtype: pandas.DataFrame

---

### `stock_rank_cxd_ths(symbol: str = '创月新低') -> pandas.DataFrame`

同花顺-数据中心-技术选股-创新低
https://data.10jqka.com.cn/rank/cxd/
:param symbol: choice of {"创月新低", "半年新低", "一年新低", "历史新低"}
:type symbol: str
:return: 创新低数据
:rtype: pandas.DataFrame

---

### `stock_rank_cxfl_ths() -> pandas.DataFrame`

同花顺-数据中心-技术选股-持续放量
https://data.10jqka.com.cn/rank/cxfl/
:return: 持续放量
:rtype: pandas.DataFrame

---

### `stock_rank_cxg_ths(symbol: str = '创月新高') -> pandas.DataFrame`

同花顺-数据中心-技术选股-创新高
https://data.10jqka.com.cn/rank/cxg/
:param symbol: choice of {"创月新高", "半年新高", "一年新高", "历史新高"}
:type symbol: str
:return: 创新高数据
:rtype: pandas.DataFrame

---

### `stock_rank_cxsl_ths() -> pandas.DataFrame`

同花顺-数据中心-技术选股-持续缩量
https://data.10jqka.com.cn/rank/cxsl/
:return: 持续缩量
:rtype: pandas.DataFrame

---

### `stock_rank_forecast_cninfo(date: str = '20230817') -> pandas.DataFrame`

巨潮资讯-数据中心-评级预测-投资评级
https://webapi.cninfo.com.cn/#/thematicStatistics?name=%E6%8A%95%E8%B5%84%E8%AF%84%E7%BA%A7
:param date: 查询日期
:type date: str
:return: 投资评级
:rtype: pandas.DataFrame

---

### `stock_rank_ljqd_ths() -> pandas.DataFrame`

同花顺-数据中心-技术选股-量价齐跌
http://data.10jqka.com.cn/rank/ljqd/
:return: 量价齐跌
:rtype: pandas.DataFrame

---

### `stock_rank_ljqs_ths() -> pandas.DataFrame`

同花顺-数据中心-技术选股-量价齐升
http://data.10jqka.com.cn/rank/ljqs/
:return: 量价齐升
:rtype: pandas.DataFrame

---

### `stock_rank_lxsz_ths() -> pandas.DataFrame`

同花顺-数据中心-技术选股-连续上涨
https://data.10jqka.com.cn/rank/lxsz/
:return: 连续上涨
:rtype: pandas.DataFrame

---

### `stock_rank_lxxd_ths() -> pandas.DataFrame`

同花顺-数据中心-技术选股-连续下跌
https://data.10jqka.com.cn/rank/lxxd/
:return: 连续下跌
:rtype: pandas.DataFrame

---

### `stock_rank_xstp_ths(symbol: str = '500日均线') -> pandas.DataFrame`

同花顺-数据中心-技术选股-向上突破
https://data.10jqka.com.cn/rank/xstp/
:param symbol: choice of {"5日均线", "10日均线", "20日均线", "30日均线", "60日均线", "90日均线", "250日均线", "500日均线"}
:type symbol: str
:return: 向上突破
:rtype: pandas.DataFrame

---

### `stock_rank_xxtp_ths(symbol: str = '500日均线') -> pandas.DataFrame`

同花顺-数据中心-技术选股-向下突破
https://data.10jqka.com.cn/rank/xxtp/
:param symbol: choice of {"5日均线", "10日均线", "20日均线", "30日均线", "60日均线", "90日均线", "250日均线", "500日均线"}
:type symbol: str
:return: 向下突破
:rtype: pandas.DataFrame

---

### `stock_rank_xzjp_ths() -> pandas.DataFrame`

同花顺-数据中心-技术选股-险资举牌
https://data.10jqka.com.cn/financial/xzjp/
:return: 险资举牌
:rtype: pandas.DataFrame

---

### `stock_register_all_em() -> pandas.DataFrame`

东方财富网-数据中心-新股数据-IPO审核信息-全部
https://data.eastmoney.com/xg/ipo/
:return: 科创板注册制审核结果
:rtype: pandas.DataFrame

---

### `stock_register_bj() -> pandas.DataFrame`

东方财富网-数据中心-新股数据-IPO审核信息-北交所
https://data.eastmoney.com/xg/ipo/
:return: 北交所
:rtype: pandas.DataFrame

---

### `stock_register_cyb() -> pandas.DataFrame`

东方财富网-数据中心-新股数据-IPO审核信息-创业板
https://data.eastmoney.com/xg/ipo/
:return: 创业板注册制审核结果
:rtype: pandas.DataFrame

---

### `stock_register_db() -> pandas.DataFrame`

东方财富网-数据中心-新股数据-IPO审核信息-达标企业
https://data.eastmoney.com/xg/cyb/
:return: 达标企业
:rtype: pandas.DataFrame

---

### `stock_register_kcb() -> pandas.DataFrame`

东方财富网-数据中心-新股数据-IPO审核信息-科创板
https://data.eastmoney.com/xg/ipo/
:return: 科创板注册制审核结果
:rtype: pandas.DataFrame

---

### `stock_register_sh() -> pandas.DataFrame`

东方财富网-数据中心-新股数据-IPO审核信息-上海主板
https://data.eastmoney.com/xg/ipo/
:return: 上海主板
:rtype: pandas.DataFrame

---

### `stock_register_sz() -> pandas.DataFrame`

东方财富网-数据中心-新股数据-IPO审核信息-深圳主板
https://data.eastmoney.com/xg/ipo/
:return: 深圳主板
:rtype: pandas.DataFrame

---

### `stock_report_disclosure(market: str = '沪深京', period: str = '2021年报') -> pandas.DataFrame`

巨潮资讯-首页-数据-预约披露
http://www.cninfo.com.cn/new/commonUrl?url=data/yypl
:param market: choice of {"沪深京": "szsh", "深市": "sz", "深主板": "szmb", "中小板": "szsme",
"创业板": "szcn", "沪市": "sh", "沪主板": "shmb", "科创板": "shkcp"}
:type market: str
:param period: 最近四期的财报
:type period: str
:return: 指定 market 和 period 的数据
:rtype: pandas.DataFrame

---

### `stock_repurchase_em() -> pandas.DataFrame`

东方财富网-数据中心-股票回购-股票回购数据
https://data.eastmoney.com/gphg/hglist.html
:return: 股票回购数据
:rtype: pandas.DataFrame

---

### `stock_research_report_em(symbol: str = '000001') -> pandas.DataFrame`

东方财富网-数据中心-研究报告-个股研报
https://data.eastmoney.com/report/stock.jshtml
:param symbol: 个股代码
:type symbol: str
:return: 个股研报
:rtype: pandas.DataFrame

---

### `stock_restricted_release_detail_em(start_date: str = '20221202', end_date: str = '20241202') -> pandas.DataFrame`

东方财富网-数据中心-限售股解禁-解禁详情一览
https://data.eastmoney.com/dxf/detail.html
:param start_date: 开始时间
:type start_date: str
:param end_date: 结束时间
:type end_date: str
:return: 解禁详情一览
:rtype: pandas.DataFrame

---

### `stock_restricted_release_queue_em(symbol: str = '600000') -> pandas.DataFrame`

东方财富网-数据中心-个股限售解禁-解禁批次
https://data.eastmoney.com/dxf/q/600000.html
:param symbol: 股票代码
:type symbol: str
:return: 个股限售解禁
:rtype: pandas.DataFrame

---

### `stock_restricted_release_queue_sina(symbol: str = '600000') -> pandas.DataFrame`

新浪财经-发行分配-限售解禁
https://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/xsjj/index.phtml?symbol=sh600000
:param symbol: 股票代码
:type symbol: str
:return: 返回限售解禁数据
:rtype: pandas.DataFrame

---

### `stock_restricted_release_stockholder_em(symbol: str = '600000', date: str = '20200904') -> pandas.DataFrame`

东方财富网-数据中心-个股限售解禁-解禁股东
https://data.eastmoney.com/dxf/q/600000.html
:param symbol: 股票代码
:type symbol: str
:param date: 日期; 通过 ak.stock_restricted_release_queue_em(symbol="600000") 获取
:type date: str
:return: 个股限售解禁
:rtype: pandas.DataFrame

---

### `stock_restricted_release_summary_em(symbol: str = '全部股票', start_date: str = '20221101', end_date: str = '20221209') -> pandas.DataFrame`

东方财富网-数据中心-特色数据-限售股解禁
https://data.eastmoney.com/dxf/marketStatistics.html?type=day&startdate=2022-11-08&enddate=2022-12-19
:param symbol: 标的市场; choice of {"全部股票", "沪市A股", "科创板", "深市A股", "创业板", "京市A股"}
:type symbol: str
:param start_date: 开始时间
:type start_date: str
:param end_date: 结束时间
:type end_date: str
:return: 限售股解禁
:rtype: pandas.DataFrame

---

### `stock_sgt_reference_exchange_rate_sse() -> pandas.DataFrame`

沪港通-港股通信息披露-参考汇率
https://www.sse.com.cn/services/hkexsc/disclo/ratios/
:return: 参考汇率
:rtype: pandas.DataFrame

---

### `stock_sgt_reference_exchange_rate_szse() -> pandas.DataFrame`

深港通-港股通业务信息-参考汇率
https://www.szse.cn/szhk/hkbussiness/exchangerate/index.html
:return: 参考汇率
:rtype: pandas.DataFrame

---

### `stock_sgt_settlement_exchange_rate_sse() -> pandas.DataFrame`

沪港通-港股通信息披露-结算汇兑
https://www.sse.com.cn/services/hkexsc/disclo/ratios/
:return: 结算汇兑比率
:rtype: pandas.DataFrame

---

### `stock_sgt_settlement_exchange_rate_szse() -> pandas.DataFrame`

深港通-港股通业务信息-结算汇率
https://www.szse.cn/szhk/hkbussiness/exchangerate/index.html
:return: 结算汇率
:rtype: pandas.DataFrame

---

### `stock_share_change_cninfo(symbol: str = '002594', start_date: str = '20091227', end_date: str = '20241021') -> pandas.DataFrame`

巨潮资讯-股本股东-公司股本变动
https://webapi.cninfo.com.cn/#/apiDoc
查询 p_stock2215 接口
:param symbol: 股票代码
:type symbol: str
:param start_date: 开始变动日期
:type start_date: str
:param end_date: 结束变动日期
:type end_date: str
:return: 公司股本变动
:rtype: pandas.DataFrame

---

### `stock_share_hold_change_bse(symbol: str = '430489') -> pandas.DataFrame`

北京证券交易所-信息披露-监管信息-董监高及相关人员持股变动
https://www.bse.cn/disclosure/djg_sharehold_change.html
:param symbol: choice of {"全部", "具体股票代码"}
:type symbol: str
:return: 董监高及相关人员持股变动
:rtype: pandas.DataFrame

---

### `stock_share_hold_change_sse(symbol: str = '600000') -> pandas.DataFrame`

上海证券交易所-披露-监管信息公开-公司监管-董董监高人员股份变动
https://www.sse.com.cn/disclosure/credibility/supervision/change/
:param symbol: choice of {"全部", "具体股票代码"}
:type symbol: str
:return: 董监高人员股份变动
:rtype: pandas.DataFrame

---

### `stock_share_hold_change_szse(symbol: str = '全部') -> pandas.DataFrame`

深圳证券交易所-信息披露-监管信息公开-董监高人员股份变动
https://www.szse.cn/disclosure/supervision/change/index.html
:param symbol: choice of {"全部", "具体股票代码"}
:type symbol: str
:return: 董监高人员股份变动
:rtype: pandas.DataFrame

---

### `stock_shareholder_change_ths(symbol: str = '688981') -> pandas.DataFrame`

同花顺-公司大事-股东持股变动
https://basic.10jqka.com.cn/new/688981/event.html
:param symbol: 股票代码
:type symbol: str
:return: 同花顺-公司大事-股东持股变动
:rtype: pandas.DataFrame

---

### `stock_sns_sseinfo(symbol: str = '603119') -> pandas.DataFrame`

上证e互动-提问与回答
https://sns.sseinfo.com/company.do?uid=65
:param symbol: 股票代码
:type symbol: str
:return: 提问与回答
:rtype: str

---

### `stock_sse_deal_daily(date: str = '20241216') -> pandas.DataFrame`

上海证券交易所-数据-股票数据-成交概况-股票成交概况-每日股票情况
https://www.sse.com.cn/market/stockdata/overview/day/
:param date: 交易日
:type date: str
:return: 每日股票情况
:rtype: pandas.DataFrame

---

### `stock_sse_summary() -> pandas.DataFrame`

上海证券交易所-总貌
https://www.sse.com.cn/market/stockdata/statistic/
:return: 上海证券交易所-总貌
:rtype: pandas.DataFrame

---

### `stock_sy_hy_em(date: str = '20240930') -> pandas.DataFrame`

东方财富网-数据中心-特色数据-商誉-行业商誉
https://data.eastmoney.com/sy/hylist.html
:param date: 参考网站指定的数据日期
:type date: str
:return: 个股商誉明细
:rtype: pandas.DataFrame

---

### `stock_sy_jz_em(date: str = '20240630') -> pandas.DataFrame`

东方财富网-数据中心-特色数据-商誉-个股商誉减值明细
https://data.eastmoney.com/sy/jzlist.html
:param date: 参考网站指定的数据日期
:type date: str
:return: 个股商誉减值明细
:rtype: pandas.DataFrame

---

### `stock_sy_yq_em(date: str = '20240630') -> pandas.DataFrame`

东方财富网-数据中心-特色数据-商誉-商誉减值预期明细
https://data.eastmoney.com/sy/yqlist.html
:param date: 参考网站指定的数据日期
:type date: str
:return: 商誉减值预期明细
:rtype: pandas.DataFrame

---

### `stock_szse_area_summary(date: str = '202203') -> pandas.DataFrame`

深证证券交易所-总貌-地区交易排序
https://www.szse.cn/market/overview/index.html
:param date: 最近结束交易日
:type date: str
:return: 地区交易排序
:rtype: pandas.DataFrame

---

### `stock_szse_sector_summary(symbol: str = '当月', date: str = '202501') -> pandas.DataFrame`

深圳证券交易所-统计资料-股票行业成交数据
https://docs.static.szse.cn/www/market/periodical/month/W020220511355248518608.html
:param symbol: choice of {"当月", "当年"}
:type symbol: str
:param date: 交易年月
:type date: str
:return: 股票行业成交数据
:rtype: pandas.DataFrame

---

### `stock_szse_summary(date: str = '20240830') -> pandas.DataFrame`

深证证券交易所-总貌-证券类别统计
https://www.szse.cn/market/overview/index.html
:param date: 最近结束交易日
:type date: str
:return: 证券类别统计
:rtype: pandas.DataFrame

---

### `stock_tfp_em(date: str = '20240426') -> pandas.DataFrame`

东方财富网-数据中心-特色数据-停复牌信息
https://data.eastmoney.com/tfpxx/
:param date: 查询参数 "20240426"
:type date: str
:return: 停复牌信息表
:rtype: pandas.DataFrame

---

### `stock_xgsglb_em(symbol: str = '全部股票') -> pandas.DataFrame`

新股申购与中签查询
https://data.eastmoney.com/xg/xg/default_2.html
:param symbol: choice of {"全部股票", "沪市主板", "科创板", "深市主板", "创业板", "北交所"}
:type symbol: str
:return: 新股申购与中签数据
:rtype: pandas.DataFrame

---

### `stock_xgsr_ths() -> pandas.DataFrame`

同花顺-数据中心-新股数据-新股上市首日
https://data.10jqka.com.cn/ipo/xgsr/
:return: 新股上市首日
:rtype: pandas.DataFrame

---

### `stock_yysj_em(symbol: str = '沪深A股', date: str = '20200331') -> pandas.DataFrame`

东方财富-数据中心-年报季报-预约披露时间
https://data.eastmoney.com/bbsj/202003/yysj.html
:param symbol: choice of {'沪深A股', '沪市A股', '科创板', '深市A股', '创业板', '京市A股', 'ST板'}
:type symbol: str
:param date: "20190331", "20190630", "20190930", "20191231"; 从 20081231 开始
:type date: str
:return: 指定时间的上市公司预约披露时间数据
:rtype: pandas.DataFrame

---

### `stock_yzxdr_em(date: str = '20240930') -> pandas.DataFrame`

东方财富网-数据中心-特色数据-一致行动人
https://data.eastmoney.com/yzxdr/
:param date: 每年的季度末时间点
:type date: str
:return: 一致行动人
:rtype: pandas.DataFrame

---

### `stock_zdhtmx_em(start_date: str = '20200819', end_date: str = '20230819') -> pandas.DataFrame`

东方财富网-数据中心-重大合同-重大合同明细
https://data.eastmoney.com/zdht/mx.html
:param start_date: 开始日期, eg 20200819
:type start_date: str
:param end_date: 结束日期, eg 20230819
:type end_date: str
:return: 股东大会
:rtype: pandas.DataFrame

---

### `stock_zh_a_disclosure_relation_cninfo(symbol: str = '000001', market: str = '沪深京', start_date: str = '20230618', end_date: str = '20231219') -> pandas.DataFrame`

巨潮资讯-首页-数据-预约披露调研
http://www.cninfo.com.cn/new/commonUrl?url=data/yypl
:param symbol: 股票代码
:type symbol: str
:param market: choice of {"沪深京", "港股", "三板", "基金", "债券", "监管", "预披露"}
:type market: str
:param start_date: 开始时间
:type start_date: str
:param end_date: 开始时间
:type end_date: str
:return: 指定 symbol 的数据
:rtype: pandas.DataFrame

---

### `stock_zh_a_disclosure_report_cninfo(symbol: str = '000001', market: str = '沪深京', keyword: str = '', category: str = '', start_date: str = '20230618', end_date: str = '20231219') -> pandas.DataFrame`

巨潮资讯-首页-公告查询-信息披露公告
http://www.cninfo.com.cn/new/commonUrl/pageOfSearch?url=disclosure/list/search
:param symbol: 股票代码
:type symbol: str
:param market: choice of {"沪深京", "港股", "三板", "基金", "债券", "监管", "预披露"}
:type market: str
:param keyword: 关键词
:type keyword: str
:param category: choice of {'年报', '半年报', '一季报', '三季报', '业绩预告', '权益分派',
'董事会', '监事会', '股东大会', '日常经营', '公司治理', '中介报告',
 '首发', '增发', '股权激励', '配股', '解禁', '公司债', '可转债', '其他融资',
 '股权变动', '补充更正', '澄清致歉', '风险提示', '特别处理和退市', '退市整理期'}
:type category: str
:param start_date: 开始时间
:type start_date: str
:param end_date: 开始时间
:type end_date: str
:return: 指定 symbol 的数据
:rtype: pandas.DataFrame

---

### `stock_zh_a_gbjg_em(symbol: str = '603392.SH') -> pandas.DataFrame`

东方财富-A股数据-股本结构
https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html#/gbjg
:param symbol: 股票代码
:type symbol: str
:return: 股本结构
:rtype: pandas.DataFrame

---

### `stock_zh_a_tick_tx_js(symbol: str = 'sz000001') -> pandas.DataFrame`

腾讯财经-历史分笔数据
https://gu.qq.com/sz300494/gp/detail
:param symbol: 股票代码
:type symbol: str
:return: 历史分笔数据
:rtype: pandas.DataFrame

---

### `stock_zh_index_daily(symbol: str = 'sh000922') -> pandas.DataFrame`

新浪财经-指数-历史行情数据, 大量抓取容易封 IP
https://finance.sina.com.cn/realstock/company/sh000909/nc.shtml
:param symbol: sz399998, 指定指数代码
:type symbol: str
:return: 历史行情数据
:rtype: pandas.DataFrame

---

### `stock_zh_index_daily_em(symbol: str = 'csi931151', start_date: str = '19900101', end_date: str = '20500101') -> pandas.DataFrame`

东方财富网-股票指数数据
https://quote.eastmoney.com/center/hszs.html
:param symbol: 带市场标识的指数代码; sz: 深交所, sh: 上交所, csi: 中信指数 + id(000905)
:type symbol: str
:param start_date: 开始时间
:type start_date: str
:param end_date: 结束时间
:type end_date: str
:return: 指数数据
:rtype: pandas.DataFrame

---

### `stock_zh_index_daily_tx(symbol: str = 'sz980017') -> pandas.DataFrame`

腾讯证券-日频-股票或者指数历史数据
作为 ak.stock_zh_index_daily() 的补充, 因为在新浪中有部分指数数据缺失
注意都是: 前复权, 不同网站复权方式不同, 不可混用数据
https://gu.qq.com/sh000919/zs
:param symbol: 带市场标识的股票或者指数代码
:type symbol: str
:return: 前复权的股票和指数数据
:rtype: pandas.DataFrame

---

### `stock_zh_index_hist_csindex(symbol: str = '000928', start_date: str = '20180526', end_date: str = '20240604') -> pandas.DataFrame`

中证指数-具体指数-历史行情数据
P.S. 只有收盘价，正常情况下不应使用该接口，除非指数只有中证网站有
https://www.csindex.com.cn/zh-CN/indices/index-detail/H30374#/indices/family/detail?indexCode=H30374
:param symbol: 指数代码; e.g., H30374
:type symbol: str
:param start_date: 开始日期
:type start_date: str
:param end_date: 结束日期
:type end_date: str
:return: 包含日期和收盘价的指数数据
:rtype: pandas.DataFrame

---

### `stock_zh_index_spot_em(symbol: str = '上证系列指数') -> pandas.DataFrame`

东方财富网-行情中心-沪深京指数
https://quote.eastmoney.com/center/gridlist.html#index_sz
:param symbol: "上证系列指数"; choice of {"沪深重要指数", "上证系列指数", "深证系列指数", "指数成份", "中证系列指数"}
:type symbol: str
:return: 指数的实时行情数据
:rtype: pandas.DataFrame

---

### `stock_zh_index_spot_sina() -> pandas.DataFrame`

新浪财经-行情中心首页-A股-分类-所有指数
大量采集会被目标网站服务器封禁 IP, 如果被封禁 IP, 请 10 分钟后再试
https://vip.stock.finance.sina.com.cn/mkt/#hs_s
:return: 所有指数的实时行情数据
:rtype: pandas.DataFrame

---

### `stock_zh_index_value_csindex(symbol: str = 'H30374') -> pandas.DataFrame`

中证指数-指数估值数据
https://www.csindex.com.cn/zh-CN/indices/index-detail/H30374#/indices/family/detail?indexCode=H30374
:param symbol: 指数代码; e.g., H30374
:type symbol: str
:return: 指数估值数据
:rtype: pandas.DataFrame

---

### `stock_zh_kcb_report_em(from_page: int = 1, to_page: int = 100) -> pandas.DataFrame`

科创板报告内容
https://data.eastmoney.com/notices/kcb.html
:param from_page: 开始获取的页码
:type from_page: int
:param to_page: 结束获取的页码
:type to_page: int
:return: 科创板报告内容
:rtype: pandas.DataFrame

---

### `stock_zh_vote_baidu(symbol: str = '000001', indicator: str = '指数') -> pandas.DataFrame`

百度股市通- A 股或指数-股评-投票
https://gushitong.baidu.com/index/ab-000001
:param symbol: 股票代码
:type symbol: str
:param indicator: choice of {"指数", "股票"}
:type indicator: str
:return: 投票数据
:rtype: pandas.DataFrame

---

### `stock_zygc_em(symbol: str = 'SH688041') -> pandas.DataFrame`

东方财富网-个股-主营构成
https://emweb.securities.eastmoney.com/PC_HSF10/BusinessAnalysis/Index?type=web&code=SH688041#
:param symbol: 带市场标识的股票代码
:type symbol: str
:return: 主营构成
:rtype: pandas.DataFrame

---

### `stock_zyjs_ths(symbol: str = '000066') -> pandas.DataFrame`

同花顺-主营介绍
https://basic.10jqka.com.cn/new/000066/operate.html
:param symbol: 股票代码
:type symbol: str
:return: 主营介绍
:rtype: pandas.DataFrame

---

