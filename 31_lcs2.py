# Uses python3
import sys


def lcs2(s, t):
    m = len(s)
    n = len(t)
    c = {}
    for i in range(-1, m):
        c[i, -1] = 0
    for j in range(-1, n):
        c[-1, j] = 0
    for i in range(m):
        for j in range(n):
            if s[i] == t[j]:
                c[i, j] = c[i - 1, j - 1] + 1
            else:
                c[i, j] = max(c[i - 1, j], c[i, j - 1])
    return c[m - 1, n - 1]


if __name__ == '__main__':
    inp = sys.stdin.read()
    data = list(map(int, inp.split()))
    n = data[0]
    data = data[1:]
    a = data[:n]
    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]
    print(lcs2(a, b))
