# Uses python3
from numpy import inf


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def min_and_max(i, j, operands, m, M):
    minimum = inf
    maximum = -inf
    for k in range(i, j):
        a = evalt(M[i][k], M[k + 1][j], operands[k])
        b = evalt(M[i][k], m[k + 1][j], operands[k])
        c = evalt(m[i][k], M[k + 1][j], operands[k])
        d = evalt(m[i][k], m[k + 1][j], operands[k])
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    return minimum, maximum


def get_maximum_value(dataset):
    numbers = dataset[0::2]
    operands = dataset[1::2]
    n = len(numbers)

    m = [[0 for _ in range(n)] for _ in range(n)]
    M = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        m[i][i] = int(numbers[i])
        M[i][i] = int(numbers[i])

    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(i, j, operands, m, M)

    return M[0][n - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
