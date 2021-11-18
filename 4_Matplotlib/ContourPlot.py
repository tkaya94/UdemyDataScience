import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)


def f(x, y):
    return x**2 + y**2


x = np.arange(-5, 5.0, 0.25)
y = np.arange(-5, 5.0, 0.25)

X, Y = np.meshgrid(x, y)

Z = f(X, Y)
#plt.contourf(X, Y, Z, 20, cmap="RdGy")
#plt.colorbar()
#plt.show()

delta = .025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
plt.contour(X, Y, Z)
plt.colorbar()
plt.show()
