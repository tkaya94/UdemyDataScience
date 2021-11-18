import numpy as np
np.random.seed(0)
import pandas as pd
from PandasIntro import series_info, df_info

num_samples = 10
num_features = 3
index = pd.date_range("21/4/2021", periods=num_samples)
series_info(index)
print("=======")

df = pd.DataFrame(np.random.randn(num_samples, num_features), index=index, 
    columns=["Weight", "Temp", "Speed"])
df_info(df)

print("Total weight is", np.sum(df["Weight"]))

for weight in df["Weight"]:
    print(weight)

for key, val in df.iterrows():
    print(type(key))
    print(type(val))
    print(key, val, "\n")

print(df.loc["2021-04-22":"2021-04-25", "Weight"])
print(df.iloc[1:5])
