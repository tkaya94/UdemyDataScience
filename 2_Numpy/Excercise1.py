import numpy as np
np.random.seed(0)


def array_info(array: np.ndarray) -> None:
    print(f"ndim: {array.ndim}")
    print(f"shape: {array.shape}")
    print(f"size: {array.size}")
    print(f"dtype: {array.dtype}")
    print(f"values:\n{array}\n")

print("=1=")
M = np.random.random_integers(low=-10, high=10, size=[5, 5])
print(M)

print("=2=")
lo = -10
hi = 10
N = (hi - lo) * np.random.random_sample(size=[5, 5]) + lo
print(N)

print("=3=")
print(np.sum(M < 0), "elements less than 0 in M")
print(np.sum(N < 0), "elements less than 0 in N")

print("=4=")
M[M < 0] = 0
N[N < 0] = 0
print(M)
print(N)

print("=5=")
O = np.concatenate((M, N), axis=0)
print(O)

print("=6=")
print(np.cos(O * np.pi))
