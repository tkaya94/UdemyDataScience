import numpy as np
np.random.seed(0)

from NumpyIntro import array_info


def compare_array(a1: np.ndarray, a2: np.ndarray) -> None:
    print(a1)
    print(a2)


x = np.arange(4).reshape((2, 2))
array_info(x)

x_moved = np.moveaxis(x, source=0, destination=1)
compare_array(x, x_moved)

print("=====")

x_rolled = np.roll(x, axis=1, shift=-1)
compare_array(x, x_rolled)

print("=====")

y = np.random.randint(low=-10, high=10, size=10)
y_sorted = np.sort(y)
compare_array(y, y_sorted)

y_sorted = np.argsort(y)
compare_array(y, y_sorted)

y_argmax = np.argmax(y)
y_argmin = np.argmin(y)
print(y_argmax, y_argmin)
