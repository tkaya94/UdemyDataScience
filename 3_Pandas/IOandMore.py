import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
import pandas as pd


def df_info(df: pd.DataFrame) -> None:
    return df.head(n=20).style


df = pd.read_csv("data/titanic/dataset.csv")
print(df.columns)

cols = ["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Cabin", "Embarked"]
index_name = "PassengerId"
df = pd.DataFrame(df[cols], index=df[index_name])
df.index.name = "ID"
print(df)

df.iloc[:100].to_csv("data/titanic/modified_dataset.csv")

print(df.describe())
