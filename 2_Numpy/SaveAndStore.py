import numpy as np
np.random.seed(0)


def strctured_array_info(array: np.ndarray) -> None:
    print(f"ndim: {array.ndim}")
    print(f"shape: {array.shape}")
    print(f"size: {array.size}")
    print(f"dtype: {array.dtype}")
    print(f"names: {array.dtype.names}")
    print(f"field: {array.dtype.fields}")
    print(f"values:\n{array}\n")


with open('data/test2.npy', 'wb') as f:
    np.save(f, np.array([1, 2]))
    np.save(f, np.array([1, 3]))

with open('data/test2.npy', 'rb') as f:
    a = np.load(f)
    b = np.load(f)

print(a)

x = np.array(
    [
        ('jan', 9, 81.0),
        ('Peter', 3, 27.0)
    ],
    dtype=[
        ('name', 'U10'),
        ('age', 'i4'),
        ('weight', 'f4')
        ]
)
strctured_array_info(x)
