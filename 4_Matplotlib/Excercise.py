import numpy as np
np.random.seed(0)
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


def array_info(array: np.ndarray) -> None:
    print(f"ndim: {array.ndim}")
    print(f"shape: {array.shape}")
    print(f"size: {array.size}")
    print(f"dtype: {array.dtype}")
    print(f"values:\n{array}\n")


print("=1=")
mean = [-5, 5]
cov = [[1, 0], [0, 1]]
n_samples = 100
x1, x2 = np.random.multivariate_normal(mean, cov, n_samples).T

y = x1 + x2

print("=2=")
# plt.scatter(x1, x2, c=y, cmap="coolwarm")
# plt.xlabel("x_1")
# plt.ylabel("x_2")
# plt.colorbar()
# plt.show()

print("=3=")
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import LinearLocator

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

fig3 = ax.scatter3D(x1, x2, y, c=y, cmap='coolwarm')
ax.set_xlabel("x_1")
ax.set_ylabel("x_2")
fig.colorbar(fig3)
plt.show()
