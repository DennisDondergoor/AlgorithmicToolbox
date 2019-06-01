# Uses python3
import sys


def lcs3(a, b, c):
    d = len(a)
    e = len(b)
    f = len(c)
    subs = [[[0 for _ in range(f + 1)] for _ in range(e + 1)] for _ in range(d + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            for k, z in enumerate(c):
                if x == y and y == z:
                    subs[i + 1][j + 1][k + 1] = subs[i][j][k] + 1
                else:
                    subs[i + 1][j + 1][k + 1] = max(subs[i][j + 1][k + 1],
                                                    subs[i + 1][j][k + 1],
                                                    subs[i + 1][j + 1][k])
    return subs[d][e][f]


if __name__ == '__main__':
    inp = sys.stdin.read()
    data = list(map(int, inp.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
