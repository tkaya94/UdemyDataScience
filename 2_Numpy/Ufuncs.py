from typing import Iterable
import numpy as np
np.random.seed(0)


def reciprocal(values: Iterable[float]) -> Iterable[float]:
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output


small_array = np.random.randint(low=1, high=10, size=5)
# print(reciprocal(small_array))
