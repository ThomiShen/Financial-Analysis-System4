import akshare as ak
data = ak.stock_zh_a_hist(symbol="300188",period="daily")
print(data.iloc[0])