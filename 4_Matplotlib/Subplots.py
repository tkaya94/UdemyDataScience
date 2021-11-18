import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.set_ylim(-1.2, 1.2)

ax2 = fig.add_subplot(212)
ax2.set_ylim(-1.2, 1.2)

x = np.linspace(0, 10)
ax1.plot(np.sin(x))
ax2.plot(np.cos(x))
plt.show()
