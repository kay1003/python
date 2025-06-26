import akshare as ak
import pandas as pd
pd.set_option('display.max_rows', None)  # 显示所有行
pd.set_option('display.max_columns', None)  # 显示所有列

df = ak.fund_etf_hist_em(symbol="515450", period="daily", start_date="20240101", end_date="20250101", adjust="qfq")
# 格式处理
df["日期"] = pd.to_datetime(df["日期"])
df = df.sort_values("日期").reset_index(drop=True)

# # 计算每日涨跌幅
# df["涨跌幅"] = df["收盘"].pct_change() * 100

# 筛选出下跌交易日
df['涨跌幅'] = df['涨跌幅'].astype(float)
df_down = df[df["涨跌幅"] < 0]

# 统计并输出
print(f"2024年下跌交易日数量：{len(df_down[df_down['日期'].dt.year == 2024])} 天")
# 定义跌幅区间：[(上限, 下限)]
intervals = [
    (-0.0, -0.5),
    (-0.5, -1.0),
    (-1.0, -1.5),
    (-1.5, -2.0),
    (-2.0, -5.0)
]
# 遍历并筛选
for upper, lower in intervals:
    mask = (df['涨跌幅'] <= upper) & (df['涨跌幅'] > lower)
    subset = df[mask]

    print(f"\n--- 跌幅区间：{upper:.1f}% 到 {lower:.1f}% ---")
    print(f"共 {len(subset)} 天")
    if not subset.empty:
        print(subset[['日期', '涨跌幅']].to_string(index=False))