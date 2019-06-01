# Uses python3
import sys


def edit_distance(s, t):
    m = len(s) + 1
    n = len(t) + 1
    tbl = {}
    for i in range(m):
        tbl[i, 0] = i
    for j in range(n):
        tbl[0, j] = j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s[i - 1] == t[j - 1] else 1
            tbl[i, j] = min(tbl[i, j - 1] + 1, tbl[i - 1, j] + 1, tbl[i - 1, j - 1] + cost)
    return tbl[m - 1, n - 1]


if __name__ == "__main__":
    inp = sys.stdin.read()
    s, t = inp.split()
    print(edit_distance(s, t))
