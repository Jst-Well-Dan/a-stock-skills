# 其他域接口详情

> 覆盖现货(spot)、外汇(fx)、货币(currency)、能源碳排(energy)、AMAC、QDII、REITs、申万行业(sw)等域。

## 接口列表

### `amac_aoin_info() -> pandas.DataFrame`

中国证券投资基金业协会-信息公示-基金产品公示-证券公司直投基金
https://gs.amac.org.cn/amac-infodisc/res/aoin/product/index.html
:return: 证券公司直投基金
:rtype: pandas.DataFrame

---

### `amac_fund_abs() -> pandas.DataFrame`

中国证券投资基金业协会-信息公示-基金产品公示-资产支持专项计划公示信息
https://gs.amac.org.cn/amac-infodisc/res/fund/abs/index.html
:return: 资产支持专项计划公示信息
:rtype: pandas.DataFrame

---

### `amac_fund_account_info() -> pandas.DataFrame`

中国证券投资基金业协会-信息公示-基金产品公示-基金公司及子公司集合资管产品公示
https://gs.amac.org.cn/amac-infodisc/res/fund/account/index.html
:return: 基金公司及子公司集合资管产品公示
:rtype: pandas.DataFrame

---

### `amac_fund_info(start_page: str = '1', end_page: str = '2000') -> pandas.DataFrame`

中国证券投资基金业协会-信息公示-基金产品-私募基金管理人基金产品
https://gs.amac.org.cn/amac-infodisc/res/pof/fund/index.html
:param start_page: 开始页码, 获取指定页码直接的数据
:type start_page: str
:param end_page: 结束页码, 获取指定页码直接的数据
:type end_page: str
:return: 私募基金管理人基金产品
:rtype: pandas.DataFrame

---

### `amac_fund_sub_info() -> pandas.DataFrame`

中国证券投资基金业协会-信息公示-基金产品公示-证券公司私募投资基金
https://gs.amac.org.cn/amac-infodisc/res/pof/subfund/index.html
:return: 证券公司私募投资基金
:rtype: pandas.DataFrame

---

### `amac_futures_info() -> pandas.DataFrame`

中国证券投资基金业协会-信息公示-基金产品公示-期货公司集合资管产品公示
https://gs.amac.org.cn/amac-infodisc/res/pof/futures/index.html
:return: 期货公司集合资管产品公示
:rtype: pandas.DataFrame

---

### `amac_manager_cancelled_info() -> pandas.DataFrame`

中国证券投资基金业协会-信息公示-诚信信息公示-已注销私募基金管理人名单
https://gs.amac.org.cn/amac-infodisc/res/cancelled/manager/index.html
主动注销: 100
依公告注销: 200
协会注销: 300
:return: 已注销私募基金管理人名单
:rtype: pandas.DataFrame

---

### `amac_manager_classify_info() -> pandas.DataFrame`

中国证券投资基金业协会-信息公示-私募基金管理人公示-私募基金管理人分类公示
https://gs.amac.org.cn/amac-infodisc/res/pof/manager/managerList.html
:return: 私募基金管理人分类公示
:rtype: pandas.DataFrame

---

### `amac_manager_info() -> pandas.DataFrame`

中国证券投资基金业协会-信息公示-私募基金管理人公示-私募基金管理人综合查询
https://gs.amac.org.cn/amac-infodisc/res/pof/manager/index.html
:return: 私募基金管理人综合查询
:rtype: pandas.DataFrame

---

### `amac_member_info() -> pandas.DataFrame`

中国证券投资基金业协会-信息公示-会员信息-会员机构综合查询
https://gs.amac.org.cn/amac-infodisc/res/pof/member/index.html
:return: 会员机构综合查询
:rtype: pandas.DataFrame

---

### `amac_member_sub_info() -> pandas.DataFrame`

中国证券投资基金业协会-信息公示-私募基金管理人公示-证券公司私募基金子公司管理人信息公示
https://gs.amac.org.cn/amac-infodisc/res/pof/member/index.html?primaryInvestType=private
:return: 证券公司私募基金子公司管理人信息公示
:rtype: pandas.DataFrame

---

### `amac_person_bond_org_list() -> pandas.DataFrame`

中国证券投资基金业协会-信息公示-从业人员信息-债券投资交易相关人员公示
https://human.amac.org.cn/web/org/personPublicity.html
:return: 债券投资交易相关人员公示
:rtype: pandas.DataFrame

---

### `amac_person_fund_org_list(symbol: str = '公募基金管理公司') -> pandas.DataFrame`

中国证券投资基金业协会-信息公示-从业人员信息-基金从业人员资格注册信息
https://gs.amac.org.cn/amac-infodisc/res/pof/person/personOrgList.html
:param symbol: choice of {"公募基金管理公司", "公募基金管理公司资管子公司", "商业银行", "证券公司", "证券公司子公司",
"私募基金管理人", "保险公司子公司", "保险公司", "外包服务机构", "期货公司", "期货公司资管子公司", "媒体机构",
"证券投资咨询机构", "评价机构", "外资私募证券基金管理人", "支付结算", "独立服务机构", "地方自律组织", "境外机构",
"律师事务所", "会计师事务所", "交易所", "独立第三方销售机构", "证券公司资管子公司", "证券公司私募基金子公司", "其他"}
:type symbol: str
:return: 基金从业人员资格注册信息
:rtype: pandas.DataFrame

---

### `amac_securities_info() -> pandas.DataFrame`

中国证券投资基金业协会-信息公示-基金产品公示-证券公司集合资管产品公示
https://gs.amac.org.cn/amac-infodisc/res/pof/securities/index.html
:return: 证券公司集合资管产品公示
:rtype: pandas.DataFrame

---

### `crypto_bitcoin_cme(date: str = '20230830') -> pandas.DataFrame`

芝加哥商业交易所-比特币成交量报告
https://datacenter.jin10.com/reportType/dc_cme_btc_report
:param date: Specific date, e.g., "20230830"
:type date: str
:return: 比特币成交量报告
:rtype: pandas.DataFrame

---

### `crypto_bitcoin_hold_report()`

金十数据-比特币持仓报告
https://datacenter.jin10.com/dc_report?name=bitcoint
:return: 比特币持仓报告
:rtype: pandas.DataFrame

---

### `crypto_js_spot() -> pandas.DataFrame`

主流加密货币的实时行情数据, 一次请求返回具体某一时刻行情数据
https://datacenter.jin10.com/reportType/dc_bitcoin_current
:return: pandas.DataFrame

---

### `currency_boc_safe() -> pandas.DataFrame`

人民币汇率中间价
https://www.safe.gov.cn/safe/rmbhlzjj/index.html
:return: 人民币汇率中间价
:rtype: pandas.DataFrame

---

### `currency_boc_sina(symbol: str = '美元', start_date: str = '20230304', end_date: str = '20231110') -> pandas.DataFrame`

新浪财经-中行人民币牌价历史数据查询
https://biz.finance.sina.com.cn/forex/forex.php?startdate=2012-01-01&enddate=2021-06-14&money_code=EUR&type=0
:param symbol: choice of {'美元', '英镑', '欧元', '澳门元', '泰国铢', '菲律宾比索', '港币', '瑞士法郎', '新加坡元', '瑞典克朗', '丹麦克朗', '挪威克朗', '日元', '加拿大元', '澳大利亚元', '新西兰元', '韩国元'}
:type symbol: str
:param start_date: 开始交易日
:type start_date: str
:param end_date: 结束交易日
:type end_date: str
:return: 中行人民币牌价历史数据查询
:rtype: pandas.DataFrame

---

### `currency_convert(base: str = 'USD', to: str = 'CNY', amount: str = '10000', api_key: str = '') -> pandas.DataFrame`

currencies data from currencyscoop.com
https://currencyscoop.com/api-documentation
:param base: The base currency you would like to use for your rates
:type base: str
:param to: The currency you would like to use for your rates
:type to: str
:param amount: The amount of base currency
:type amount: str
:param api_key: Account -> Account Details -> API KEY (use as password in external tools)
:type api_key: str
:return: Latest data of base currency
:rtype: pandas.Series

---

### `currency_currencies(c_type: str = 'fiat', api_key: str = '') -> pandas.DataFrame`

currencies data from currencyscoop.com
https://currencyscoop.com/api-documentation
:param c_type: now only "fiat" can return data
:type c_type: str
:param api_key: Account -> Account Details -> API KEY (use as password in external tools)
:type api_key: str
:return: Latest data of base currency
:rtype: pandas.DataFrame

---

### `currency_history(base: str = 'USD', date: str = '2023-02-03', symbols: str = '', api_key: str = '') -> pandas.DataFrame`

Latest data from currencyscoop.com
https://currencyscoop.com/api-documentation
:param base: The base currency you would like to use for your rates
:type base: str
:param date: Specific date, e.g., "2020-02-03"
:type date: str
:param symbols: A list of currencies you will like to see the rates for. You can refer to a list all supported currencies here
:type symbols: str
:param api_key: Account -> Account Details -> API KEY (use as password in external tools)
:type api_key: str
:return: Latest data of base currency
:rtype: pandas.DataFrame

---

### `currency_latest(base: str = 'USD', symbols: str = '', api_key: str = '') -> pandas.DataFrame`

Latest data from currencyscoop.com
https://currencyscoop.com/api-documentation
:param base: The base currency you would like to use for your rates
:type base: str
:param symbols: A list of currencies you will like to see the rates for. You can refer to a list all supported currencies here
:type symbols: str
:param api_key: Account -> Account Details -> API KEY (use as password in external tools)
:type api_key: str
:return: Latest data of base currency
:rtype: pandas.DataFrame

---

### `currency_pair_map(symbol: str = '美元') -> pandas.DataFrame`

指定货币的所有可获取货币对的数据
https://cn.investing.com/currencies/cny-jmd
:param symbol: 指定货币
:type symbol: str
:return: 指定货币的所有可获取货币对的数据
:rtype: pandas.DataFrame

---

### `currency_time_series(base: str = 'USD', start_date: str = '2023-02-03', end_date: str = '2023-03-04', symbols: str = '', api_key: str = '') -> pandas.DataFrame`

Time-series data from currencyscoop.com
P.S. need special authority
https://currencyscoop.com/api-documentation
:param base: The base currency you would like to use for your rates
:type base: str
:param start_date: Specific date, e.g., "2020-02-03"
:type start_date: str
:param end_date: Specific date, e.g., "2020-02-03"
:type end_date: str
:param symbols: A list of currencies you will like to see the rates for. You can refer to a list all supported currencies here
:type symbols: str
:param api_key: Account -> Account Details -> API KEY (use as password in external tools)
:type api_key: str
:return: Latest data of base currency
:rtype: pandas.DataFrame

---

### `energy_carbon_bj() -> pandas.DataFrame`

北京市碳排放权电子交易平台-北京市碳排放权公开交易行情
https://www.bjets.com.cn/article/jyxx/
:return: 北京市碳排放权公开交易行情
:rtype: pandas.DataFrame

---

### `energy_carbon_domestic(symbol: str = '湖北') -> pandas.DataFrame`

碳交易网-行情信息
http://www.tanjiaoyi.com/
:param symbol: choice of {'湖北', '上海', '北京', '重庆', '广东', '天津', '深圳', '福建'}
:type symbol: str
:return: 行情信息
:rtype: pandas.DataFrame

---

### `energy_carbon_eu() -> pandas.DataFrame`

深圳碳排放交易所-国际碳情
http://www.cerx.cn/dailynewsOuter/index.htm
:return: 国际碳情每日行情数据
:rtype: pandas.DataFrame

---

### `energy_carbon_gz() -> pandas.DataFrame`

广州碳排放权交易中心-行情信息
http://www.cnemission.com/article/hqxx/
:return: 行情信息数据
:rtype: pandas.DataFrame

---

### `energy_carbon_hb() -> pandas.DataFrame`

湖北碳排放权交易中心-现货交易数据-配额-每日概况
http://www.hbets.cn/list/13.html?page=42
:return: 现货交易数据-配额-每日概况行情数据
:rtype: pandas.DataFrame

---

### `energy_carbon_sz() -> pandas.DataFrame`

深圳碳排放交易所-国内碳情
http://www.cerx.cn/dailynewsCN/index.htm
:return: 国内碳情每日行情数据
:rtype: pandas.DataFrame

---

### `energy_oil_detail(date: str = '20220517') -> pandas.DataFrame`

全国各地区的汽油和柴油油价
https://data.eastmoney.com/cjsj/oil_default.html
:param date: 可以调用 ak.energy_oil_hist() 得到可以获取油价的调整时间
:type date: str
:return: oil price at specific date
:rtype: pandas.DataFrame

---

### `energy_oil_hist() -> pandas.DataFrame`

汽柴油历史调价信息
https://data.eastmoney.com/cjsj/oil_default.html
:return: 汽柴油历史调价信息
:rtype: pandas.DataFrame

---

### `fx_c_swap_cm()`

中国外汇交易中心暨全国银行间同业拆借中心-基准-外汇市场-外汇掉期曲线-外汇掉期 C-Swap 定盘曲线
https://www.chinamoney.org.cn/chinese/bkcurvfsw
:return: 外汇掉期 C-Swap 定盘曲线
:rtype: pandas.DataFrame

---

### `fx_pair_quote() -> pandas.DataFrame`

中国外汇交易中心暨全国银行间同业拆借中心-市场数据-市场行情-债券市场行情-外币对即期报价
http://www.chinamoney.com.cn/chinese/mkdatapfx/
:return: 外币对即期报价
:rtype: pandas.DataFrame

---

### `fx_quote_baidu(symbol: str = '人民币') -> pandas.DataFrame`

百度股市通-外汇-行情榜单
https://gushitong.baidu.com/top/foreign-rmb
:param symbol: choice of {"人民币", 美元"}
:type symbol: str
:return: 外汇行情数据
:rtype: pandas.DataFrame

---

### `fx_spot_quote() -> pandas.DataFrame`

中国外汇交易中心暨全国银行间同业拆借中心-市场数据-市场行情-外汇市场行情-人民币外汇即期报价
http://www.chinamoney.com.cn/chinese/mkdatapfx/
:return: 人民币外汇即期报价
:rtype: pandas.DataFrame

---

### `fx_swap_quote() -> pandas.DataFrame`

中国外汇交易中心暨全国银行间同业拆借中心-市场数据-市场行情-债券市场行情-人民币外汇远掉报价
https://www.chinamoney.com.cn/chinese/index.html
:return: 人民币外汇远掉报价
:rtype: pandas.DataFrame

---

### `qdii_a_index_jsl(cookie: str = '') -> pandas.DataFrame`

集思录-T+0 QDII-亚洲市场-亚洲指数
https://www.jisilu.cn/data/qdii/#qdiia
:return: T+0 QDII-亚洲市场-亚洲指数
:rtype: pandas.DataFrame

---

### `qdii_e_comm_jsl(cookie: str = '') -> pandas.DataFrame`

集思录-T+0 QDII-欧美市场-商品
https://www.jisilu.cn/data/qdii/#qdiia
:return: T+0 QDII-欧美市场-商品
:rtype: pandas.DataFrame

---

### `qdii_e_index_jsl(cookie: str = '') -> pandas.DataFrame`

集思录-T+0 QDII-欧美市场-欧美指数
https://www.jisilu.cn/data/qdii/#qdiia
:return: T+0 QDII-亚洲市场
:rtype: pandas.DataFrame

---

### `qhkc_tool_foreign(url: ~AnyStr = 'https://qhkch.com/ajax/toolbox_foreign.php')`

奇货可查-工具-外盘比价
实时更新数据, 暂不能查询历史数据
:param url: str 网址
:return: 外盘比价
:rtype: pandas.DataFrame
name    base_time base_price latest_price   rate
 伦敦铜  10/08 01:00       5704       5746.5  0.745
 伦敦锌  10/08 01:00    2291.25      2305.75  0.633
 伦敦镍  10/08 01:00      17720      17372.5 -1.961
 伦敦铝  10/08 01:00     1743.5      1742.75 -0.043
 伦敦锡  10/07 15:00      16550        16290 -1.571
 伦敦铅  10/08 01:00    2181.25       2177.5 -0.172
美原油1  10/08 02:30      52.81        53.05  0.454
美原油2  10/07 23:00      53.94        53.05  -1.65
布原油1  10/08 02:30      58.41        58.67  0.445
布原油2  10/07 23:00      59.54        58.67 -1.461
 美燃油  10/07 23:00     1.9287       1.9102 -0.959
CMX金  10/08 02:30     1495.9       1496.5   0.04
CMX银  10/08 02:30     17.457       17.457      0
  美豆  10/07 23:00     916.12       915.88 -0.026
 美豆粕  10/07 23:00     302.75       302.65 -0.033
 美豆油  10/07 23:00      30.02        29.91 -0.366
 美玉米  10/07 23:00     386.38       387.88  0.388
  美糖  10/07 23:30      12.37        12.53  1.293
 美棉花  10/07 23:30      61.69        61.05 -1.037

---

### `qhkc_tool_gdp(url: ~AnyStr = 'https://qhkch.com/dist/views/toolbox/gdp.html?v=1.10.7.1')`

  奇货可查-工具-各地区经济数据
  实时更新数据, 暂不能查询历史数据
  :param url:
  :return: pandas.DataFrame
  国家  国内生产总值 国内生产总值YoY 国内生产总值QoQ  ...       预算       债务   经常账户       人口
   美国   20494     2.30%     2.00%  ...   -3.80%  106.10%  -2.40   327.17
  欧元区   13670     1.20%     0.20%  ...   -0.50%   85.10%   2.90   341.15
   中国   13608     6.20%     1.60%  ...   -4.20%   50.50%   0.40  1395.38
   日本    4971     1.00%     0.30%  ...   -3.80%  238.20%   3.50   126.25
   德国    3997     0.40%    -0.10%  ...    1.70%   60.90%   7.30    82.85
   英国    2825     1.30%    -0.20%  ...   -2.00%   84.70%  -3.90    66.19
   法国    2778     1.40%     0.30%  ...   -2.50%   98.40%  -0.30    67.19
   印度    2726     5.00%     1.00%  ...   -3.42%   68.30%  -2.30  1298.04
  意大利    2074    -0.10%     0.00%  ...   -2.10%  134.80%   2.50    60.48
   巴西    1869     1.00%     0.40%  ...   -7.10%   77.22%  -0.77   208.49
  加拿大    1709     1.60%     0.90%  ...   -0.70%   90.60%  -2.60    37.31
  俄罗斯    1658     0.90%     0.20%  ...    2.70%   13.50%   7.00   146.90
   韩国    1619     2.00%     1.00%  ...   -1.60%   36.60%   4.70    51.61
 澳大利亚    1432     1.40%     0.50%  ...   -0.60%   40.70%  -1.50    25.18
  西班牙    1426     2.00%     0.40%  ...   -2.50%   97.10%   0.90    46.66
  墨西哥    1224    -0.80%     0.00%  ...   -2.00%   46.00%  -1.80   125.33
   印尼    1042     5.05%     4.20%  ...   -1.76%   29.80%  -3.00   264.20
   荷兰     913     1.80%     0.40%  ...    1.50%   52.40%  10.80    17.12
沙特阿拉伯     782     0.50%     0.00%  ...   -9.20%   19.10%   9.20    33.41
  土耳其     767    -1.50%     1.20%  ...   -2.00%   30.40%  -3.50    82.00
   瑞士     706     0.20%     0.30%  ...    1.30%   27.70%  10.20     8.48
   台湾     589     2.40%     0.67%  ...   -1.90%   30.90%  11.60    23.58
   波兰     586     4.50%     0.80%  ...   -0.40%   48.90%  -0.70    37.98
   瑞典     551     1.00%     0.10%  ...    0.90%   38.80%   2.00    10.12
  比利时     532     1.20%     0.20%  ...   -0.70%  102.00%  -1.30    11.41
  阿根廷     519     0.60%    -0.30%  ...   -5.50%   86.20%  -5.40    44.50
   泰国     505     2.30%     0.60%  ...   -2.50%   41.80%   7.50    66.41
 委内瑞拉     482   -22.50%    -5.40%  ...  -20.00%   23.00%   6.00    31.83
  奥地利     456     1.50%     0.30%  ...    0.10%   73.80%   2.30     8.82
   伊朗     454     1.80%       NaN  ...   -3.90%   44.20%   1.30    82.10
   挪威     435    -0.70%     0.30%  ...    7.30%   36.30%   8.10     5.30
  阿联酋     414     2.20%     1.70%  ...   -1.80%   18.60%   9.10     9.60
 尼日利亚     397     1.94%     2.85%  ...   -2.80%   18.20%   2.30   195.87
  爱尔兰     376     5.80%     0.70%  ...    0.00%   64.80%   9.10     4.84
  以色列     370     3.20%     0.30%  ...   -1.90%   61.00%   1.90     8.97
   南非     366     0.90%     3.10%  ...   -4.40%   55.80%  -3.60    58.78
  新加坡     364     0.10%    -3.30%  ...    0.40%  112.20%  17.70     5.64
   香港     363     0.50%    -0.40%  ...    2.10%   38.40%   4.30     7.48
 马来西亚     354     4.90%     1.00%  ...   -3.70%   51.80%   2.30    32.40
   丹麦     351     2.60%     0.90%  ...    0.50%   34.10%   6.10     5.78
  菲律宾     331     5.50%     1.40%  ...   -3.20%   41.90%  -2.40   107.00
 哥伦比亚     330     3.00%     1.40%  ...   -3.10%   50.50%  -3.80    49.83
 巴基斯坦     313     5.20%     5.79%  ...   -6.60%   72.50%  -4.80   212.22
   智利     298     1.90%     0.80%  ...   -1.70%   25.60%  -3.10    18.75
   芬兰     276     1.20%     0.50%  ...   -0.70%   58.90%  -1.90     5.51
 孟加拉国     274     7.90%     7.90%  ...   -4.80%   27.90%  -3.60   163.70
   埃及     251     5.70%     5.40%  ...   -8.20%   90.50%  -2.40    98.00
   越南     245     7.31%     6.88%  ...   -3.50%   57.50%   3.00    94.67
捷克共和国     244     2.70%     0.70%  ...    0.90%   32.70%   0.30    10.61

---

### `reits_hist_em(symbol: str = '508097') -> pandas.DataFrame`

东方财富网-行情中心-REITs-沪深 REITs-历史行情
https://quote.eastmoney.com/sh508097.html
:param symbol: REITs 代码
:type symbol: str
:return: 沪深 REITs-历史行情
:rtype: pandas.DataFrame

---

### `reits_hist_min_em(symbol: str = '508097') -> pandas.DataFrame`

东方财富网-行情中心-REITs-沪深 REITs-历史行情
https://quote.eastmoney.com/sh508097.html
:param symbol: REITs 代码
:type symbol: str
:return: 沪深 REITs-历史行情
:rtype: pandas.DataFrame

---

### `reits_realtime_em() -> pandas.DataFrame`

东方财富网-行情中心-REITs-沪深 REITs
https://quote.eastmoney.com/center/gridlist.html#fund_reits_all
:return: 沪深 REITs-实时行情
:rtype: pandas.DataFrame

---

### `spot_corn_price_soozhu() -> pandas.DataFrame`

搜猪-生猪大数据-全国玉米价格走势
https://www.soozhu.com/price/data/center/
:return: 全国玉米价格走势
:rtype: pandas.DataFrame

---

### `spot_golden_benchmark_sge() -> pandas.DataFrame`

上海黄金交易所-数据资讯-上海金基准价-历史数据
https://www.sge.com.cn/sjzx/jzj
:return: 历史数据
:rtype: pandas.DataFrame

---

### `spot_goods(symbol: str = '波罗的海干散货指数') -> pandas.DataFrame`

新浪财经-商品现货价格指数
https://finance.sina.com.cn/futuremarket/spotprice.shtml#titlePos_0
:param symbol: choice of {"波罗的海干散货指数", "钢坯价格指数", "澳大利亚粉矿价格"}
:type symbol: str
:return: 商品现货价格指数
:rtype: pandas.DataFrame

---

### `spot_hist_sge(symbol: str = 'Au99.99') -> pandas.DataFrame`

上海黄金交易所-数据资讯-行情走势-历史数据
https://www.sge.com.cn/sjzx/mrhq
:param symbol: choice of {'Au99.99', 'Au99.95', 'Au100g', 'Pt99.95', 'Ag(T+D)', 'Au(T+D)',
'mAu(T+D)', 'Au(T+N1)', 'Au(T+N2)', 'Ag99.99', 'iAu99.99', 'Au99.5', 'iAu100g', 'iAu99.5',
'PGC30g', 'NYAuTN06', 'NYAuTN12'}; 可以通过 ak.spot_symbol_table_sge() 获取品种表
:type symbol: str
:return: 历史数据
:rtype: pandas.DataFrame

---

### `spot_hog_crossbred_soozhu() -> pandas.DataFrame`

搜猪-生猪大数据-全国后备二元母猪
https://www.soozhu.com/price/data/center/
:return: 全国后备二元母猪
:rtype: pandas.DataFrame

---

### `spot_hog_lean_price_soozhu() -> pandas.DataFrame`

搜猪-生猪大数据-全国瘦肉型肉猪
https://www.soozhu.com/price/data/center/
:return: 全国瘦肉型肉猪
:rtype: pandas.DataFrame

---

### `spot_hog_soozhu() -> pandas.DataFrame`

搜猪-生猪大数据-各省均价实时排行榜
https://www.soozhu.com/price/data/center/
:return: 各省均价实时排行榜
:rtype: pandas.DataFrame

---

### `spot_hog_three_way_soozhu() -> pandas.DataFrame`

搜猪-生猪大数据-全国三元仔猪
https://www.soozhu.com/price/data/center/
:return: 全国三元仔猪
:rtype: pandas.DataFrame

---

### `spot_hog_year_trend_soozhu() -> pandas.DataFrame`

搜猪-生猪大数据-今年以来全国出栏均价走势
https://www.soozhu.com/price/data/center/
:return: 今年以来全国出栏均价走势
:rtype: pandas.DataFrame

---

### `spot_mixed_feed_soozhu() -> pandas.DataFrame`

搜猪-生猪大数据-全国育肥猪合料（含自配料）半月走势
https://www.soozhu.com/price/data/center/
:return: 全国育肥猪合料（含自配料）半月走势
:rtype: pandas.DataFrame

---

### `spot_price_qh(symbol: str = '螺纹钢') -> pandas.DataFrame`

99 期货-数据-期现-现货走势
https://www.99qh.com/data/spotTrend
:param symbol: 品种名称
:type symbol: str
:return: 现货走势
:rtype: pandas.DataFrame

---

### `spot_price_table_qh() -> pandas.DataFrame`

99 期货-数据-期现-交易所与品种对照表
https://www.99qh.com/data/spotTrend
:return: 交易所与品种对照表
:rtype: pandas.DataFrame

---

### `spot_quotations_sge(symbol: str = 'Au99.99') -> pandas.DataFrame`

上海黄金交易所-实时行情数据
https://www.sge.com.cn/
https://www.sge.com.cn/graph/quotations
:param symbol: choice of {'Au99.99', 'Au99.95', 'Au100g', 'Pt99.95', 'Ag(T+D)', 'Au(T+D)',
'mAu(T+D)', 'Au(T+N1)', 'Au(T+N2)', 'Ag99.99', 'iAu99.99', 'Au99.5', 'iAu100g',
'iAu99.5', 'PGC30g', 'NYAuTN06', 'NYAuTN12'}; 可以通过 ak.spot_symbol_table_sge() 获取品种表
:type symbol: str
:return: 行情数据
:rtype: pandas.DataFrame

---

### `spot_silver_benchmark_sge() -> pandas.DataFrame`

上海黄金交易所-数据资讯-上海银基准价-历史数据
https://www.sge.com.cn/sjzx/mrhq
:return: 历史数据
:rtype: pandas.DataFrame

---

### `spot_soybean_price_soozhu() -> pandas.DataFrame`

搜猪-生猪大数据-全国豆粕价格走势
https://www.soozhu.com/price/data/center/
:return: 全国豆粕价格走势
:rtype: pandas.DataFrame

---

### `spot_symbol_table_sge() -> pandas.DataFrame`

上海黄金交易所-数据资讯-行情走势-品种表
https://www.sge.com.cn/sjzx/mrhq
:return: 品种表
:rtype: pandas.DataFrame

---

### `sw_index_first_info() -> pandas.DataFrame`

乐咕乐股-申万一级-分类
https://legulegu.com/stockdata/sw-industry-overview#level1
:return: 分类
:rtype: pandas.DataFrame

---

### `sw_index_second_info() -> pandas.DataFrame`

乐咕乐股-申万二级-分类
https://legulegu.com/stockdata/sw-industry-overview#level1
:return: 分类
:rtype: pandas.DataFrame

---

### `sw_index_third_cons(symbol: str = '801120.SI') -> pandas.DataFrame`

乐咕乐股-申万三级-行业成份
https://legulegu.com/stockdata/index-composition?industryCode=801120.SI
:param symbol: 三级行业的行业代码
:type symbol: str
:return: 行业成份
:rtype: pandas.DataFrame

---

### `sw_index_third_info() -> pandas.DataFrame`

乐咕乐股-申万三级-分类
https://legulegu.com/stockdata/sw-industry-overview#level1
:return: 分类
:rtype: pandas.DataFrame

---

