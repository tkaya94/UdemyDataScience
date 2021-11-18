import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)


fig = plt.figure()
ax = plt.axes()

x = np.linspace(start=0, stop=2 * np.pi, num=25)
ax.plot(x, np.sin(x))
ax.plot(x, np.cos(x))
plt.xlim(-1, 7)
plt.ylim(-1.25, 1.25)
plt.title("Curves")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["sin(x)", "cos(x)"])
plt.show()
