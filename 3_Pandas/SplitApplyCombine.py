import numpy as np
np.random.seed(0)
import pandas as pd

data = [[4, 9], [4, 9], [4, 9]]
df = pd.DataFrame(data, columns=["A", "B"])
print("Dataframe is:\n", df)

print("sqrt Applied:\n", df.apply(np.sqrt))

print("Sum applied:\n", df.apply(np.sum, axis=0))

keys = ['A', 'B', 'C', 'A', 'B', 'C']
names = ['N1', 'N1', 'N2', 'N2', 'N3', 'N4']

df = pd.DataFrame(
    {
        'key': keys,
        'name': names,
        'data': range(10, 16)
    }
)
print("Dataframe is:\n", df)
for c in ["A", "B", "C"]:
    print(df[df["key"] == c].data.sum())

grouped = df.groupby("key")
for v in grouped:
    print(v)

print(df.groupby("key").aggregate(np.sum))

print(df.groupby("key").agg(["min", "max", "mean", "std", "var"]))

print(grouped.transform(lambda x: x**2))
