import pandas as pd

# df = pd.read_csv("numpytxt.csv").copy()

# print(df.describe())
# print(df.isna().sum().sum())
# print(df.groupby(by=["animal","water_need"]).max())

data = pd.Series([*range(10)])

print(data.rolling(3,min_periods=1).mean())
