import numpy as np
from NumpyIntro import array_info

a = np.arange(start=1, stop=10)
array_info(a)

grid = np.reshape(a, newshape=(3, 3))
array_info(grid)

x = np.array([1, 2, 3])
x = np.reshape(x, newshape=(1, 3))
array_info(x)

x = x.ravel()
array_info(x)

y = np.array([-1.0, 2.0, 3.0], dtype=np.float32)
y = y.astype(np.int8)
array_info(y)

print("=======")

b = np.array([1, 2, 3])
c = np.array([3, 3, 1])
result = np.concatenate([b, c]) # immer auf zeile 0
array_info(result)

grid = np.array([[1, 2, 3], [4, 6, 5]])
res = np.concatenate([grid, grid], axis=1)
array_info(res)
