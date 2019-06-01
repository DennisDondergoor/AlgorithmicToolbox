# Uses python3
import sys

import numpy as np


def get_optimal_value(c, w, v):
    value = 0
    w = np.array(w)
    v = np.array(v) / w
    ind = np.argsort(-v)
    v = np.array(v)[ind]
    w = np.array(w)[ind]
    for i in range(len(v)):
        if c == 0:
            return value
        else:
            b = min(w[i], c)
            value = value + b * v[i]
            c = c - b
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
