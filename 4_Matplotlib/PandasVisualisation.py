import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
import pandas as pd

num_samples = 100
ts = pd.Series(np.random.randn(num_samples), index=pd.date_range("1/1/2000", periods=num_samples))
# # print(ts.head())
# ts.plot()
# plt.show()

data = np.concatenate([np.random.randn(num_samples, 2),
    np.random.randint(low=0, high=10, size=(num_samples, 1))], axis=1)

df = pd.DataFrame(data, index=ts.index, columns=["A", "B", "C"]).astype(
    {"A": np.float32, "B": np.float32, "C": np.uint8})
# print(df.head())
df.plot()
plt.show()
