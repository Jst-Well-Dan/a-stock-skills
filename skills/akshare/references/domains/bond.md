# Bond 域接口详情

> 共 42 个接口，覆盖国债/可转债/企业债 行情、收益率曲线、发行数据、质押回购等。

## 接口列表

### `bond_buy_back_hist_em(symbol: str = '204001')`

东方财富网-行情中心-债券市场-质押式回购-历史数据
https://quote.eastmoney.com/center/gridlist.html#bond_sh_buyback
:param symbol: 质押式回购代码
:type symbol: str
:return: 历史数据
:rtype: pandas.DataFrame

---

### `bond_cash_summary_sse(date: str = '20210111') -> pandas.DataFrame`

上登债券信息网-市场数据-市场统计-市场概览-债券现券市场概览
http://bond.sse.com.cn/data/statistics/overview/bondow/
:param date: 指定日期
:type date: str
:return: 债券成交概览
:rtype: pandas.DataFrame

---

### `bond_cb_adj_logs_jsl(symbol: str = '128013') -> pandas.DataFrame`

集思录-可转债转股价-调整记录
https://www.jisilu.cn/data/cbnew/#cb
:param symbol: 可转债代码
:type symbol: str
:return: 转股价调整记录
:rtype: pandas.DataFrame

---

### `bond_cb_index_jsl() -> pandas.DataFrame`

首页-可转债-集思录可转债等权指数
https://www.jisilu.cn/web/data/cb/index
:return: 集思录可转债等权指数
:rtype: pandas.DataFrame

---

### `bond_cb_jsl(cookie: str = None) -> pandas.DataFrame`

集思录可转债
https://www.jisilu.cn/data/cbnew/#cb
:param cookie: 输入获取到的游览器 cookie
:type cookie: str
:return: 集思录可转债
:rtype: pandas.DataFrame

---

### `bond_cb_profile_sina(symbol: str = 'sz128039') -> pandas.DataFrame`

新浪财经-债券-可转债-详情资料
https://money.finance.sina.com.cn/bond/info/sz128039.html
:param symbol: 带市场标识的转债代码
:type symbol: str
:return: 可转债-详情资料
:rtype: pandas.DataFrame

---

### `bond_cb_redeem_jsl() -> pandas.DataFrame`

集思录可转债-强赎
https://www.jisilu.cn/data/cbnew/#redeem
:return: 集思录可转债-强赎
:rtype: pandas.DataFrame

---

### `bond_cb_summary_sina(symbol: str = 'sh155255') -> pandas.DataFrame`

新浪财经-债券-可转债-债券概况
https://money.finance.sina.com.cn/bond/quotes/sh155255.html
:param symbol: 带市场标识的转债代码
:type symbol: str
:return: 可转债-债券概况
:rtype: pandas.DataFrame

---

### `bond_china_close_return(symbol: str = '国债', period: str = '1', start_date: str = '20231101', end_date: str = '20231101') -> pandas.DataFrame`

收盘收益率曲线历史数据
https://www.chinamoney.com.cn/chinese/bkcurvclosedyhis/?bondType=CYCC000&reference=1
:param symbol: 需要获取的指标
:type period: choice of {'0.1', '0.5', '1'}
:param period: 期限间隔
:type symbol: str
:param start_date: 开始日期, 结束日期和开始日期不要超过 1 个月
:type start_date: str
:param end_date: 结束日期, 结束日期和开始日期不要超过 1 个月
:type end_date: str
:return: 收盘收益率曲线历史数据
:rtype: pandas.DataFrame

---

### `bond_china_close_return_map() -> pandas.DataFrame`

收盘收益率曲线历史数据
https://www.chinamoney.com.cn/chinese/bkcurvclosedyhis/?bondType=CYCC000&reference=1
:return: 收盘收益率曲线历史数据
:rtype: pandas.DataFrame

---

### `bond_china_yield(start_date: str = '20200204', end_date: str = '20210124') -> pandas.DataFrame`

中国债券信息网-国债及其他债券收益率曲线
https://www.chinabond.com.cn/
https://yield.chinabond.com.cn/cbweb-pbc-web/pbc/historyQuery?startDate=2019-02-07&endDate=2020-02-04&gjqx=0&qxId=ycqx&locale=cn_ZH
注意: end_date - start_date 应该小于一年
:param start_date: 需要查询的日期, 返回在该日期之后一年内的数据
:type start_date: str
:param end_date: 需要查询的日期, 返回在该日期之前一年内的数据
:type end_date: str
:return: 返回在指定日期之间之前一年内的数据
:rtype: pandas.DataFrame

---

### `bond_composite_index_cbond(indicator: str = '财富', period: str = '总值') -> pandas.DataFrame`

中国债券信息网-中债指数-中债指数族系-总指数-综合类指数-中债-综合指数
https://yield.chinabond.com.cn/cbweb-mn/indices/single_index_query
:param indicator: choice of {"全价", "净价", "财富", "平均市值法久期", "平均现金流法久期", "平均市值法凸性", "平均现金流法凸性", "平均现金流法到期收益率", "平均市值法到期收益率", "平均基点价值", "平均待偿期", "平均派息率", "指数上日总市值", "财富指数涨跌幅", "全价指数涨跌幅", "净价指数涨跌幅", "现券结算量"}
:type indicator: str
:param period: choice of {"总值", "1年以下", "1-3年", "3-5年", "5-7年", "7-10年", "10年以上", "0-3个月", "3-6个月", "6-9个月", "9-12个月", "0-6个月", "6-12个月"}
:type period: str
:return: 新综合指数
:rtype: pandas.DataFrame

---

### `bond_corporate_issue_cninfo(start_date: str = '20210911', end_date: str = '20211110') -> pandas.DataFrame`

巨潮资讯-数据中心-专题统计-债券报表-债券发行-企业债发行
http://webapi.cninfo.com.cn/#/thematicStatistics
:param start_date: 开始统计时间
:type start_date: str
:param end_date: 开始统计时间
:type end_date: str
:return: 企业债发行
:rtype: pandas.DataFrame

---

### `bond_cov_comparison() -> pandas.DataFrame`

东方财富网-行情中心-债券市场-可转债比价表
https://quote.eastmoney.com/center/fullscreenlist.html#convertible_comparison
:return: 可转债比价表数据
:rtype: pandas.DataFrame

---

### `bond_cov_issue_cninfo(start_date: str = '20210913', end_date: str = '20211112') -> pandas.DataFrame`

巨潮资讯-数据中心-专题统计-债券报表-债券发行-可转债发行
http://webapi.cninfo.com.cn/#/thematicStatistics
:param start_date: 开始统计时间
:type start_date: str
:param end_date: 开始统计时间
:type end_date: str
:return: 可转债发行
:rtype: pandas.DataFrame

---

### `bond_cov_stock_issue_cninfo() -> pandas.DataFrame`

巨潮资讯-数据中心-专题统计-债券报表-债券发行-可转债转股
http://webapi.cninfo.com.cn/#/thematicStatistics
:return: 可转债转股
:rtype: pandas.DataFrame

---

### `bond_deal_summary_sse(date: str = '20210104') -> pandas.DataFrame`

上登债券信息网-市场数据-市场统计-市场概览-债券成交概览
http://bond.sse.com.cn/data/statistics/overview/turnover/
:param date: 指定日期
:type date: str
:return: 债券成交概览
:rtype: pandas.DataFrame

---

### `bond_debt_nafmii(page: str = '1') -> pandas.DataFrame`

中国银行间市场交易商协会-非金融企业债务融资工具注册信息系统
http://zhuce.nafmii.org.cn/fans/publicQuery/manager
:param page: 输入数字页码
:type page: int
:return: 指定 sector 和 indicator 的数据
:rtype: pandas.DataFrame

---

### `bond_gb_us_sina(symbol: str = '美国10年期国债') -> pandas.DataFrame`

新浪财经-债券-美国国债收益率行情数据
https://stock.finance.sina.com.cn/forex/globalbd/cn10yt.html
:param symbol: choice of {"美国1月期国债", "美国2月期国债", "美国3月期国债", "美国4月期国债", "美国6月期国债", "美国1年期国债", "美国2年期国债", "美国3年期国债", "美国5年期国债", "美国7年期国债", "美国10年期国债", "美国20年期国债", "美国30年期国债"}
:type symbol: str
:return: 美国国债收益率行情数据
:rtype: pandas.DataFrame

---

### `bond_gb_zh_sina(symbol: str = '中国10年期国债') -> pandas.DataFrame`

新浪财经-债券-中国国债收益率行情数据
https://stock.finance.sina.com.cn/forex/globalbd/cn10yt.html
:param symbol: choice of {"中国1年期国债", "中国2年期国债", "中国3年期国债", "中国5年期国债", "中国7年期国债", "中国10年期国债", "中国15年期国债", "中国20年期国债", "中国30年期国债"}
:type symbol: str
:return: 中国国债收益率行情数据
:rtype: pandas.DataFrame

---

### `bond_info_cm(bond_name: str = '', bond_code: str = '', bond_issue: str = '', bond_type: str = '', coupon_type: str = '', issue_year: str = '', underwriter: str = '', grade: str = '') -> pandas.DataFrame`

中国外汇交易中心暨全国银行间同业拆借中心-数据-债券信息-信息查询
https://www.chinamoney.com.cn/chinese/scsjzqxx/
:param bond_name: 债券名称
:type bond_name: str
:param bond_code: 债券代码
:type bond_code: str
:param bond_issue: 发行人/受托机构
:type bond_issue: str
:param bond_type: 债券类型
:type bond_type: str
:param coupon_type: 息票类型
:type coupon_type: str
:param issue_year: 发行年份
:type issue_year: str
:param underwriter: 主承销商
:type underwriter: str
:param grade: 评级等级
:type grade: str
:return: 信息查询结果
:rtype: pandas.DataFrame

---

### `bond_info_cm_query(symbol: str = '评级等级') -> pandas.DataFrame`

中国外汇交易中心暨全国银行间同业拆借中心-查询相关指标的参数
https://www.chinamoney.com.cn/chinese/scsjzqxx/
:param symbol: choice of {"主承销商", "债券类型", "息票类型", "发行年份", "评级等级"}
:type symbol: str
:return: 查询相关指标的参数
:rtype: pandas.DataFrame

---

### `bond_info_detail_cm(symbol: str = '淮安农商行CDSD2022021012') -> pandas.DataFrame`

中国外汇交易中心暨全国银行间同业拆借中心-数据-债券信息-信息查询-债券详情
https://www.chinamoney.com.cn/chinese/zqjc/?bondDefinedCode=egfjh08154
:param symbol: 债券简称
:type symbol: str
:return: 债券详情
:rtype: pandas.DataFrame

---

### `bond_local_government_issue_cninfo(start_date: str = '20210911', end_date: str = '20211110') -> pandas.DataFrame`

巨潮资讯-数据中心-专题统计-债券报表-债券发行-地方债发行
http://webapi.cninfo.com.cn/#/thematicStatistics
:param start_date: 开始统计时间
:type start_date: str
:param end_date: 开始统计时间
:type end_date: str
:return: 地方债发行
:rtype: pandas.DataFrame

---

### `bond_new_composite_index_cbond(indicator: str = '财富', period: str = '总值') -> pandas.DataFrame`

中国债券信息网-中债指数-中债指数族系-总指数-综合类指数-中债-新综合指数
https://yield.chinabond.com.cn/cbweb-mn/indices/single_index_query
:param indicator: choice of {"全价", "净价", "财富", "平均市值法久期", "平均现金流法久期", "平均市值法凸性", "平均现金流法凸性", "平均现金流法到期收益率", "平均市值法到期收益率", "平均基点价值", "平均待偿期", "平均派息率", "指数上日总市值", "财富指数涨跌幅", "全价指数涨跌幅", "净价指数涨跌幅", "现券结算量"}
:type indicator: str
:param period: choice of {"总值", "1年以下", "1-3年", "3-5年", "5-7年", "7-10年", "10年以上", "0-3个月", "3-6个月", "6-9个月", "9-12个月", "0-6个月", "6-12个月"}
:type period: str
:return: 新综合指数
:rtype: pandas.DataFrame

---

### `bond_sh_buy_back_em() -> pandas.DataFrame`

东方财富网-行情中心-债券市场-上证质押式回购
https://quote.eastmoney.com/center/gridlist.html#bond_sh_buyback
:return: 上证质押式回购
:rtype: pandas.DataFrame

---

### `bond_spot_deal() -> pandas.DataFrame`

中国外汇交易中心暨全国银行间同业拆借中心-市场数据-债券市场行情-现券市场成交行情
https://www.chinamoney.com.cn/chinese/mkdatabond/
:return: 现券市场成交行情
:rtype: pandas.DataFrame

---

### `bond_spot_quote() -> pandas.DataFrame`

中国外汇交易中心暨全国银行间同业拆借中心-市场数据-债券市场行情-现券市场做市报价
https://www.chinamoney.com.cn/chinese/mkdatabond/
:return: 现券市场做市报价
:rtype: pandas.DataFrame

---

### `bond_sz_buy_back_em() -> pandas.DataFrame`

东方财富网-行情中心-债券市场-深证质押式回购
https://quote.eastmoney.com/center/gridlist.html#bond_sz_buyback
:return: 深证质押式回购
:rtype: pandas.DataFrame

---

### `bond_treasure_issue_cninfo(start_date: str = '20210910', end_date: str = '20211109') -> pandas.DataFrame`

巨潮资讯-数据中心-专题统计-债券报表-债券发行-国债发行
http://webapi.cninfo.com.cn/#/thematicStatistics
:param start_date: 开始统计时间
:type start_date: str
:param end_date: 结束统计数据
:type end_date: str
:return: 国债发行
:rtype: pandas.DataFrame

---

### `bond_zh_cov() -> pandas.DataFrame`

东方财富网-数据中心-新股数据-可转债数据
https://data.eastmoney.com/kzz/default.html
:return: 可转债数据
:rtype: pandas.DataFrame

---

### `bond_zh_cov_info(symbol: str = '123121', indicator: str = '基本信息') -> pandas.DataFrame`

https://data.eastmoney.com/kzz/detail/123121.html
东方财富网-数据中心-新股数据-可转债详情
:param symbol: 可转债代码
:type symbol: str
:param indicator: choice of {"基本信息", "中签号", "筹资用途", "重要日期"}
:type indicator: str
:return: 可转债详情
:rtype: pandas.DataFrame

---

### `bond_zh_cov_info_ths() -> pandas.DataFrame`

同花顺-数据中心-可转债
https://data.10jqka.com.cn/ipo/bond/
:return: 可转债行情
:rtype: pandas.DataFrame

---

### `bond_zh_cov_value_analysis(symbol: str = '113527') -> pandas.DataFrame`

https://data.eastmoney.com/kzz/detail/113527.html
东方财富网-数据中心-新股数据-可转债数据-价值分析-溢价率分析
:param symbol: 可转债代码
:type symbol: str
:return: 可转债价值分析
:rtype: pandas.DataFrame

---

### `bond_zh_hs_cov_daily(symbol: str = 'sh010107') -> pandas.DataFrame`

新浪财经-债券-沪深可转债的历史行情数据, 大量抓取容易封 IP
https://vip.stock.finance.sina.com.cn/mkt/#hskzz_z
:param symbol: 沪深可转债代码; e.g., sh010107
:type symbol: str
:return: 指定沪深可转债代码的日 K 线数据
:rtype: pandas.DataFrame

---

### `bond_zh_hs_cov_min(symbol: str = 'sz128039', period: str = '15', adjust: str = '', start_date: str = '1979-09-01 09:32:00', end_date: str = '2222-01-01 09:32:00') -> pandas.DataFrame`

东方财富网-可转债-分时行情
https://quote.eastmoney.com/concept/sz128039.html
:param symbol: 转债代码
:type symbol: str
:param period: choice of {'1', '5', '15', '30', '60'}
:type period: str
:param adjust: choice of {'', 'qfq', 'hfq'}
:type adjust: str
:param start_date: 开始日期
:type start_date: str
:param end_date: 结束日期
:type end_date: str
:return: 分时行情
:rtype: pandas.DataFrame

---

### `bond_zh_hs_cov_pre_min(symbol: str = 'sh113570') -> pandas.DataFrame`

东方财富网-可转债-分时行情-盘前
https://quote.eastmoney.com/concept/sz128039.html
:param symbol: 转债代码
:type symbol: str
:return: 分时行情-盘前
:rtype: pandas.DataFrame

---

### `bond_zh_hs_cov_spot() -> pandas.DataFrame`

新浪财经-债券-沪深可转债的实时行情数据; 大量抓取容易封IP
https://vip.stock.finance.sina.com.cn/mkt/#hskzz_z
:return: 所有沪深可转债在当前时刻的实时行情数据
:rtype: pandas.DataFrame

---

### `bond_zh_hs_daily(symbol: str = 'sh010107') -> pandas.DataFrame`

新浪财经-债券-沪深债券-历史行情数据, 大量抓取容易封 IP
https://vip.stock.finance.sina.com.cn/mkt/#hs_z
:param symbol: 沪深债券代码; e.g., sh010107
:type symbol: str
:return: 指定沪深债券代码的日 K 线数据
:rtype: pandas.DataFrame

---

### `bond_zh_hs_spot(start_page: str = '1', end_page: str = '10') -> pandas.DataFrame`

新浪财经-债券-沪深债券-实时行情数据, 大量抓取容易封IP
https://vip.stock.finance.sina.com.cn/mkt/#hs_z
:param start_page: 分页起始页
:type start_page: str
:param end_page: 分页结束页
:type end_page: str
:return: 所有沪深债券在当前时刻的实时行情数据
:rtype: pandas.DataFrame

---

### `bond_zh_us_rate(start_date: str = '19901219') -> pandas.DataFrame`

东方财富网-数据中心-经济数据-中美国债收益率
https://data.eastmoney.com/cjsj/zmgzsyl.html
:param start_date: 开始统计时间
:type start_date: str
:return: 中美国债收益率
:rtype: pandas.DataFrame

---

