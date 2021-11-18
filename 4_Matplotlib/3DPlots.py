import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import LinearLocator

import numpy as np
np.random.seed(0)

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

# zline = np.linspace(0, 15, 1000)
# xline = np.sin(zline)
# yline = np.cos(zline)
# ax.plot3D(xline, yline, zline, "gray")

# zdata = 15 * np.random.random(100)
# xdata = np.sin(zdata)
# ydata = np.cos(zdata)
# ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap="Greens")
# plt.show()


def f(x, y):
    return x**2 + y**2


s = .05
x = np.arange(-5, 5, s)
y = np.arange(-5, 5, s)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# ax.contour3D(X, Y, Z, 50, cmap="binary")
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.set_zlabel("z")
# plt.show()

surf = ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor="none")
ax.set_title("surface")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
fig.colorbar(surf, shrink=.5, aspect=5)
plt.show()
