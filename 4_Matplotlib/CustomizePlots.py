import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)

x = np.linspace(0, 10, 1000)
# fig, ax = plt.subplots()
# ax.plot(x, np.sin(x), "-b", label="sin")
# ax.plot(x, np.cos(x), "--r", label="cos")
# ax.axis("equal")
# ax.legend(loc="upper left")
# plt.show()

# I = np.sin(x) * np.cos(x[:, np.newaxis])
# plt.imshow(I, cmap='gray')
# plt.show()

fig = plt.figure()
ax = fig.add_subplot()

ax.plot(x, np.cos(x), label="first")
ax.plot(x, np.sin(x), label="second")
ax.legend()

fig.suptitle(
    'bold figure suptitle',
    fontsize=14,
    fontweight='bold'
)

ax.set_title('axes title')
ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')

ax.text(
    2, 2,
    'test'
)

ax.plot([np.pi / 2.0], [1], 'o')
ax.annotate(
    '$cos(\pi / 2)$',
    xy=(np.pi / 2.0, 1),
    xytext=(np.pi / 2.0 - 0.65, 1.75),
    arrowprops=dict(facecolor='black', shrink=0.05)
)

plt.show()
