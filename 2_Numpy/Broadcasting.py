import numpy as np
np.random.seed(0)

a = np.array([1, 2])
b = 1.6

print(a * b)

print(a + 5)

M = np.ones(shape=(2, 2))
print(M + a)

a = np.arange(start=0, stop=3)
b = np.arange(start=0, stop=3)[:, np.newaxis]
print(a + b)

x = np.random.normal(loc=5.0, scale=2.0, size=(100_000, 2))
x_mean = np.mean(x, axis=0)
x_var = np.var(x, axis=0)
x_centered = x - x_mean
x_standardized = x_centered / (np.sqrt(1e-6 + x_var))
