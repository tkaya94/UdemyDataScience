import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
import pandas as pd

df = pd.read_csv("data/USA_cars_datasets.csv")
print(df.head())

print("=1=")
grouped = df.groupby(["state"])
print(grouped.count())

print("=2=")
df2 = df[df.state == "new mexico"]
print(df2)
print(df2.count())

print("=3=")
df3 = df[df.state == "new york"]
print("Mileage mean from New York is", df3["mileage"].mean())

print("=4=")
df_newer = df.loc[df["year"] >= 2019]
print(df_newer)

print("=5=")
df["color"] = df["color"].transform(lambda x: x[0])
print(df.head())
