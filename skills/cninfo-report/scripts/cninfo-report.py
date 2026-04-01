#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
股票财务报告下载工具 - 命令行版
支持沪深京和港股市场的年报、季报批量下载
"""

import math
import re
import sys
import argparse
import time
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from typing import Optional, Tuple
from urllib.parse import urlparse, parse_qs

import pandas as pd
import requests

# 设置控制台编码为UTF-8，解决中文显示问题
if sys.platform.startswith('win'):
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.detach())


# ─────────────────────────────────────────────────────────────
# 巨潮资讯网 API 辅助函数（移植自 akshare，已修复 params/data bug）
# ─────────────────────────────────────────────────────────────

@lru_cache(maxsize=None)
def _获取类别字典() -> dict:
    """公告类别名称 -> 巨潮 API category 参数值"""
    return {
        "年报":   "category_ndbg_szsh",
        "半年报": "category_bndbg_szsh",
        "一季报": "category_yjdbg_szsh",
        "三季报": "category_sjdbg_szsh",
    }


@lru_cache(maxsize=None)
def _获取股票代码映射(市场: str = "沪深京") -> dict:
    """从巨潮资讯获取 股票代码 -> orgId 的映射字典"""
    url_map = {
        "沪深京": "http://www.cninfo.com.cn/new/data/szse_stock.json",
        "港股":   "http://www.cninfo.com.cn/new/data/hke_stock.json",
        "三板":   "http://www.cninfo.com.cn/new/data/gfzr_stock.json",
        "基金":   "http://www.cninfo.com.cn/new/data/fund_stock.json",
        "债券":   "http://www.cninfo.com.cn/new/data/bond_stock.json",
    }
    r = requests.get(url_map[市场], timeout=15)
    stock_list = r.json()["stockList"]
    return {item["code"]: item["orgId"] for item in stock_list}


class 股票报告下载器:
    """股票财务报告下载工具类"""
    
    def __init__(self, 下载目录: str = None):
        """
        初始化下载器

        Args:
            下载目录: 报告保存的根目录，默认为项目根目录下的 财务报告下载 文件夹
        """
        if 下载目录 is None:
            # 默认输出到项目根目录
            self.下载目录 = Path.cwd() / "财务报告下载"
        else:
            self.下载目录 = Path(下载目录)
        self.下载目录.mkdir(exist_ok=True)
        
        # 请求头，模拟浏览器访问
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
    
    def 获取报告数据(self, 股票代码: str, 市场: str, 报告类型: str = "所有报告", 
                    开始日期: str = "20200101", 结束日期: str = None) -> pd.DataFrame:
        """获取股票报告数据"""
        if 结束日期 is None:
            结束日期 = datetime.now().strftime("%Y%m%d")
        
        print(f"正在获取 {股票代码} ({市场}) 的{报告类型}数据...")
        
        try:
            if 市场 == "港股":
                return self._获取港股报告(股票代码, 报告类型, 开始日期, 结束日期)
            elif 市场 == "沪深京":
                return self._获取沪深京报告(股票代码, 报告类型, 开始日期, 结束日期)
            else:
                raise ValueError("市场参数只能是 '沪深京' 或 '港股'")
                
        except Exception as e:
            print(f"获取报告数据时出错: {e}")
            return pd.DataFrame()
    
    def _获取港股报告(self, 股票代码: str, 报告类型: str, 开始日期: str, 结束日期: str) -> pd.DataFrame:
        """直接调用巨潮资讯网API获取港股报告（参照akshare实现修复）"""
        try:
            # 从巨潮港股股票列表获取真实 orgId
            hke_json = requests.get(
                'http://www.cninfo.com.cn/new/data/hke_stock.json', timeout=15
            ).json()
            org_map = {item['code']: item['orgId'] for item in hke_json['stockList']}
            if 股票代码 not in org_map:
                print(f"  在巨潮港股列表中未找到股票代码 {股票代码}")
                return pd.DataFrame()
            org_id = org_map[股票代码]

            # 日期格式转换：YYYYMMDD -> YYYY-MM-DD
            def fmt(d):
                return f"{d[:4]}-{d[4:6]}-{d[6:]}"

            url = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'
            payload = {
                'pageNum': '1',
                'pageSize': '30',
                'column': 'hke',
                'tabName': 'fulltext',
                'plate': '',
                'stock': f"{股票代码},{org_id}",
                'searchkey': '',
                'secid': '',
                'category': '',
                'trade': '',
                'seDate': f"{fmt(开始日期)}~{fmt(结束日期)}",
                'sortName': '',
                'sortType': '',
                'isHLtitle': 'true',
            }

            # 第一次请求用 data= 获取总页数（akshare 用 params= 是 bug）
            r = requests.post(url, data=payload, timeout=30)
            text_json = r.json()
            total = int(text_json.get('totalAnnouncement', 0))
            if total == 0:
                print(f"  未找到 {股票代码} 的报告数据")
                return pd.DataFrame()

            page_num = math.ceil(total / 30)
            all_records = []
            for page in range(1, page_num + 1):
                payload['pageNum'] = str(page)
                r = requests.post(url, data=payload, timeout=30)
                announcements = r.json().get('announcements') or []
                all_records.extend(announcements)
                time.sleep(0.5)

            # 年报关键词过滤（注意 "年度报告" 是 "半年度报告" 的子串，需显式排除）
            年报关键词 = ['年报', '年度报告', '全年业绩']
            排除关键词 = ['半年', '摘要', '英文', '海外监管公告']
            if 报告类型 == "年报":
                all_records = [
                    a for a in all_records
                    if any(kw in a.get('announcementTitle', '') for kw in 年报关键词)
                    and not any(ex in a.get('announcementTitle', '') for ex in 排除关键词)
                ]

            # 构建与 A 股一致的 DataFrame，PDF 直接用 adjunctUrl 拼接
            records = []
            for a in all_records:
                ts_ms = a.get('announcementTime', 0)
                pub_date = datetime.fromtimestamp(ts_ms / 1000).strftime('%Y-%m-%d') if ts_ms else ''
                adj_url = a.get('adjunctUrl', '')
                pdf_url = f"http://static.cninfo.com.cn/{adj_url}" if adj_url else ''
                records.append({
                    '代码': a.get('secCode', 股票代码),
                    '简称': a.get('secName', 股票代码),
                    '公告标题': a.get('announcementTitle', ''),
                    '公告时间': pub_date,
                    '公告链接': pdf_url,
                })

            df = pd.DataFrame(records)
            df = df.sort_values('公告时间', ascending=False).reset_index(drop=True)
            print(f"找到 {len(df)} 个报告")
            return df

        except Exception as e:
            print(f"获取港股报告时出错: {e}")
            return pd.DataFrame()
    
    def _获取沪深京报告(self, 股票代码: str, 报告类型: str, 开始日期: str, 结束日期: str) -> pd.DataFrame:
        """直接调用巨潮资讯网API获取沪深京报告（移植自akshare，已修复 params/data bug）"""
        try:
            股票映射 = _获取股票代码映射("沪深京")
            if 股票代码 not in 股票映射:
                print(f"  在巨潮沪深京列表中未找到股票代码 {股票代码}")
                return pd.DataFrame()
            org_id = 股票映射[股票代码]

            类别字典 = _获取类别字典()

            def fmt(d):
                return f"{d[:4]}-{d[4:6]}-{d[6:]}"

            url = "http://www.cninfo.com.cn/new/hisAnnouncement/query"

            if 报告类型 == "年报":
                类别列表 = ["年报"]
            else:
                类别列表 = ["年报", "半年报", "一季报", "三季报"]

            报告列表 = []
            for 类别 in 类别列表:
                print(f"  正在获取{类别}数据...")
                payload = {
                    "pageNum": "1",
                    "pageSize": "30",
                    "column": "szse",
                    "tabName": "fulltext",
                    "plate": "",
                    "stock": f"{股票代码},{org_id}",
                    "searchkey": "",
                    "secid": "",
                    "category": 类别字典.get(类别, ""),
                    "trade": "",
                    "seDate": f"{fmt(开始日期)}~{fmt(结束日期)}",
                    "sortName": "",
                    "sortType": "",
                    "isHLtitle": "true",
                }
                try:
                    # 全程使用 data=payload（akshare 第一次用 params= 是 bug）
                    r = requests.post(url, data=payload, timeout=30)
                    text_json = r.json()
                    total = int(text_json.get("totalAnnouncement", 0))
                    if total == 0:
                        print(f"    未找到{类别}数据")
                        continue

                    page_num = math.ceil(total / 30)
                    all_records = []
                    for page in range(1, page_num + 1):
                        payload["pageNum"] = str(page)
                        r = requests.post(url, data=payload, timeout=30)
                        announcements = r.json().get("announcements") or []
                        all_records.extend(announcements)
                        time.sleep(0.3)

                    # 过滤摘要、英文版
                    all_records = [
                        a for a in all_records
                        if not any(ex in a.get("announcementTitle", "") for ex in ["摘要", "英文"])
                    ]

                    # 构建 DataFrame，链接格式与 akshare 一致（供 _转换巨潮链接 处理）
                    records = []
                    for a in all_records:
                        ts_ms = a.get("announcementTime", 0)
                        pub_date = datetime.fromtimestamp(ts_ms / 1000).strftime("%Y-%m-%d") if ts_ms else ""
                        ann_id = a.get("announcementId", "")
                        o_id = a.get("orgId", org_id)
                        link = (
                            f"http://www.cninfo.com.cn/new/disclosure/detail"
                            f"?stockCode={a.get('secCode', 股票代码)}"
                            f"&announcementId={ann_id}"
                            f"&orgId={o_id}"
                            f"&announcementTime={pub_date}"
                        )
                        records.append({
                            "代码": a.get("secCode", 股票代码),
                            "简称": a.get("secName", 股票代码),
                            "公告标题": a.get("announcementTitle", ""),
                            "公告时间": pub_date,
                            "公告链接": link,
                        })

                    if records:
                        df = pd.DataFrame(records)
                        报告列表.append(df)
                        print(f"    找到 {len(df)} 个{类别}")

                except Exception as e:
                    print(f"    获取{类别}时出错: {e}")
                    continue

            if 报告列表:
                合并结果 = pd.concat(报告列表, ignore_index=True)
                合并结果 = 合并结果.sort_values("公告时间", ascending=False)

                # 同日期去重：有"年度报告"版时丢掉仅含"年报"的简短版本
                def _去重优先年度报告(组):
                    有年度报告 = 组['公告标题'].str.contains('年度报告')
                    if 有年度报告.any() and not 有年度报告.all():
                        return 组[有年度报告]
                    return 组
                合并结果 = 合并结果.groupby('公告时间', group_keys=False).apply(_去重优先年度报告)
                合并结果 = 合并结果.sort_values("公告时间", ascending=False)

                print(f"总计找到 {len(合并结果)} 个报告")
                return 合并结果.reset_index(drop=True)
            else:
                print("未找到任何报告")
                return pd.DataFrame()

        except Exception as e:
            print(f"获取沪深京报告时出错: {e}")
            return pd.DataFrame()
    
    def 生成文件名(self, 报告信息: pd.Series) -> str:
        """根据报告信息生成合理的文件名"""
        股票代码 = 报告信息['代码']
        股票简称 = 报告信息['简称']
        公告标题 = 报告信息['公告标题']
        公告时间 = 报告信息['公告时间']
        
        if isinstance(公告时间, str):
            日期部分 = 公告时间[:10].replace('-', '')
        else:
            日期部分 = datetime.now().strftime("%Y%m%d")
        
        清理标题 = re.sub(r'[<>:"/\\|?*]', '_', 公告标题)
        清理标题 = 清理标题.strip()
        
        文件名 = f"{股票代码}_{股票简称}_{日期部分}_{清理标题}"
        
        if len(文件名) > 100:
            文件名 = 文件名[:100] + "..."
        
        return 文件名
    
    def _转换巨潮链接(self, 原链接: str) -> Optional[str]:
        """转换巨潮资讯网链接为PDF下载链接"""
        try:
            parsed_url = urlparse(原链接)
            params = parse_qs(parsed_url.query)
            
            announcement_id = params.get('announcementId', [None])[0]
            announcement_time = params.get('announcementTime', [None])[0]
            
            if not announcement_id or not announcement_time:
                print(f"  无法从链接中提取必要参数: {原链接}")
                return None
            
            # 处理时间格式，只保留日期部分
            if ' ' in announcement_time:
                announcement_time = announcement_time.split(' ')[0]
            
            if len(announcement_time) == 10 and announcement_time.count('-') == 2:
                pdf_url = f"http://static.cninfo.com.cn/finalpage/{announcement_time}/{announcement_id}.PDF"
                print(f"  转换巨潮链接: {pdf_url}")
                return pdf_url
            else:
                print(f"  日期格式不正确: {announcement_time}")
                return None
            
        except Exception as e:
            print(f"  转换巨潮链接时出错: {e}")
            return None
    
    def 下载PDF(self, 下载链接: str, 保存路径: Path, 最大重试次数: int = 3) -> bool:
        """下载PDF文件"""
        # 如果是巨潮资讯网链接，先转换为PDF直链
        if 'cninfo.com.cn' in 下载链接 and 'disclosure/detail' in 下载链接:
            pdf_url = self._转换巨潮链接(下载链接)
            if pdf_url:
                下载链接 = pdf_url
            else:
                print(f"  无法转换巨潮链接")
                return False
        
        for 重试次数 in range(最大重试次数):
            try:
                print(f"  正在下载PDF文件... (尝试 {重试次数 + 1}/{最大重试次数})")
                
                response = requests.get(下载链接, headers=self.headers, timeout=30, stream=True)
                response.raise_for_status()
                
                content_type = response.headers.get('Content-Type', '').lower()
                if 'pdf' in content_type or 'application/pdf' in content_type:
                    保存路径.parent.mkdir(parents=True, exist_ok=True)
                    
                    with open(保存路径, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
                    
                    文件大小 = 保存路径.stat().st_size
                    if 文件大小 > 1024:
                        print(f"  下载完成: {保存路径.name} ({文件大小/1024:.1f} KB)")
                        return True
                    else:
                        print(f"  下载的文件过小，可能下载失败")
                        保存路径.unlink(missing_ok=True)
                else:
                    print(f"  链接不是PDF文件，可能需要进一步处理")
                        
            except requests.exceptions.RequestException as e:
                print(f"  下载失败 (尝试 {重试次数 + 1}): {e}")
                if 重试次数 < 最大重试次数 - 1:
                    time.sleep(2)
                    
            except Exception as e:
                print(f"  下载时发生未知错误: {e}")
                break
        
        return False
    
    def 批量下载报告(self, 股票代码: str, 市场: str, 报告类型: str = "所有报告",
                     开始日期: str = "20200101", 结束日期: str = None) -> Tuple[int, int]:
        """批量下载股票报告"""
        print(f"\n开始批量下载 {股票代码} ({市场}) 的{报告类型}")
        print("=" * 60)
        
        报告数据 = self.获取报告数据(股票代码, 市场, 报告类型, 开始日期, 结束日期)
        
        if 报告数据.empty:
            print("未找到任何报告数据")
            return 0, 0
        
        # 不再限制最大下载数量，下载所有找到的报告
        总数量 = len(报告数据)
        成功数量 = 0
        
        股票目录 = self.下载目录 / f"{股票代码}_{报告数据.iloc[0]['简称']}_年度报告"
        股票目录.mkdir(exist_ok=True)
        
        print(f"\n准备下载 {总数量} 个报告到目录: {股票目录}")
        print("-" * 60)
        
        for idx, 报告 in 报告数据.iterrows():
            try:
                print(f"\n[{idx + 1}/{总数量}] {报告['公告标题']}")
                print(f"发布时间: {报告['公告时间']}")
                
                文件名 = self.生成文件名(报告)
                保存路径 = 股票目录 / f"{文件名}.pdf"
                
                if 保存路径.exists():
                    print(f"  文件已存在，跳过下载: {保存路径.name}")
                    成功数量 += 1
                    continue
                
                if self.下载PDF(报告['公告链接'], 保存路径):
                    成功数量 += 1
                else:
                    print(f"  下载失败: {报告['公告标题']}")
                
                time.sleep(1)
                
            except Exception as e:
                print(f"  处理报告时出错: {e}")
                continue
        
        print("\n" + "=" * 60)
        print(f"下载完成! 成功: {成功数量}/{总数量}")
        print(f"保存位置: {股票目录}")
        
        return 成功数量, 总数量


def main():
    """主函数 - 命令行参数模式"""
    parser = argparse.ArgumentParser(
        description="股票财务报告下载工具 - 支持沪深京和港股市场",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  python 命令行下载.py 000001
  python 命令行下载.py 600036 --market 沪深京 --years 3
  python 命令行下载.py 00700 --market 港股 --type all
  python 命令行下载.py 000001 --years 10 --type all

股票代码格式:
  沪深京市场: 6位数字 (如 000001、600036)
  港股市场:   5位数字 (如 00700、01299)
        """
    )

    parser.add_argument("股票代码", help="股票代码")
    parser.add_argument(
        "--market", dest="市场", default="沪深京", choices=["沪深京", "港股"],
        help="市场类型 (默认: 沪深京)"
    )
    parser.add_argument(
        "--type", dest="报告类型", default="年报", choices=["年报", "all"],
        metavar="TYPE",
        help="报告类型: 年报 | all (年报+半年报+季报，默认: 年报)"
    )
    parser.add_argument(
        "--years", dest="年数", type=int, default=5,
        metavar="N",
        help="下载最近N年的报告，范围1-20 (默认: 5)"
    )

    args = parser.parse_args()

    if args.年数 < 1 or args.年数 > 20:
        parser.error("--years 参数应在 1-20 之间")

    报告类型 = "所有报告" if args.报告类型 == "all" else "年报"

    当前年份 = datetime.now().year
    开始年份 = 当前年份 - args.年数 + 1
    开始日期 = f"{开始年份}0101"

    print("=" * 60)
    print(f"  股票代码: {args.股票代码}  市场: {args.市场}")
    print(f"  报告类型: {报告类型}  年份范围: {开始年份}-{当前年份} (近{args.年数}年)")
    print("=" * 60)

    try:
        下载器 = 股票报告下载器()  # 默认输出到项目根目录/财务报告下载
        成功数量, 总数量 = 下载器.批量下载报告(
            股票代码=args.股票代码,
            市场=args.市场,
            报告类型=报告类型,
            开始日期=开始日期
        )

        print("\n" + "=" * 60)
        if 成功数量 > 0:
            print(f"下载完成! 成功下载 {成功数量}/{总数量} 个文件")
            print(f"文件保存在: 财务报告下载/{args.股票代码}_*")
        else:
            print(f"下载失败! {成功数量}/{总数量}")
            print("可能原因: 网络连接问题、股票代码不存在、指定时间范围内无报告")
        print("=" * 60)

    except KeyboardInterrupt:
        print("\n用户中断下载")
        sys.exit(1)
    except Exception as e:
        print(f"\n下载过程中出错: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 