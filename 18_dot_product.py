# Uses python3
import sys

import numpy as np


def max_dot_product(x, y):
    x = -np.sort(-np.array(x))
    y = -np.sort(-np.array(y))
    return np.dot(x, y)


if __name__ == '__main__':
    inp = sys.stdin.read()
    data = list(map(int, inp.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
