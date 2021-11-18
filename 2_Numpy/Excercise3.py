import numpy as np

print("=1=")
A = np.zeros(shape=(5, 5))
A[1:-1, 1:-1] = 1
print(A)

print("=2=")
B = np.zeros(shape=(8, 8))
B[1::2, ::2] = 1
B[::2, 1::2] = 1
print(B)

print("=3=")


def get_closest(array, val):
    idxs = np.argsort(np.abs(array - val))
    return idxs[0]


val = 4.6
array = np.array([1, 2, 3, 4, 5])
print("Element", get_closest(array, val), "is closest")

print("=4=")


def n_largest(array, n):
    array_sort = np.flip(np.sort(array))
    return array_sort[0:n]


array = np.arange(10)
n = 4
print(n_largest(array, n))
