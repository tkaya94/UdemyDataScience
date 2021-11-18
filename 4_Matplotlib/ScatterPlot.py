import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)

x = np.linspace(0, 10, 30)
y = np.sin(x)

#plt.scatter(x, y, marker="o")
#plt.show()

x = np.random.randn(100)
y = np.random.randn(100)
colors = np.random.rand(100)
plt.scatter(x, y, c=colors, s=10, alpha=1.0, cmap="viridis")
plt.colorbar()
plt.show()
