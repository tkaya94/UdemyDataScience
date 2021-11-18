import matplotlib.pyplot as plt
from PandasIntro import df_info
import numpy as np
np.random.seed(0)
import pandas as pd


df = pd.read_csv("data/titanic/dataset.csv")
cols = ["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Cabin", "Embarked"]
index_name = "PassengerId"
df = pd.DataFrame(df[cols], index=df[index_name])
df.index.name = "ID"
print(df)

print("=1=")
df["Age"] = df["Age"].fillna(value=-1.0)
df["Pclass"] = df["Pclass"].fillna(value=-1.0)
df["Cabin"] = df["Cabin"].fillna(value="None")
df = df.astype({"Age": "int8"})
df = df.astype({"Pclass": "int8"})

print("=2=")
df = df.dropna(axis="rows")
print(df)

print("=3=")
# print(df["Sex"][lambda x: x == "male"])
mean_vals = df.groupby(["Sex", "Survived"]).mean()
print("Mean age is:\n", mean_vals["Age"])

med_vals = df.groupby(["Sex", "Survived"]).median()
print("Median age is:\n", med_vals["Age"])

min_vals = df.groupby(["Sex", "Survived"]).min()
print("Min age is:\n", min_vals["Age"])

max_vals = df.groupby(["Sex", "Survived"]).max()
print("Max age is:\n", max_vals["Age"])

print("=4=")
grouped = df.groupby(["Age"]).sum()
group_sort = grouped["Survived"].sort_values()
group_sort = group_sort.drop(-1)
print(group_sort.idxmax(), "is the aged that survived most")
print(group_sort[24], "people survived")
