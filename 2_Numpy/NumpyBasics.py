import numpy as np
from NumpyIntro import array_info

x = np.array([[1, 2], [3, 4], [5, 6]])
array_info(x)

print(x[1:])
print("======")

mean = [0, 0]
cov = [[1, 2], [2, 5]]
y = np.random.multivariate_normal(mean=mean, cov=cov, size=10)
print(y)
print(y.shape)

rand_idxs = np.random.randint(low=0, high=y.shape[0], size=3)
print(rand_idxs)

y_subsample = y[rand_idxs, :]
print(y_subsample)
