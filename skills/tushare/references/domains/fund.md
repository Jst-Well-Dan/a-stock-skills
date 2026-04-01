# Fund Domain Interfaces

## ETF专题

- `rt_min`: ETF实时分钟 - 获取ETF实时分钟数据，包括1\~60min
- `rt_etf_k`: ETF实时日线 - 获取ETF实时日k线行情，支持按ETF代码或代码通配符一次性提取全部ETF实时日k线行情
- `stk_mins`: ETF历史分钟 - 获取ETF分钟数据，支持1min/5min/15min/30min/60min行情，提供Python SDK和 http Restful API两种方式
- `etf_index`: ETF基准指数 - 获取ETF基准指数列表信息
- `etf_basic`: ETF基本信息 - 获取国内ETF基础信息，包括了QDII。数据来源与沪深交易所公开披露信息。
- `fund_adj`: ETF复权因子 - 获取基金复权因子，用于计算基金复权行情
- `fund_daily`: ETF日线行情 - 获取ETF行情每日收盘后成交数据，历史超过10年
- `etf_share_size`: ETF份额规模 - 获取沪深ETF每日份额和规模数据，能体现规模份额的变化，掌握ETF资金动向，同时提供每日净值和收盘价；数据指标是分批入库，建议在每日19点后提取；另外，涉及海外的ETF数据更新会晚一些属于正常情况。

## 公募基金

- `fund_manager`: 基金经理 - 获取公募基金经理数据，包括基金经理简历等数据
- `fund_share`: 基金规模 - 获取基金规模数据，包含上海和深圳ETF基金
- `fund_portfolio`: 基金持仓 - 获取公募基金持仓数据，季度更新
- `fund_div`: 基金分红 - 获取公募基金分红数据
- `fund_nav`: 基金净值 - 获取公募基金净值数据
- `fund_company`: 基金管理人 - 获取公募基金管理人列表
- `fund_basic`: 基金列表 - 获取公募基金数据列表，包括场内和场外基金
- `fund_factor_pro`: 基金技术面因子(专业版) - 获取场内基金每日技术面因子数据，用于跟踪场内基金当前走势情况，数据由Tushare社区自产，覆盖全历史；输出参数_bfq表示不复权，描述中说明了因子的默认传参，如需要特殊参数或者更多因子可以联系管理员评估

