import akshare as ak
import pandas as pd


df = ak.fund_etf_hist_em(symbol="515450", period="daily", start_date="20240100", end_date="20250101", adjust="qfq")
# 格式处理
df["日期"] = pd.to_datetime(df["日期"])
df = df.sort_values("日期").reset_index(drop=True)

# 计算每日涨跌幅
df["涨跌幅"] = df["收盘价"].pct_change() * 100

# 筛选出下跌交易日
df_down = df[df["涨跌幅"] < 0]

# 输出统计结果
print(f"2024年下跌交易日数量：{len(df_down[df_down['日期'].dt.year == 2024])} 天")
print(df_down[df_down["日期"].dt.year == 2024][["日期", "涨跌幅"]])