import numpy as np


def array_info(array: np.ndarray) -> None:
    print(f"ndim: {array.ndim}")
    print(f"shape: {array.shape}")
    print(f"size: {array.size}")
    print(f"dtype: {array.dtype}")
    print(f"values:\n{array}\n")

if __name__ == '__main__':
    # my_np_array = np.array([1, 2, 3.14, 5, 4, 3], dtype="float32")
    # my_np_array = np.zeros(shape=(3, 5), dtype=float)
    # my_np_array = np.arange(start=0, stop=20, step=2)
    my_np_array = np.linspace(start=0, stop=1, num=5)
    array_info(my_np_array)

    print("====")

    # my_rand_array = np.random.randint(low=0, high=10, size=(3, 3)) # high not inclusive
    my_rand_array = np.random.random(size=(3, 3)) # gaussian
    array_info(my_rand_array)
