# Index 域接口详情

> 共 80 个接口，覆盖申万/中证/国证指数、全球指数、波动率指数(QVIX)、财新PMI等。

## 接口列表

### `index_ai_cx() -> pandas.DataFrame`

财新数据-指数报告-AI策略指数
https://yun.ccxe.com.cn/indices/ai
:return: AI策略指数
:rtype: pandas.DataFrame

---

### `index_all_cni() -> pandas.DataFrame`

国证指数-最近交易日的所有指数
https://www.cnindex.com.cn/zh_indices/sese/index.html?act_menu=1&index_type=-1
:return: 国证指数-所有指数
:rtype: pandas.DataFrame

---

### `index_analysis_daily_sw(symbol: str = '市场表征', start_date: str = '20221103', end_date: str = '20221103') -> pandas.DataFrame`

申万宏源研究-指数分析
https://www.swsresearch.com/institute_sw/allIndex/analysisIndex
:param symbol: choice of {"市场表征", "一级行业", "二级行业", "风格指数"}
:type symbol: str
:param start_date: 开始日期
:type start_date: str
:param end_date: 结束日期
:type end_date: str
:return: 指数分析
:rtype: pandas.DataFrame

---

### `index_analysis_monthly_sw(symbol: str = '市场表征', date: str = '20221031') -> pandas.DataFrame`

申万宏源研究-指数分析-月报告
https://www.swsresearch.com/institute_sw/allIndex/analysisIndex
:param symbol: choice of {"市场表征", "一级行业", "二级行业", "风格指数"}
:type symbol: str
:param date: 查询日期; 通过调用 ak.index_analysis_week_month_sw() 接口获取
:type date: str
:return: 指数分析
:rtype: pandas.DataFrame

---

### `index_analysis_week_month_sw(symbol: str = 'month') -> pandas.DataFrame`

申万宏源研究-周/月报表-日期序列
https://www.swsresearch.com/institute_sw/allIndex/analysisIndex
:param symbol: choice of {"week", "month"}
:type symbol: str
:return: 日期序列
:rtype: pandas.DataFrame

---

### `index_analysis_weekly_sw(symbol: str = '市场表征', date: str = '20221104') -> pandas.DataFrame`

申万宏源研究-指数分析-周报告
https://www.swsresearch.com/institute_sw/allIndex/analysisIndex
:param symbol: choice of {"市场表征", "一级行业", "二级行业", "风格指数"}
:type symbol: str
:param date: 查询日期; 通过调用 ak.index_analysis_week_month_sw(date="20221104") 接口获取
:type date: str
:return: 指数分析
:rtype: pandas.DataFrame

---

### `index_awpr_cx() -> pandas.DataFrame`

财新数据-指数报告-新经济入职工资溢价水平
https://yun.ccxe.com.cn/indices/nei
:return: 新经济入职工资溢价水平
:rtype: pandas.DataFrame

---

### `index_bei_cx() -> pandas.DataFrame`

财新数据-指数报告-基石经济指数
https://yun.ccxe.com.cn/indices/bei
:return: 基石经济指数
:rtype: pandas.DataFrame

---

### `index_bi_cx() -> pandas.DataFrame`

财新数据-指数报告-基础指数
https://yun.ccxe.com.cn/indices/dei
:return: 基础指数
:rtype: pandas.DataFrame

---

### `index_bloomberg_billionaires() -> pandas.DataFrame`

Bloomberg Billionaires Index
https://www.bloomberg.com/billionaires/
:return: 彭博亿万富豪指数
:rtype: pandas.DataFrame

---

### `index_bloomberg_billionaires_hist(year: str = '2021') -> pandas.DataFrame`

Bloomberg Billionaires Index
https://stats.areppim.com/stats/links_billionairexlists.htm
:param year: choice of {"2021", "2019", "2018", ...}
:type year: str
:return: 彭博亿万富豪指数历史数据
:rtype: pandas.DataFrame

---

### `index_cci_cx() -> pandas.DataFrame`

财新数据-指数报告-大宗商品指数
https://yun.ccxe.com.cn/indices/nei
:return: 大宗商品指数
:rtype: pandas.DataFrame

---

### `index_ci_cx() -> pandas.DataFrame`

财新数据-指数报告-资本投入指数
https://yun.ccxe.com.cn/indices/nei
:return: 资本投入指数
:rtype: pandas.DataFrame

---

### `index_code_id_map_em() -> dict`

东方财富-股票和市场代码
https://quote.eastmoney.com/center/gridlist.html#hs_a_board
:return: 股票和市场代码
:rtype: dict

---

### `index_component_sw(symbol: str = '801001') -> pandas.DataFrame`

申万宏源研究-指数发布-指数详情-成分股
https://www.swsresearch.com/institute_sw/allIndex/releasedIndex/releasedetail?code=801001&name=%E7%94%B3%E4%B8%8750
:param symbol: 指数代码
:type symbol: str
:return: 成分股
:rtype: pandas.DataFrame

---

### `index_csindex_all() -> pandas.DataFrame`

中证指数网站-指数列表
https://www.csindex.com.cn/#/indices/family/list?index_series=1
Note: 但是不知道数据更新时间
:return: 最新指数的列表,
:rtype: pandas.DataFrame

---

### `index_dei_cx() -> pandas.DataFrame`

财新数据-指数报告-数字经济指数
https://yun.ccxe.com.cn/indices/dei
:return: 数字经济指数
:rtype: pandas.DataFrame

---

### `index_detail_cni(symbol: str = '399001') -> pandas.DataFrame`

国证指数-样本详情-指定日期的样本成份
https://www.cnindex.com.cn/module/index-detail.html?act_menu=1&indexCode=399001
:param symbol: 指数代码
:type symbol: str
:return: 指定日期的样本成份
:rtype: pandas.DataFrame

---

### `index_detail_hist_adjust_cni(symbol: str = '399005') -> pandas.DataFrame`

国证指数-样本详情-历史调样
http://www.cnindex.com.cn/module/index-detail.html?act_menu=1&indexCode=399005
:param symbol: 指数代码
:type symbol: str
:return: 历史调样
:rtype: pandas.DataFrame

---

### `index_detail_hist_cni(symbol: str = '399001') -> pandas.DataFrame`

国证指数-样本详情-历史样本
https://www.cnindex.com.cn/module/index-detail.html?act_menu=1&indexCode=399001
:param symbol: 指数代码; "399001"
:type symbol: str
:return: 历史样本
:rtype: pandas.DataFrame

---

### `index_eri(symbol: str = '月度') -> pandas.DataFrame`

浙江省排污权交易指数
https://zs.zjpwq.net
:param symbol: choice of {"月度", "季度"}
:type symbol: str
:return: 浙江省排污权交易指数
:rtype: pandas.DataFrame

---

### `index_fi_cx() -> pandas.DataFrame`

财新数据-指数报告-融合指数
https://yun.ccxe.com.cn/indices/dei
:return: 融合指数
:rtype: pandas.DataFrame

---

### `index_global_hist_em(symbol: str = '美元指数') -> pandas.DataFrame`

东方财富网-行情中心-全球指数-历史行情数据
https://quote.eastmoney.com/gb/zsUDI.html
:param symbol: 指数名称；可以通过 ak.index_global_spot_em() 获取
:type symbol: str
:return: 历史行情数据
:rtype: pandas.DataFrame

---

### `index_global_hist_sina(symbol: str = 'OMX') -> pandas.DataFrame`

新浪财经-行情中心-环球市场-历史行情
https://finance.sina.com.cn/stock/globalindex/quotes/UKX
:param symbol: 指数名称；可以通过 ak.index_global_name_table() 获取
:type symbol: str
:return: 环球市场历史行情
:rtype: pandas.DataFrame

---

### `index_global_name_table() -> pandas.DataFrame`

新浪财经-行情中心-环球市场-名称代码映射表
https://finance.sina.com.cn/stock/globalindex/quotes/UKX
:return: 名称代码映射表
:rtype: pandas.DataFrame

---

### `index_global_spot_em() -> pandas.DataFrame`

东方财富网-行情中心-全球指数-实时行情数据
https://quote.eastmoney.com/center/gridlist.html#global_qtzs
:return: 实时行情数据
:rtype: pandas.DataFrame

---

### `index_hist_cni(symbol: str = '399001', start_date: str = '20230114', end_date: str = '20240114') -> pandas.DataFrame`

指数历史行情数据
http://www.cnindex.com.cn/module/index-detail.html?act_menu=1&indexCode=399001
:param symbol: 指数代码
:type symbol: str
:param start_date: 开始时间
:type start_date: str
:param end_date: 结束时间
:type end_date: str
:return: 指数历史行情数据
:rtype: pandas.DataFrame

---

### `index_hist_fund_sw(symbol: str = '807200', period: str = 'day') -> pandas.DataFrame`

申万宏源研究-申万指数-指数发布-基金指数-历史行情
https://www.swsresearch.com/institute_sw/allIndex/releasedIndex/fundDetail?code=807100
:param symbol: 基金指数代码
:type symbol: str
:param period: 周期
:type period: str
:return: 历史行情
:rtype: pandas.DataFrame

---

### `index_hist_sw(symbol: str = '801030', period: str = 'day') -> pandas.DataFrame`

申万宏源研究-指数发布-指数详情-指数历史数据
https://www.swsresearch.com/institute_sw/allIndex/releasedIndex/releasedetail?code=801001&name=%E7%94%B3%E4%B8%8750
:param symbol: 指数代码
:type symbol: str
:param period: choice of {"day", "week", "month"}
:type period: str
:return: 指数历史数据
:rtype: pandas.DataFrame

---

### `index_hog_spot_price() -> pandas.DataFrame`

行情宝-生猪市场价格指数
https://hqb.nxin.com/pigindex/index.shtml
:return: 生猪市场价格指数
:rtype: pandas.DataFrame

---

### `index_ii_cx() -> pandas.DataFrame`

财新数据-指数报告-产业指数
https://yun.ccxe.com.cn/indices/dei
:return: 产业指数
:rtype: pandas.DataFrame

---

### `index_inner_quote_sugar_msweet() -> pandas.DataFrame`

沐甜科技数据中心-配额内进口糖估算指数
https://www.msweet.com.cn/mtkj/sjzx13/index.html
:return: 配额内进口糖估算指数
:rtype: pandas.DataFrame

---

### `index_kq_fashion(symbol: str = '时尚创意指数') -> pandas.DataFrame`

柯桥时尚指数
http://ss.kqindex.cn:9559/rinder_web_kqsszs/index/index_page.do
:param symbol: choice of {'柯桥时尚指数', '时尚创意指数', '时尚设计人才数', '新花型推出数', '创意产品成交数', '创意企业数量', '时尚活跃度指数', '电商运行数', '时尚平台拓展数', '新产品销售额占比', '企业合作占比', '品牌传播费用', '时尚推广度指数', '国际交流合作次数', '企业参展次数', '外商驻点数量变化', '时尚评价指数'}
:type symbol: str
:return: 柯桥时尚指数及其子项数据
:rtype: pandas.DataFrame

---

### `index_kq_fz(symbol: str = '价格指数') -> pandas.DataFrame`

中国柯桥纺织指数
http://www.kqindex.cn/flzs/jiage
:param symbol: choice of {'价格指数', '景气指数', '外贸指数'}
:type symbol: str
:return: 中国柯桥纺织指数
:rtype: pandas.DataFrame

---

### `index_li_cx() -> pandas.DataFrame`

财新数据-指数报告-劳动力投入指数
https://yun.ccxe.com.cn/indices/nei
:return: 劳动力投入指数
:rtype: pandas.DataFrame

---

### `index_min_sw(symbol: str = '801001') -> pandas.DataFrame`

申万宏源研究-指数发布-指数详情-指数分时数据
https://www.swsresearch.com/institute_sw/allIndex/releasedIndex/releasedetail?code=801001&name=%E7%94%B3%E4%B8%8750
:param symbol: 指数代码
:type symbol: str
:return: 指数分时数据
:rtype: pandas.DataFrame

---

### `index_neaw_cx() -> pandas.DataFrame`

财新数据-指数报告-新经济行业入职平均工资水平
https://yun.ccxe.com.cn/indices/nei
:return: 新经济行业入职平均工资水平
:rtype: pandas.DataFrame

---

### `index_neei_cx() -> pandas.DataFrame`

财新数据-指数报告-新动能指数
https://yun.ccxe.com.cn/indices/neei
:return: 新动能指数
:rtype: pandas.DataFrame

---

### `index_nei_cx() -> pandas.DataFrame`

财新数据-指数报告-中国新经济指数
https://yun.ccxe.com.cn/indices/nei
:return: 中国新经济指数
:rtype: pandas.DataFrame

---

### `index_news_sentiment_scope() -> pandas.DataFrame`

数库-A股新闻情绪指数
https://www.chinascope.com/reasearch.html
:return: A股新闻情绪指数
:rtype: pandas.DataFrame

---

### `index_option_1000index_min_qvix() -> pandas.DataFrame`

中证1000股指 期权波动率指数 QVIX-分时
http://1.optbbs.com/s/vix.shtml?Index1000
:return: 中证1000股指 期权波动率指数 QVIX-分时
:rtype: pandas.DataFrame

---

### `index_option_1000index_qvix() -> pandas.DataFrame`

中证1000股指 期权波动率指数 QVIX
http://1.optbbs.com/s/vix.shtml?Index1000
:return: 中证1000股指 期权波动率指数 QVIX
:rtype: pandas.DataFrame

---

### `index_option_100etf_min_qvix() -> pandas.DataFrame`

深证100ETF 期权波动率指数 QVIX-分时
http://1.optbbs.com/s/vix.shtml?100ETF
:return: 深证100ETF 期权波动率指数 QVIX-分时
:rtype: pandas.DataFrame

---

### `index_option_100etf_qvix() -> pandas.DataFrame`

深证100ETF 期权波动率指数 QVIX
http://1.optbbs.com/s/vix.shtml?100ETF
:return: 深证100ETF 期权波动率指数 QVIX
:rtype: pandas.DataFrame

---

### `index_option_300etf_min_qvix() -> pandas.DataFrame`

300 ETF 期权波动率指数 QVIX-分时
http://1.optbbs.com/s/vix.shtml?300ETF
:return: 300 ETF 期权波动率指数 QVIX-分时
:rtype: pandas.DataFrame

---

### `index_option_300etf_qvix() -> pandas.DataFrame`

300 ETF 期权波动率指数 QVIX
http://1.optbbs.com/s/vix.shtml?300ETF
:return: 300 ETF 期权波动率指数 QVIX
:rtype: pandas.DataFrame

---

### `index_option_300index_min_qvix() -> pandas.DataFrame`

中证300股指 期权波动率指数 QVIX-分时
http://1.optbbs.com/s/vix.shtml?Index
:return: 中证300股指 期权波动率指数 QVIX-分时
:rtype: pandas.DataFrame

---

### `index_option_300index_qvix() -> pandas.DataFrame`

中证300股指 期权波动率指数 QVIX
http://1.optbbs.com/s/vix.shtml?Index
:return: 中证300股指 期权波动率指数 QVIX
:rtype: pandas.DataFrame

---

### `index_option_500etf_min_qvix() -> pandas.DataFrame`

500 ETF 期权波动率指数 QVIX-分时
http://1.optbbs.com/s/vix.shtml?500ETF
:return: 500 ETF 期权波动率指数 QVIX-分时
:rtype: pandas.DataFrame

---

### `index_option_500etf_qvix() -> pandas.DataFrame`

500 ETF 期权波动率指数 QVIX
http://1.optbbs.com/s/vix.shtml?500ETF
:return: 500 ETF 期权波动率指数 QVIX
:rtype: pandas.DataFrame

---

### `index_option_50etf_min_qvix() -> pandas.DataFrame`

50 ETF 期权波动率指数 QVIX
http://1.optbbs.com/s/vix.shtml?50ETF
:return: 50 ETF 期权波动率指数 QVIX
:rtype: pandas.DataFrame

---

### `index_option_50etf_qvix() -> pandas.DataFrame`

50ETF 期权波动率指数 QVIX
http://1.optbbs.com/s/vix.shtml?50ETF
:return: 50ETF 期权波动率指数 QVIX
:rtype: pandas.DataFrame

---

### `index_option_50index_min_qvix() -> pandas.DataFrame`

上证50股指 期权波动率指数 QVIX-分时
http://1.optbbs.com/s/vix.shtml?50index
:return: 上证50股指 期权波动率指数 QVIX-分时
:rtype: pandas.DataFrame

---

### `index_option_50index_qvix() -> pandas.DataFrame`

上证50股指 期权波动率指数 QVIX
http://1.optbbs.com/s/vix.shtml?50index
:return: 上证50股指 期权波动率指数 QVIX
:rtype: pandas.DataFrame

---

### `index_option_cyb_min_qvix() -> pandas.DataFrame`

创业板 期权波动率指数 QVIX-分时
http://1.optbbs.com/s/vix.shtml?CYB
:return: 创业板 期权波动率指数 QVIX-分时
:rtype: pandas.DataFrame

---

### `index_option_cyb_qvix() -> pandas.DataFrame`

创业板 期权波动率指数 QVIX
http://1.optbbs.com/s/vix.shtml?CYB
:return: 创业板 期权波动率指数 QVIX
:rtype: pandas.DataFrame

---

### `index_option_kcb_min_qvix() -> pandas.DataFrame`

科创板 期权波动率指数 QVIX-分时
http://1.optbbs.com/s/vix.shtml?KCB
:return: 科创板 期权波动率指数 QVIX-分时
:rtype: pandas.DataFrame

---

### `index_option_kcb_qvix() -> pandas.DataFrame`

科创板 期权波动率指数 QVIX
http://1.optbbs.com/s/vix.shtml?KCB
:return: 科创板 期权波动率指数 QVIX
:rtype: pandas.DataFrame

---

### `index_outer_quote_sugar_msweet() -> pandas.DataFrame`

沐甜科技数据中心-配额外进口糖估算指数
https://www.msweet.com.cn/mtkj/sjzx13/index.html
:return: 配额内进口糖估算指数
:rtype: pandas.DataFrame

---

### `index_pmi_com_cx() -> pandas.DataFrame`

财新数据-指数报告-财新中国 PMI-综合 PMI
https://yun.ccxe.com.cn/indices/pmi
:return: 财新中国 PMI-综合 PMI
:rtype: pandas.DataFrame

---

### `index_pmi_man_cx() -> pandas.DataFrame`

财新数据-指数报告-财新中国 PMI-制造业 PMI
https://yun.ccxe.com.cn/indices/pmi
:return: 财新中国 PMI-制造业 PMI
:rtype: pandas.DataFrame

---

### `index_pmi_ser_cx() -> pandas.DataFrame`

财新数据-指数报告-财新中国 PMI-服务业 PMI
https://yun.ccxe.com.cn/indices/pmi
:return: 财新中国 PMI-服务业 PMI
:rtype: pandas.DataFrame

---

### `index_price_cflp(symbol: str = '周指数') -> pandas.DataFrame`

中国公路物流运价指数
http://index.0256.cn/expx.htm
:param symbol: choice of {"周指数", "月指数", "季度指数", "年度指数"}
:type symbol: str
:return: 中国公路物流运价指数
:rtype: pandas.DataFrame

---

### `index_qli_cx() -> pandas.DataFrame`

财新数据-指数报告-高质量因子
https://yun.ccxe.com.cn/indices/qli
:return: 高质量因子
:rtype: pandas.DataFrame

---

### `index_realtime_fund_sw(symbol: str = '基础一级') -> pandas.DataFrame`

申万宏源研究-申万指数-指数发布-基金指数-实时行情
https://www.swsresearch.com/institute_sw/allIndex/releasedIndex
:param symbol: choice of {"基础一级", "基础二级", "基础三级", "特色指数"}
:type symbol: str
:return: 基金指数-实时行情
:rtype: pandas.DataFrame

---

### `index_realtime_sw(symbol: str = '二级行业') -> pandas.DataFrame`

申万宏源研究-指数系列
https://www.swsresearch.com/institute_sw/allIndex/releasedIndex
:param symbol: choice of {"市场表征", "一级行业", "二级行业", "风格指数", "大类风格指数", "金创指数"}
:type symbol: str
:return: 指数系列实时行情数据
:rtype: pandas.DataFrame

---

### `index_si_cx() -> pandas.DataFrame`

财新数据-指数报告-溢出指数
https://yun.ccxe.com.cn/indices/dei
:return: 溢出指数
:rtype: pandas.DataFrame

---

### `index_stock_cons(symbol: str = '399639') -> pandas.DataFrame`

最新股票指数的成份股目录
https://vip.stock.finance.sina.com.cn/corp/view/vII_NewestComponent.php?page=1&indexid=399639
:param symbol: 指数代码, 可以通过 ak.index_stock_info() 函数获取
:type symbol: str
:return: 最新股票指数的成份股目录
:rtype: pandas.DataFrame

---

### `index_stock_cons_csindex(symbol: str = '000300') -> pandas.DataFrame`

中证指数网站-成份股目录
https://www.csindex.com.cn/zh-CN/indices/index-detail/000300
:param symbol: 指数代码, 可以通过 ak.index_stock_info() 函数获取
:type symbol: str
:return: 最新指数的成份股
:rtype: pandas.DataFrame

---

### `index_stock_cons_sina(symbol: str = '000300') -> pandas.DataFrame`

新浪新版股票指数成份页面, 目前该接口可获取指数数量较少
https://vip.stock.finance.sina.com.cn/mkt/#zhishu_000040
:param symbol: 指数代码
:type symbol: str
:return: 指数的成份股
:rtype: pandas.DataFrame

---

### `index_stock_cons_weight_csindex(symbol: str = '000300') -> pandas.DataFrame`

中证指数网站-样本权重
https://www.csindex.com.cn/zh-CN/indices/index-detail/000300
:param symbol: 指数代码, 可以通过 ak.index_stock_info() 接口获取
:type symbol: str
:return: 最新指数的成份股权重
:rtype: pandas.DataFrame

---

### `index_stock_info() -> pandas.DataFrame`

聚宽-指数数据-指数列表
https://www.joinquant.com/data/dict/indexData
:return: 指数信息的数据框
:rtype: pandas.DataFrame

---

### `index_sugar_msweet() -> pandas.DataFrame`

沐甜科技数据中心-中国食糖指数
https://www.msweet.com.cn/mtkj/sjzx13/index.html
:return: 中国食糖指数
:rtype: pandas.DataFrame

---

### `index_ti_cx() -> pandas.DataFrame`

财新数据-指数报告-科技投入指数
https://yun.ccxe.com.cn/indices/nei
:return: 科技投入指数
:rtype: pandas.DataFrame

---

### `index_us_stock_sina(symbol: str = '.INX') -> pandas.DataFrame`

新浪财经-美股指数行情
https://stock.finance.sina.com.cn/usstock/quotes/.IXIC.html
:param symbol: choice of {".IXIC", ".DJI", ".INX", ".NDX"}
:type symbol: str
:return: 美股指数行情
:rtype: pandas.DataFrame

---

### `index_volume_cflp(symbol: str = '月指数') -> pandas.DataFrame`

中国公路物流运量指数
http://index.0256.cn/expx.htm
:param symbol: choice of {"月指数", "季度指数", "年度指数"}
:type symbol: str
:return: 中国公路物流运量指数
:rtype: pandas.DataFrame

---

### `index_yw(symbol: str = '月景气指数') -> pandas.DataFrame`

义乌小商品指数
https://www.ywindex.com/Home/Product/index/
:param symbol: choice of {"周价格指数", "月价格指数", "月景气指数"}
:type symbol: str
:return: 指数结果
:rtype: pandas.DataFrame

---

### `index_zh_a_hist(symbol: str = '000859', period: str = 'daily', start_date: str = '19700101', end_date: str = '22220101') -> pandas.DataFrame`

东方财富网-中国股票指数-行情数据
https://quote.eastmoney.com/zz/2.000859.html
:param symbol: 指数代码
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

### `index_zh_a_hist_min_em(symbol: str = '399006', period: str = '1', start_date: str = '1979-09-01 09:32:00', end_date: str = '2222-01-01 09:32:00') -> pandas.DataFrame`

东方财富网-指数数据-每日分时行情
https://quote.eastmoney.com/center/hszs.html
:param symbol: 指数代码
:type symbol: str
:param period: choice of {'1', '5', '15', '30', '60'}
:type period: str
:param start_date: 开始日期
:type start_date: str
:param end_date: 结束日期
:type end_date: str
:return: 每日分时行情
:rtype: pandas.DataFrame

---

