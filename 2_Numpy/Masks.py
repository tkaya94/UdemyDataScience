import numpy as np
import numpy.ma as ma
np.random.seed(0)

x = np.random.uniform(-1.5, 1.5, size=10)
print(x)
x_slice = x[x < 1.0]
print(x_slice)

data = np.array([1, 2, 3, -1, 5])
masked_data = ma.masked_array(data, mask=[0, 0, 0, 1, 0])
print(masked_data)
