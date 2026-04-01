# Option 域接口详情

> 共 47 个接口，覆盖上交所/深交所股票期权及商品期权 合约/行情/波动率/风险指标等。

## 接口列表

### `option_cffex_hs300_daily_sina(symbol: str = 'io2202P4350') -> pandas.DataFrame`

新浪财经-中金所-沪深300指数-指定合约-日频行情
:param symbol: 具体合约代码(包括看涨和看跌标识), 可以通过 ak.option_cffex_hs300_spot_sina 中的 call-标识 获取
:type symbol: str
:return: 日频率数据
:rtype: pandas.DataFrame

---

### `option_cffex_hs300_list_sina() -> Dict[str, List[str]]`

新浪财经-中金所-沪深 300 指数-所有合约, 返回的第一个合约为主力合约
目前新浪财经-中金所有沪深 300 指数和中证 1000 指数
:return: 中金所-沪深300指数-所有合约
:rtype: dict

---

### `option_cffex_hs300_spot_sina(symbol: str = 'io2204') -> pandas.DataFrame`

中金所-沪深 300 指数-指定合约-实时行情
https://stock.finance.sina.com.cn/futures/view/optionsCffexDP.php
:param symbol: 合约代码; 用 option_cffex_hs300_list_sina 函数查看
:type symbol: str
:return: 中金所-沪深300指数-指定合约-看涨看跌实时行情
:rtype: pandas.DataFrame

---

### `option_cffex_sz50_daily_sina(symbol: str = 'ho2303P2350') -> pandas.DataFrame`

新浪财经-中金所-上证 50 指数-指定合约-日频行情
:param symbol: 具体合约代码(包括看涨和看跌标识), 可以通过 ak.option_cffex_sz50_spot_sina 中的 call-标识 获取
:type symbol: str
:return: 日频率数据
:rtype: pandas.DataFrame

---

### `option_cffex_sz50_list_sina() -> Dict[str, List[str]]`

新浪财经-中金所-上证 50 指数-所有合约, 返回的第一个合约为主力合约
目前新浪财经-中金所有上证 50 指数，沪深 300 指数和中证 1000 指数
:return: 中金所-上证 50 指数-所有合约
:rtype: dict

---

### `option_cffex_sz50_spot_sina(symbol: str = 'ho2303') -> pandas.DataFrame`

中金所-上证 50 指数-指定合约-实时行情
https://stock.finance.sina.com.cn/futures/view/optionsCffexDP.php/ho/cffex
:param symbol: 合约代码; 用 ak.option_cffex_sz300_list_sina() 函数查看
:type symbol: str
:return: 中金所-上证 50 指数-指定合约-看涨看跌实时行情
:rtype: pandas.DataFrame

---

### `option_cffex_zz1000_daily_sina(symbol: str = 'mo2208P6200') -> pandas.DataFrame`

新浪财经-中金所-中证 1000 指数-指定合约-日频行情
:param symbol: 具体合约代码(包括看涨和看跌标识), 可以通过 ak.option_cffex_zz1000_spot_sina 中的 call-标识 获取
:type symbol: str
:return: 日频率数据
:rtype: pandas.DataFrame

---

### `option_cffex_zz1000_list_sina() -> Dict[str, List[str]]`

新浪财经-中金所-中证 1000 指数-所有合约, 返回的第一个合约为主力合约
目前新浪财经-中金所有沪深 300 指数和中证 1000 指数
:return: 中金所-中证 1000 指数-所有合约
:rtype: dict

---

### `option_cffex_zz1000_spot_sina(symbol: str = 'mo2208') -> pandas.DataFrame`

中金所-中证 1000 指数-指定合约-实时行情
https://stock.finance.sina.com.cn/futures/view/optionsCffexDP.php
:param symbol: 合约代码; 用 option_cffex_zz1000_list_sina 函数查看
:type symbol: str
:return: 中金所-中证 1000 指数-指定合约-看涨看跌实时行情
:rtype: pandas.DataFrame

---

### `option_comm_info(symbol: str = '工业硅期权') -> pandas.DataFrame`

九期网-商品期权手续费
https://www.9qihuo.com/qiquanshouxufei
:param symbol: choice of {"所有", "上海期货交易所", "大连商品交易所", "郑州商品交易所", "上海国际能源交易中心", "广州期货交易所"}
:type symbol: str
:return: 期权手续费
:rtype: pandas.DataFrame

---

### `option_comm_symbol() -> pandas.DataFrame`

---

### `option_commodity_contract_sina(symbol: str = '玉米期权') -> pandas.DataFrame`

当前可以查询的期权品种的合约日期
https://stock.finance.sina.com.cn/futures/view/optionsDP.php
:param symbol: choice of {"豆粕期权", "玉米期权", "铁矿石期权", "棉花期权", "白糖期权", "PTA期权", "甲醇期权", "橡胶期权", "沪铜期权", "黄金期权", "菜籽粕期权", "液化石油气期权", "动力煤期权", "菜籽油期权", "花生期权"}
:type symbol: str
:return: e.g., {'黄金期权': ['au2012', 'au2008', 'au2010', 'au2104', 'au2102', 'au2106', 'au2108']}
:rtype: dict

---

### `option_commodity_contract_table_sina(symbol: str = '黄金期权', contract: str = 'au2204') -> pandas.DataFrame`

当前所有期权合约, 包括看涨期权合约和看跌期权合约
https://stock.finance.sina.com.cn/futures/view/optionsDP.php
:param symbol: choice of {"豆粕期权", "玉米期权", "铁矿石期权", "棉花期权", "白糖期权", "PTA期权", "甲醇期权", "橡胶期权", "沪铜期权", "黄金期权", "菜籽粕期权", "液化石油气期权", "动力煤期权", "菜籽油期权", "花生期权"}
:type symbol: str
:param contract: e.g., 'au2012'
:type contract: str
:return: 合约实时行情
:rtype: pandas.DataFrame

---

### `option_commodity_hist_sina(symbol: str = 'au2012C392') -> pandas.DataFrame`

合约历史行情-日频
https://stock.finance.sina.com.cn/futures/view/optionsDP.php
:param symbol: return of option_sina_option_commodity_contract_list(symbol="黄金期权", contract="au2012"), 看涨期权合约 filed
:type symbol: str
:return: 合约历史行情-日频
:rtype: pandas.DataFrame

---

### `option_contract_info_ctp() -> pandas.DataFrame`

openctp-合约信息接口-期权合约
http://openctp.cn/instruments.html
:return: 期权合约信息
:rtype: pandas.DataFrame

---

### `option_current_day_sse() -> pandas.DataFrame`

上海证券交易所-产品-股票期权-信息披露-当日合约
http://www.sse.com.cn/assortment/options/disclo/preinfo/
:return: 上交所期权当日合约
:rtype: pandas.DataFrame

---

### `option_current_day_szse() -> pandas.DataFrame`

深圳证券交易所-期权子网-行情数据-当日合约
https://www.sse.org.cn/option/quotation/contract/daycontract/index.html
:return: 深圳期权当日合约
:rtype: pandas.DataFrame

---

### `option_current_em() -> pandas.DataFrame`

东方财富网-行情中心-期权市场
https://quote.eastmoney.com/center/qqsc.html
:return: 期权价格
:rtype: pandas.DataFrame

---

### `option_daily_stats_sse(date: str = '20240626') -> pandas.DataFrame`

上海证券交易所-产品-股票期权-每日统计
https://www.sse.com.cn/assortment/options/date/
:param date: 交易日
:type date: str
:return: 每日统计
:rtype: pandas.DataFrame

---

### `option_daily_stats_szse(date: str = '20240626') -> pandas.DataFrame`

深圳证券交易所-市场数据-期权数据-日度概况
https://investor.szse.cn/market/option/day/index.html
:param date: 交易日
:type date: str
:return: 每日统计
:rtype: pandas.DataFrame

---

### `option_finance_board(symbol: str = '嘉实沪深300ETF期权', end_month: str = '2306') -> pandas.DataFrame`

期权当前交易日的行情数据
主要为三个: 华夏上证50ETF期权, 华泰柏瑞沪深300ETF期权, 嘉实沪深300ETF期权,
沪深300股指期权, 中证1000股指期权, 上证50股指期权, 华夏科创50ETF期权, 易方达科创50ETF期权
http://www.sse.com.cn/assortment/options/price/
http://www.szse.cn/market/product/option/index.html
http://www.cffex.com.cn/hs300gzqq/
http://www.cffex.com.cn/zz1000gzqq/
:param symbol: choice of {"华夏上证50ETF期权", "华泰柏瑞沪深300ETF期权", "南方中证500ETF期权",
"华夏科创50ETF期权", "易方达科创50ETF期权", "嘉实沪深300ETF期权", "沪深300股指期权", "中证1000股指期权", "上证50股指期权"}
:type symbol: str
:param end_month: 2003; 2020 年 3 月到期的期权
:type end_month: str
:return: 当日行情
:rtype: pandas.DataFrame

---

### `option_finance_minute_sina(symbol: str = '10002530') -> pandas.DataFrame`

指定期权的分钟频率数据
https://stock.finance.sina.com.cn/option/quotes.html
:param symbol: 期权代码
:type symbol: str
:return: 指定期权的分钟频率数据
:rtype: pandas.DataFrame

---

### `option_finance_sse_underlying(symbol: str = '华夏科创50ETF期权') -> pandas.DataFrame`

期权标的当日行情
http://www.sse.com.cn/assortment/options/price/
:param symbol: choice of {"华夏上证50ETF期权", "华泰柏瑞沪深300ETF期权", "南方中证500ETF期权", "华夏科创50ETF期权", "易方达科创50ETF期权"}
:type symbol: str
:return: 期权标的当日行情
:rtype: pandas.DataFrame

---

### `option_hist_czce(symbol: str = '白糖期权', trade_date: str = '20191017') -> pandas.DataFrame`

郑州商品交易所-期权-日频行情数据
http://www.czce.com.cn/cn/sspz/dejbqhqq/H770227index_1.htm#tabs-2
:param trade_date: 交易日
:type trade_date: str
:param symbol: choice of {"白糖期权", "棉花期权", "甲醇期权", "PTA期权", "动力煤期权", "菜籽粕期权", "菜籽油期权",
"花生期权", "对二甲苯期权", "烧碱期权", "纯碱期权", "短纤期权", "锰硅期权", "硅铁期权", "尿素期权", "苹果期权", "红枣期权",
"玻璃期权", "瓶片期权", "丙烯期货"}
:type symbol: str
:return: 日频行情数据
:rtype: pandas.DataFrame

---

### `option_hist_dce(symbol: str = '聚丙烯期权', trade_date: str = '20251016') -> pandas.DataFrame`

大连商品交易所-期权-日频行情数据
http://www.dce.com.cn/
:param trade_date: 交易日
:type trade_date: str
:param symbol: choice of {"玉米期权", "豆粕期权", "铁矿石期权", "液化石油气期权", "聚乙烯期权", "聚氯乙烯期权",
"聚丙烯期权", "棕榈油期权", "黄大豆1号期权", "黄大豆2号期权", "豆油期权", "乙二醇期权", "苯乙烯期权",
"鸡蛋期权", "玉米淀粉期权", "生猪期权", "原木期权"}
:type symbol: str
:return: 日频行情数据
:rtype: pandas.DataFrame

---

### `option_hist_gfex(symbol: str = '工业硅', trade_date: str = '20230724') -> pandas.DataFrame`

广州期货交易所-日频率-量价数据
http://www.gfex.com.cn/gfex/rihq/hqsj_tjsj.shtml
:param trade_date: 交易日
:type trade_date: str
:param symbol: choice of {"工业硅", "碳酸锂"}
:type symbol: str
:return: 日频行情数据
:rtype: pandas.DataFrame

---

### `option_hist_shfe(symbol: str = '铝期权', trade_date: str = '20250418') -> pandas.DataFrame`

上海期货交易所-期权-日频行情数据
https://www.shfe.com.cn/reports/tradedata/dailyandweeklydata/
:param trade_date: 交易日
:type trade_date: str
:param symbol: choice of {'原油期权', '铜期权', '铝期权', '锌期权', '铅期权', '螺纹钢期权', '镍期权', '锡期权', '氧化铝期权',
'黄金期权', '白银期权', '丁二烯橡胶期权', '天胶期权'}
:type symbol: str
:return: 日频行情数据
:rtype: pandas.DataFrame

---

### `option_hist_yearly_czce(symbol: str = 'SR', year: str = '2021') -> pandas.DataFrame`

郑州商品交易所-交易数据-历史行情下载-期权历史行情下载
http://www.czce.com.cn/cn/jysj/lshqxz/H770319index_1.htm
:param symbol: choice of {"白糖": "SR", "棉花": "CF", "PTA": "TA", "甲醇": "MA", "菜籽粕": "RM",
"动力煤": "ZC", "菜籽油": "OI", "花生": "PK", "对二甲苯": "PX", "烧碱": "SH", "纯碱": "SA", "短纤": "PF",
"锰硅": "SM", "硅铁": "SF", "尿素": "UR", "苹果": "AP", "红枣": "CJ", "玻璃": "FG", "瓶片": "PR"}
:type symbol: str
:param year: 需要获取数据的年份, 注意品种的上市时间
:type year: str
:return: 指定年份的日频期权数据
:rtype: pandas.DataFrame

---

### `option_lhb_em(symbol: str = '510050', indicator: str = '期权交易情况-认沽交易量', trade_date: str = '20220121') -> pandas.DataFrame`

东方财富网-数据中心-期货期权-期权龙虎榜单
https://data.eastmoney.com/other/qqlhb.html
:param symbol: 期权代码; choice of {"510050", "510300", "159919"}
:type symbol: str
:param indicator: 需要获取的指标; choice of {"期权交易情况-认沽交易量","期权持仓情况-认沽持仓量", "期权交易情况-认购交易量", "期权持仓情况-认购持仓量"}
:type indicator: str
:param trade_date: 交易日期
:type trade_date: str
:return: 期权龙虎榜单
:rtype: pandas.DataFrame

---

### `option_margin(symbol: str = '原油期权') -> pandas.DataFrame`

获取商品期权保证金
:param symbol: 商品期权品种名称, 如 "原油期权"，可以通过 ak.option_margin_symbol() 获取所有商品期权品种代码和名称
:type symbol: str
:return: 商品期权保证金
:rtype: pandas.DataFrame

---

### `option_margin_symbol() -> pandas.DataFrame`

获取商品期权品种代码和名称
:return: 商品期权品种代码和名称
:rtype: pandas.DataFrame

---

### `option_minute_em(symbol: str = 'MO2404-P-4450') -> pandas.DataFrame`

东方财富网-行情中心-期权市场-分时行情
https://wap.eastmoney.com/quote/stock/151.cu2404P61000.html
:param symbol: 期权代码; 通过调用 ak.option_current_em() 获取
:type symbol: str
:return: 指定期权的分钟频率数据
:rtype: pandas.DataFrame

---

### `option_premium_analysis_em() -> pandas.DataFrame`

东方财富网-数据中心-特色数据-期权折溢价
https://data.eastmoney.com/other/premium.html
:return: 期权折溢价
:rtype: pandas.DataFrame

---

### `option_risk_analysis_em() -> pandas.DataFrame`

东方财富网-数据中心-特色数据-期权风险分析
https://data.eastmoney.com/other/riskanal.html
:return: 期权风险分析
:rtype: pandas.DataFrame

---

### `option_risk_indicator_sse(date: str = '20240626') -> pandas.DataFrame`

上海证券交易所-产品-股票期权-期权风险指标
http://www.sse.com.cn/assortment/options/risk/
:param date: 日期; 20150209 开始
:type date: str
:return: 期权风险指标
:rtype: pandas.DataFrame

---

### `option_sse_codes_sina(symbol: str = '看涨期权', trade_date: str = '202202', underlying: str = '510050') -> pandas.DataFrame`

上海证券交易所-所有看涨和看跌合约的代码

:param symbol: choice of {"看涨期权", "看跌期权"}
:type symbol: str
:param trade_date: 期权到期月份
:type trade_date: "202002"
:param underlying: 标的产品代码 华夏上证 50ETF: 510050 or 华泰柏瑞沪深 300ETF: 510300
:type underlying: str
:return: 看涨看跌合约的代码
:rtype: Tuple[List, List]

---

### `option_sse_daily_sina(symbol: str = '10003889') -> pandas.DataFrame`

指定期权的日频率数据
:param symbol: 期权代码
:type symbol: str
:return: 指定期权的所有日频率历史数据
:rtype: pandas.DataFrame

---

### `option_sse_expire_day_sina(trade_date: str = '202102', symbol: str = '50ETF', exchange: str = 'null') -> Tuple[str, int]`

指定到期月份指定品种的剩余到期时间
:param trade_date: 到期月份: 202002, 20203, 20206, 20209
:type trade_date: str
:param symbol: 50ETF or 300ETF
:type symbol: str
:param exchange: null
:type exchange: str
:return: (到期时间, 剩余时间)
:rtype: tuple

---

### `option_sse_greeks_sina(symbol: str = '10003045') -> pandas.DataFrame`

期权基本信息表
:param symbol: 合约代码
:type symbol: str
:return: 期权基本信息表
:rtype: pandas.DataFrame

---

### `option_sse_list_sina(symbol: str = '50ETF', exchange: str = 'null') -> List[str]`

新浪财经-期权-上交所-50ETF-合约到期月份列表
https://stock.finance.sina.com.cn/option/quotes.html
:param symbol: 50ETF or 300ETF
:type symbol: str
:param exchange: null
:type exchange: str
:return: 合约到期时间
:rtype: list

---

### `option_sse_minute_sina(symbol: str = '10003720') -> pandas.DataFrame`

指定期权品种在当前交易日的分钟数据, 只能获取当前交易日的数据, 不能获取历史分钟数据
https://stock.finance.sina.com.cn/option/quotes.html
:param symbol: 期权代码
:type symbol: str
:return: 指定期权的当前交易日的分钟数据
:rtype: pandas.DataFrame

---

### `option_sse_spot_price_sina(symbol: str = '10003720') -> pandas.DataFrame`

新浪财经-期权-期权实时数据
:param symbol: 期权代码
:type symbol: str
:return: 期权量价数据
:rtype: pandas.DataFrame

---

### `option_sse_underlying_spot_price_sina(symbol: str = 'sh510300') -> pandas.DataFrame`

期权标的物的实时数据
:param symbol: sh510050 or sh510300
:type symbol: str
:return: 期权标的物的信息
:rtype: pandas.DataFrame

---

### `option_value_analysis_em() -> pandas.DataFrame`

东方财富网-数据中心-特色数据-期权价值分析
https://data.eastmoney.com/other/valueAnal.html
:return: 期权价值分析
:rtype: pandas.DataFrame

---

### `option_vol_gfex(symbol: str = '碳酸锂', trade_date: str = '20230724')`

广州期货交易所-日频率-合约隐含波动率
http://www.gfex.com.cn/gfex/rihq/hqsj_tjsj.shtml
:param symbol: choice of choice of {"工业硅", "碳酸锂"}
:type symbol: str
:param trade_date: 交易日
:type trade_date: str
:return: 日频行情数据
:rtype: pandas.DataFrame

---

### `option_vol_shfe(symbol: str = '铝期权', trade_date: str = '20250418') -> pandas.DataFrame`

上海期货交易所-期权-日频行情数据
https://www.shfe.com.cn/reports/tradedata/dailyandweeklydata/
:param trade_date: 交易日
:type trade_date: str
:param symbol: choice of {'原油期权', '铜期权', '铝期权', '锌期权', '铅期权', '螺纹钢期权', '镍期权', '锡期权', '氧化铝期权',
'黄金期权', '白银期权', '丁二烯橡胶期权', '天胶期权'}
:type symbol: str
:return: 日频行情数据
:rtype: pandas.DataFrame

---

