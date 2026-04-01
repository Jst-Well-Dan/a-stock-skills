# Futures 域接口详情

> 共 67 个接口，覆盖国内四大交易所及外盘期货 行情/持仓/仓单/结算/库存等。

## 接口列表

### `futures_comex_inventory(symbol: str = '黄金') -> pandas.DataFrame`

东方财富网-数据中心-期货期权-COMEX库存数据
https://data.eastmoney.com/pmetal/comex/by.html
:param symbol: choice of {"黄金", "白银"}
:type symbol: str
:return: COMEX库存数据
:rtype: pandas.DataFrame

---

### `futures_comm_info(symbol: str = '所有') -> pandas.DataFrame`

九期网-期货手续费
https://www.9qihuo.com/qihuoshouxufei
:param symbol: choice of {"所有", "上海期货交易所", "大连商品交易所", "郑州商品交易所", "上海国际能源交易中心", "中国金融期货交易所", "广州期货交易所"}
:type symbol: str
:return: 期货手续费
:rtype: pandas.DataFrame

---

### `futures_comm_js(date: str = '20260213') -> pandas.DataFrame`

金十财经-期货手续费
https://www.jin10.com/
:param date: 日期; 格式为 YYYYMMDD，例如 "20250213"
:type date: str
:return: 期货手续费数据
:rtype: pandas.DataFrame

---

### `futures_contract_detail(symbol: str = 'AP2101') -> pandas.DataFrame`

查询期货合约详情
https://finance.sina.com.cn/futures/quotes/V2101.shtml
:param symbol: 合约
:type symbol: str
:return: 期货合约详情
:rtype: pandas.DataFrame

---

### `futures_contract_detail_em(symbol: str = 'v2602F') -> pandas.DataFrame`

查询期货合约详情
https://quote.eastmoney.com/qihuo/v2602F.html
:param symbol: 合约
:type symbol: str
:return: 期货合约详情
:rtype: pandas.DataFrame

---

### `futures_contract_info_cffex(date: str = '20240228') -> pandas.DataFrame`

中国金融期货交易所-数据-交易参数
http://www.gfex.com.cn/gfex/hyxx/ywcs.shtml
:param date: 查询日期
:type date: str
:return: 交易参数汇总查询
:rtype: pandas.DataFrame

---

### `futures_contract_info_czce(date: str = '20240228') -> pandas.DataFrame`

郑州商品交易所-交易数据-参考数据
http://www.czce.com.cn/cn/jysj/cksj/H770322index_1.htm
:param date: 查询日期
:type date: str
:return: 交易参数汇总查询
:rtype: pandas.DataFrame

---

### `futures_contract_info_dce() -> pandas.DataFrame`

大连商品交易所-数据中心-业务数据-交易参数-合约信息
http://www.dce.com.cn/dce/channel/list/180.html
:return: 交易参数汇总查询
:rtype: pandas.DataFrame

---

### `futures_contract_info_gfex() -> pandas.DataFrame`

广州期货交易所-业务/服务-合约信息
http://www.gfex.com.cn/gfex/hyxx/ywcs.shtml
:return: 交易参数汇总查询
:rtype: pandas.DataFrame

---

### `futures_contract_info_ine(date: str = '20241129') -> pandas.DataFrame`

上海国际能源交易中心-业务指南-交易参数汇总(期货)
https://www.ine.cn/bourseService/summary/?name=currinstrumentprop
:param date: 查询日期; 交易日
:type date: str
:return: 交易参数汇总查询
:rtype: pandas.DataFrame

---

### `futures_contract_info_shfe(date: str = '20240513') -> pandas.DataFrame`

上海期货交易所-交易所服务-业务数据-交易参数汇总查询
https://tsite.shfe.com.cn/bourseService/businessdata/summaryinquiry/
:param date: 查询日期; 交易日
:type date: str
:return: 交易参数汇总查询
:rtype: pandas.DataFrame

---

### `futures_dce_position_rank(date: str = '20160919', vars_list=['IF', 'IC', 'IM', 'IH', 'T', 'TF', 'TS', 'TL', 'C', 'CS', 'A', 'B', 'M', 'Y', 'P', 'FB', 'BB', 'JD', 'L', 'V', 'PP', 'J', 'JM', 'I', 'EG', 'RR', 'EB', 'PG', 'LH', 'LG', 'BZ', 'WH', 'PM', 'CF', 'SR', 'TA', 'OI', 'RI', 'MA', 'ME', 'FG', 'RS', 'RM', 'ZC', 'JR', 'LR', 'SF', 'SM', 'WT', 'TC', 'GN', 'RO', 'ER', 'SRX', 'SRY', 'WSX', 'WSY', 'CY', 'AP', 'UR', 'CJ', 'SA', 'PK', 'PF', 'PX', 'SH', 'PR', 'PL', 'CU', 'AL', 'ZN', 'PB', 'NI', 'SN', 'AU', 'AG', 'RB', 'WR', 'HC', 'FU', 'BU', 'RU', 'SC', 'NR', 'SP', 'SS', 'LU', 'BC', 'AO', 'BR', 'EC', 'AD', 'OP', 'SI', 'LC', 'PS']) -> dict`

大连商品交易所-每日持仓排名-具体合约
http://www.dce.com.cn/dalianshangpin/xqsj/tjsj26/rtj/rcjccpm/index.html
:param date: 指定交易日; e.g., "20200511"
:type date: str
:param vars_list: 品种列表
:type vars_list: list
:return: 指定日期的持仓排名数据
:rtype: pandas.DataFrame

---

### `futures_dce_position_rank_other(date: str = '20160104')`

大连商品交易所-每日持仓排名-具体合约-补充
http://www.dce.com.cn/dalianshangpin/xqsj/tjsj26/rtj/rcjccpm/index.html
:param date: 交易日
:type date: str
:return: 合约具体名称列表
:rtype: list

---

### `futures_delivery_czce(date: str = '20210112') -> pandas.DataFrame`

郑州商品交易所-月度交割查询
http://www.czce.com.cn/cn/jysj/ydjgcx/H770316index_1.htm
:param date: 年月日
:type date: str
:return: 郑州商品交易所-月度交割查询
:rtype: pandas.DataFrame

---

### `futures_delivery_dce(date: str = '202312') -> pandas.DataFrame`

大连商品交易所-交割统计
http://www.dce.com.cn/dalianshangpin/xqsj/tjsj26/jgtj/jgsj/index.html
:param date: 交割日期
:type date: str
:return: 大连商品交易所-交割统计
:rtype: pandas.DataFrame

---

### `futures_delivery_match_czce(date: str = '20210106') -> pandas.DataFrame`

郑州商品交易所-交割配对
http://www.czce.com.cn/cn/jysj/jgpd/H770308index_1.htm
:param date: 年月日
:type date: str
:return: 郑州商品交易所-交割配对
:rtype: pandas.DataFrame

---

### `futures_delivery_match_dce(symbol: str = 'a') -> pandas.DataFrame`

大连商品交易所-交割配对表
http://www.dce.com.cn/dalianshangpin/xqsj/tjsj26/jgtj/jgsj/index.html
:param symbol: 交割品种
:type symbol: str
:return: 大连商品交易所-交割配对表
:rtype: pandas.DataFrame

---

### `futures_delivery_shfe(date: str = '202312') -> pandas.DataFrame`

上海期货交易所-交割情况表
https://tsite.shfe.com.cn/statements/dataview.html?paramid=kx
注意: 日期 -> 月度统计 -> 下拉到交割情况表
:param date: 年月日
:type date: str
:return: 上海期货交易所-交割情况表
:rtype: pandas.DataFrame

---

### `futures_display_main_sina() -> pandas.DataFrame`

新浪主力连续合约品种一览表
https://finance.sina.com.cn/futuremarket/index.shtml
:return: 新浪主力连续合约品种一览表
:rtype: pandas.DataFrame

---

### `futures_fees_info() -> pandas.DataFrame`

openctp 期货交易费用参照表
http://openctp.cn/fees.html
:return: 期货交易费用参照表
:rtype: pandas.DataFrame

---

### `futures_foreign_commodity_realtime(symbol: Union[str, List[str]]) -> pandas.DataFrame`

新浪-外盘期货-行情数据
https://finance.sina.com.cn/money/future/hf.html
:param symbol: 通过调用 ak.futures_hq_subscribe_exchange_symbol() 函数来获取
:type symbol: list or str
:return: 行情数据
:rtype: pandas.DataFrame

---

### `futures_foreign_commodity_subscribe_exchange_symbol() -> list`

需要订阅的行情的代码
https://finance.sina.com.cn/money/future/hf.html
:return: 需要订阅的行情的代码
:rtype: list

---

### `futures_foreign_detail(symbol: str = 'ZSD') -> pandas.DataFrame`

foreign futures contract detail data
:param symbol: futures symbol, you can get it from hf_subscribe_exchange_symbol function
:type symbol: str
:return: contract detail
:rtype: pandas.DataFrame

---

### `futures_foreign_hist(symbol: str = 'ZSD') -> pandas.DataFrame`

外盘期货-历史行情数据-日频率
https://finance.sina.com.cn/money/future/hf.html
:param symbol: 外盘期货代码, 可以通过 ak.futures_foreign_commodity_subscribe_exchange_symbol() 来获取所有品种代码
:type symbol: str
:return: 历史行情数据-日频率
:rtype: pandas.DataFrame

---

### `futures_gfex_position_rank(date: str = '20231113', vars_list: list = None)`

广州期货交易所-日成交持仓排名
http://www.gfex.com.cn/gfex/rcjccpm/hqsj_tjsj.shtml
:param date: 开始日期; 广州期货交易所的日成交持仓排名从 20231110 开始
:type date: str
:param vars_list: 商品代码列表
:type vars_list: list
:return: 日成交持仓排名
:rtype: pandas.DataFrame

---

### `futures_gfex_warehouse_receipt(date: str = '20240122') -> dict`

广州期货交易所-行情数据-仓单日报
http://www.gfex.com.cn/gfex/cdrb/hqsj_tjsj.shtml
:param date: 交易日, e.g., "20240122"
:type date: str
:return: 指定日期的仓单日报数据
:rtype: dict

---

### `futures_global_hist_em(symbol: str = 'HG00Y') -> pandas.DataFrame`

东方财富网-行情中心-期货市场-国际期货-历史行情数据
https://quote.eastmoney.com/globalfuture/HG25J.html
:param symbol: 品种代码；可以通过 ak.futures_global_spot_em() 来获取所有可获取历史行情数据的品种代码
:type symbol: str
:return: 历史行情数据
:rtype: pandas.DataFrame

---

### `futures_global_spot_em() -> pandas.DataFrame`

东方财富网-行情中心-期货市场-国际期货
https://quote.eastmoney.com/center/gridlist.html#futures_global
:return: 行情数据
:rtype: pandas.DataFrame

---

### `futures_hist_em(symbol: str = '热卷主连', period: str = 'daily', start_date: str = '19900101', end_date: str = '20500101') -> pandas.DataFrame`

东方财富网-期货行情-行情数据
https://qhweb.eastmoney.com/quote
:param symbol: 期货代码
:type symbol: str
:param period: choice of {'daily', 'weekly', 'monthly'}
:type period: str
:param start_date: 开始日期
:type start_date: str
:param end_date: 结束日期
:type end_date: str
:return: 行情数据
:rtype: pandas.DataFrame

---

### `futures_hist_table_em() -> pandas.DataFrame`

东方财富网-期货行情-交易所品种对照表
https://quote.eastmoney.com/qihuo/al2505.html
:return: 交易所品种对照表
:rtype: pandas.DataFrame

---

### `futures_hog_core(symbol: str = '外三元') -> pandas.DataFrame`

玄田数据-核心数据
https://zhujia.zhuwang.com.cn
:param symbol: choice of {"外三元", "内三元", "土杂猪"}
:type symbol: str
:return: 玄田数据-核心数据
:rtype: pandas.DataFrame

---

### `futures_hog_cost(symbol: str = '玉米') -> pandas.DataFrame`

玄田数据-成本维度
https://zhujia.zhuwang.com.cn
:param symbol: choice of {"玉米", "豆粕", "二元母猪价格", "仔猪价格"}
:type symbol: str
:return: 玄田数据-成本维度
:rtype: pandas.DataFrame

---

### `futures_hog_supply(symbol: str = '猪肉批发价') -> pandas.DataFrame`

玄田数据-供应维度
https://zhujia.zhuwang.com.cn
:param symbol: choice of {"猪肉批发价", "储备冻猪肉", "饲料原料数据", "白条肉",
"生猪产能", "育肥猪", "肉类价格指数", "猪粮比价"}
:type symbol: str
:return: 玄田数据-供应维度
:rtype: pandas.DataFrame

---

### `futures_hold_pos_sina(symbol: str = '成交量', contract: str = 'OI2501', date: str = '20240223') -> pandas.DataFrame`

新浪财经-期货-成交持仓
https://vip.stock.finance.sina.com.cn/q/view/vFutures_Positions_cjcc.php
:param symbol: choice of {"成交量", "多单持仓", "空单持仓"}
:type symbol: str
:param contract: 期货合约
:type contract: str
:param date: 查询日期
:type date: str
:return: 成交持仓
:rtype: pandas.DataFrame

---

### `futures_hq_subscribe_exchange_symbol() -> pandas.DataFrame`

将品种字典转化为 pandas.DataFrame
https://finance.sina.com.cn/money/future/hf.html
:return: 品种对应表
:rtype: pandas.DataFrame

---

### `futures_index_ccidx(symbol: str = '中证商品期货指数') -> pandas.DataFrame`

中证商品指数-商品指数-日频率
http://www.ccidx.com/index.html
:param symbol: choice of {"中证商品期货指数", "中证商品期货价格指数"}
:type symbol: str
:return: 商品指数-日频率
:rtype: pandas.DataFrame

---

### `futures_inventory_99(symbol: str = '豆一') -> pandas.DataFrame`

99 期货网-大宗商品库存数据
https://www.99qh.com/data/stockIn?productId=12
:param symbol: 交易所对应的具体品种; 如：大连商品交易所的 豆一
:type symbol: str
:return: 大宗商品库存数据
:rtype: pandas.DataFrame

---

### `futures_inventory_em(symbol: str = 'a') -> pandas.DataFrame`

东方财富网-数据中心-期货库存数据
https://data.eastmoney.com/ifdata/kcsj.html
:param symbol: 支持品种代码和中文名称，中文名称参见：https://data.eastmoney.com/ifdata/kcsj.html
:type symbol: str
:return: 指定品种的库存数据
:rtype: pandas.DataFrame

---

### `futures_main_sina(symbol: str = 'V0', start_date: str = '19900101', end_date: str = '22220101') -> pandas.DataFrame`

新浪财经-期货-主力连续日数据
https://vip.stock.finance.sina.com.cn/quotes_service/view/qihuohangqing.html#titlePos_1
:param symbol: 通过 ak.futures_display_main_sina() 函数获取 symbol
:type symbol: str
:param start_date: 开始时间
:type start_date: str
:param end_date: 结束时间
:type end_date: str
:return: 主力连续日数据
:rtype: pandas.DataFrame

---

### `futures_news_shmet(symbol: str = '全部') -> pandas.DataFrame`

上海金属网-快讯
https://www.shmet.com/newsFlash/newsFlash.html?searchKeyword=
:param symbol: choice of {"全部", "要闻", "VIP", "财经", "铜", "铝", "铅", "锌", "镍", "锡", "贵金属", "小金属"}
:type symbol: str
:return: 上海金属网-快讯
:rtype: pandas.DataFrame

---

### `futures_rule(date: str = '20231205') -> pandas.DataFrame`

国泰君安期货-交易日历数据表
https://www.gtjaqh.com/pc/calendar.html
:param date: 需要指定为交易日, 且是近期的日期
:type date: str
:return: 交易日历数据
:rtype: pandas.DataFrame

---

### `futures_settle(date: str = '20260119', market: str = 'CFFEX') -> pandas.DataFrame`

期货交易所结算参数
:param date: 结算日期 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象，默认为当前交易日
:type date: str or datetime.date
:param market: 交易所代码: CFFEX-中金所, CZCE-郑商所, SHFE-上期所, DCE-大商所, INE-上能中心, GFEX-广期所
:type market: str
:return: 结算参数数据（统一格式）
:rtype: pandas.DataFrame

---

### `futures_settle_cffex(date: str = '20260119') -> pandas.DataFrame`

中国金融期货交易所-结算参数
http://www.cffex.com.cn/jscs/
:param date: 结算参数日期 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象，默认为当前交易日
:type date: str or datetime.date
:return: 结算参数数据
:rtype: pandas.DataFrame

---

### `futures_settle_czce(date: str = '20260119') -> pandas.DataFrame`

郑州商品交易所-结算参数
http://www.czce.com.cn/cn/jysj/jscs/H077003003index_1.htm
:param date: 结算参数日期 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象，默认为当前交易日
:type date: str or datetime.date
:return: 结算参数数据
:rtype: pandas.DataFrame

---

### `futures_settle_gfex(date: str = '20260119') -> pandas.DataFrame`

广州期货交易所-结算参数
http://www.gfex.com.cn/gfex/rjycs/ywcs.shtml
:param date: 结算参数日期 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象，默认为当前交易日
:type date: str or datetime.date
:return: 结算参数数据
:rtype: pandas.DataFrame

---

### `futures_settle_ine(date: str = '20260119') -> pandas.DataFrame`

上海国际能源交易中心-结算参数
https://www.ine.cn/reports/businessdata/prmsummary/
:param date: 结算参数日期 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象，默认为当前交易日
:type date: str or datetime.date
:return: 结算参数数据
:rtype: pandas.DataFrame

---

### `futures_settle_shfe(date: str = '20260119') -> pandas.DataFrame`

上海期货交易所-结算参数
https://www.shfe.com.cn/reports/tradedata/dailyandweeklydata/
:param date: 结算参数日期 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象，默认为当前交易日
:type date: str or datetime.date
:return: 结算参数数据
:rtype: pandas.DataFrame

---

### `futures_settlement_price_sgx(date: str = '20231107') -> pandas.DataFrame`

新加坡交易所-衍生品-历史数据-历史结算价格
https://www.sgx.com/zh-hans/research-education/derivatives
:param date: 交易日
:type date: str
:return: 所有期货品种的在指定交易日的历史结算价格
:rtype: pandas.DataFrame

---

### `futures_shfe_warehouse_receipt(date: str = '20200702') -> dict`

上海期货交易所指定交割仓库期货仓单日报
https://tsite.shfe.com.cn/statements/dataview.html?paramid=dailystock&paramdate=20200703
:param date: 交易日, e.g., "20200702"
:type date: str
:return: 指定日期的仓单日报数据
:rtype: dict

---

### `futures_spot_price(date: str = '20240430', vars_list: list = ['IF', 'IC', 'IM', 'IH', 'T', 'TF', 'TS', 'TL', 'C', 'CS', 'A', 'B', 'M', 'Y', 'P', 'FB', 'BB', 'JD', 'L', 'V', 'PP', 'J', 'JM', 'I', 'EG', 'RR', 'EB', 'PG', 'LH', 'LG', 'BZ', 'WH', 'PM', 'CF', 'SR', 'TA', 'OI', 'RI', 'MA', 'ME', 'FG', 'RS', 'RM', 'ZC', 'JR', 'LR', 'SF', 'SM', 'WT', 'TC', 'GN', 'RO', 'ER', 'SRX', 'SRY', 'WSX', 'WSY', 'CY', 'AP', 'UR', 'CJ', 'SA', 'PK', 'PF', 'PX', 'SH', 'PR', 'PL', 'CU', 'AL', 'ZN', 'PB', 'NI', 'SN', 'AU', 'AG', 'RB', 'WR', 'HC', 'FU', 'BU', 'RU', 'SC', 'NR', 'SP', 'SS', 'LU', 'BC', 'AO', 'BR', 'EC', 'AD', 'OP', 'SI', 'LC', 'PS']) -> pandas.DataFrame`

指定交易日大宗商品现货价格及相应基差
https://www.100ppi.com/sf/day-2017-09-12.html
:param date: 开始日期 format: YYYY-MM-DD 或 YYYYMMDD 或 datetime.date 对象; 为空时为当天
:param vars_list: 合约品种如 RB、AL 等列表 为空时为所有商品
:return: pandas.DataFrame
展期收益率数据:
var              商品品种                     string
sp               现货价格                     float
near_symbol      临近交割合约                  string
near_price       临近交割合约结算价             float
dom_symbol       主力合约                     string
dom_price        主力合约结算价                float
near_basis       临近交割合约相对现货的基差      float
dom_basis        主力合约相对现货的基差         float
near_basis_rate  临近交割合约相对现货的基差率    float
dom_basis_rate   主力合约相对现货的基差率       float
date             日期                         string YYYYMMDD

---

### `futures_spot_price_daily(start_day: str = '20210201', end_day: str = '20210208', vars_list: list = ['IF', 'IC', 'IM', 'IH', 'T', 'TF', 'TS', 'TL', 'C', 'CS', 'A', 'B', 'M', 'Y', 'P', 'FB', 'BB', 'JD', 'L', 'V', 'PP', 'J', 'JM', 'I', 'EG', 'RR', 'EB', 'PG', 'LH', 'LG', 'BZ', 'WH', 'PM', 'CF', 'SR', 'TA', 'OI', 'RI', 'MA', 'ME', 'FG', 'RS', 'RM', 'ZC', 'JR', 'LR', 'SF', 'SM', 'WT', 'TC', 'GN', 'RO', 'ER', 'SRX', 'SRY', 'WSX', 'WSY', 'CY', 'AP', 'UR', 'CJ', 'SA', 'PK', 'PF', 'PX', 'SH', 'PR', 'PL', 'CU', 'AL', 'ZN', 'PB', 'NI', 'SN', 'AU', 'AG', 'RB', 'WR', 'HC', 'FU', 'BU', 'RU', 'SC', 'NR', 'SP', 'SS', 'LU', 'BC', 'AO', 'BR', 'EC', 'AD', 'OP', 'SI', 'LC', 'PS'])`

指定时间段内大宗商品现货价格及相应基差
https://www.100ppi.com/sf/
:param start_day: str 开始日期 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象; 默认为当天
:param end_day: str 结束数据 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象; 默认为当天
:param vars_list: list 合约品种如 [RB, AL]; 默认参数为所有商品
:return: 基差
:rtype: pandas.DataFrame
展期收益率数据:
var               商品品种                      string
sp                现货价格                      float
near_symbol       临近交割合约                  string
near_price        临近交割合约结算价             float
dom_symbol        主力合约                      string
dom_price         主力合约结算价                 float
near_basis        临近交割合约相对现货的基差      float
dom_basis         主力合约相对现货的基差          float
near_basis_rate   临近交割合约相对现货的基差率    float
dom_basis_rate    主力合约相对现货的基差率        float
date              日期                          string YYYYMMDD

---

### `futures_spot_price_previous(date: str = '20240430') -> pandas.DataFrame`

具体交易日大宗商品现货价格及相应基差
https://www.100ppi.com/sf/day-2017-09-12.html
:param date: 交易日; 历史日期
:type date: str
:return: 现货价格及相应基差
:rtype: pandas.DataFrame

---

### `futures_spot_stock(symbol: str = '能源') -> pandas.DataFrame`

东方财富网-数据中心-现货与股票
https://data.eastmoney.com/ifdata/xhgp.html
:param symbol: choice of {'能源', '化工', '塑料', '纺织', '有色', '钢铁', '建材', '农副'}
:type symbol: str
:return: 现货与股票上下游对应数据
:rtype: pandas.DataFrame

---

### `futures_spot_sys(symbol: str = '铜', indicator: str = '市场价格') -> pandas.DataFrame`

生意社-商品与期货-现期图
https://www.100ppi.com/sf/792.html
:param symbol: 期货品种
:type symbol: str
:param indicator: 市场价格; choice of {"市场价格", "基差率", "主力基差"}
:type indicator: str
:return: pandas.DataFrame
:rtype: dict

---

### `futures_stock_shfe_js(date: str = '20240419') -> pandas.DataFrame`

金十财经-上海期货交易所指定交割仓库库存周报
https://datacenter.jin10.com/reportType/dc_shfe_weekly_stock
:param date: 交易日; 库存周报只在每周的最后一个交易日公布数据
:type date: str
:return: 库存周报
:rtype: pandas.Series

---

### `futures_symbol_mark() -> pandas.DataFrame`

期货的品种和代码映射
https://vip.stock.finance.sina.com.cn/quotes_service/view/js/qihuohangqing.js
:return: 期货的品种和代码映射
:rtype: pandas.DataFrame

---

### `futures_to_spot_czce(date: str = '20231228') -> pandas.DataFrame`

郑州商品交易所-期转现统计
http://www.czce.com.cn/cn/jysj/qzxtj/H770311index_1.htm
:param date: 年月日
:type date: str
:return: 郑州商品交易所-期转现统计
:rtype: pandas.DataFrame

---

### `futures_to_spot_dce(date: str = '202312') -> pandas.DataFrame`

大连商品交易所-期转现
http://www.dce.com.cn/dalianshangpin/xqsj/tjsj26/jgtj/qzxcx/index.html
:param date: 期转现日期
:type date: str
:return: 大连商品交易所-期转现
:rtype: pandas.DataFrame

---

### `futures_to_spot_shfe(date: str = '202312') -> pandas.DataFrame`

上海期货交易所-期转现
https://tsite.shfe.com.cn/statements/dataview.html?paramid=kx
1、铜、铜(BC)、铝、锌、铅、镍、锡、螺纹钢、线材、热轧卷板、天然橡胶、20号胶、低硫燃料油、燃料油、石油沥青、纸浆、不锈钢的数量单位为：吨；黄金的数量单位为：克；白银的数量单位为：千克；原油的数量单位为：桶。
2、交割量、期转现量为单向计算。
:param date: 年月
:type date: str
:return: 上海期货交易所期转现
:rtype: pandas.DataFrame

---

### `futures_warehouse_receipt_czce(date: str = '20251103') -> dict`

郑州商品交易所-交易数据-仓单日报
http://www.czce.com.cn/cn/jysj/cdrb/H770310index_1.htm
:param date: 交易日, e.g., "20200702"
:type date: str
:return: 指定日期的仓单日报数据
:rtype: dict

---

### `futures_warehouse_receipt_dce(date: str = '20251027') -> pandas.DataFrame`

大连商品交易所-行情数据-统计数据-日统计-仓单日报
http://www.dce.com.cn/dce/channel/list/187.html
:param date: 交易日, e.g., "20200702"
:type date: str
:return: 指定日期的仓单日报数据
:rtype: dict

---

### `futures_zh_daily_sina(symbol: str = 'RB0') -> pandas.DataFrame`

中国各品种期货日频率数据
https://finance.sina.com.cn/futures/quotes/V2105.shtml
:param symbol: 可以通过 match_main_contract(symbol="cffex") 获取, 或者访问网页获取
:type symbol: str
:return: 指定 symbol 的数据
:rtype: pandas.DataFrame

---

### `futures_zh_minute_sina(symbol: str = 'IF2008', period: str = '1') -> pandas.DataFrame`

中国各品种期货分钟频率数据
https://vip.stock.finance.sina.com.cn/quotes_service/view/qihuohangqing.html#titlePos_3
:param symbol: 可以通过 match_main_contract(symbol="cffex") 获取, 或者访问网页获取
:type symbol: str
:param period: choice of {"1": "1分钟", "5": "5分钟", "15": "15分钟", "30": "30分钟", "60": "60分钟"}
:type period: str
:return: 指定 symbol 和 period 的数据
:rtype: pandas.DataFrame

---

### `futures_zh_realtime(symbol: str = 'PTA') -> pandas.DataFrame`

期货品种当前时刻所有可交易的合约实时数据
https://vip.stock.finance.sina.com.cn/quotes_service/view/qihuohangqing.html#titlePos_1
:param symbol: 品种名称；可以通过 ak.futures_symbol_mark() 获取所有品种命名表
:type symbol: str
:return: 期货品种当前时刻所有可交易的合约实时数据
:rtype: pandas.DataFrame

---

### `futures_zh_spot(symbol: str = 'V2309', market: str = 'CF', adjust: str = '0') -> pandas.DataFrame`

期货的实时行情数据
https://vip.stock.finance.sina.com.cn/quotes_service/view/qihuohangqing.html#titlePos_1
:param symbol: 合约名称的字符串组合
:type symbol: str
:param market: CF 为商品期货
:type market: str
:param adjust: '1' or '0'；字符串的 0 或 1；返回合约、交易所和最小变动单位的实时数据, 返回数据会变慢
:type adjust: str
:return: 期货的实时行情数据
:rtype: pandas.DataFrame

---

