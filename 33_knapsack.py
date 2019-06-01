# Uses python3

import sys


def knapsack(w, W):
    memo = {}

    def best_value(i, j):
        key = (i, j)
        if key in memo:
            return memo[key]
        if i == 0:
            memo[key] = 0
            return 0
        value = w[i - 1]
        if value > j:
            memo[key] = best_value(i - 1, j)
            return memo[key]
        else:
            memo[key] = max(best_value(i - 1, j), best_value(i - 1, j - value) + value)
            return memo[key]

    j = W
    for i in range(len(w), 0, -1):
        if best_value(i, j) != best_value(i - 1, j):
            j -= w[i - 1]
    return best_value(len(w), W)


if __name__ == '__main__':
    inp = sys.stdin.read()
    data = list(map(int, inp.split()))
    W, n, *w = list(map(int, inp.split()))
    print(knapsack(w, W))
