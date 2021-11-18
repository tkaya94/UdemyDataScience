import numpy as np
np.random.seed(0)

from NumpyIntro import array_info

x = np.array([[1, 2], [5, 3], [4, 6]])
array_info(x)

print(np.max(x, axis=1))
