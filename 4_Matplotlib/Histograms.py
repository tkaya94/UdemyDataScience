import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)

data = np.random.randn(10_000)
#plt.hist(data, bins=30, alpha=.5, histtype="stepfilled", color="steelblue")
#plt.show()

counts, bin_edges = np.histogram(data, bins=5)
print(counts)
print(bin_edges)

x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

kwargs = dict(
    histtype='stepfilled',
    alpha=0.3,
    bins=40
)

#plt.hist(x1, **kwargs)
#plt.hist(x2, **kwargs)
#plt.hist(x3, **kwargs)
#plt.show()

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean=mean, cov=cov, size=10000).T
plt.hist2d(x, y, bins=30, cmap="Blues")
plt.colorbar()
plt.show()
