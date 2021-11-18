import numpy as np
np.random.seed(0)


def array_info(array: np.ndarray) -> None:
    print(f"ndim: {array.ndim}")
    print(f"shape: {array.shape}")
    print(f"size: {array.size}")
    print(f"dtype: {array.dtype}")
    print(f"values:\n{array}\n")


print("=1=")
M = np.zeros(shape=[3, 3])
print(M)

print("=2=")
idxsDiag = np.diag_indices(3)
# print(idxs)
M[idxsDiag] = np.pi
print(M)

print("=3=")
idxsU = np.triu_indices(3, 1)
# print(idxsU)
M[idxsU] = 1
print(M)

print("=4=")
idxsL = np.tril_indices(3, -1)
# print(idxsL)
M[idxsL] = -1
print(M)

print("=5=")
print(np.where(M >= 1))
