# Uses python3
import sys


def optimal_summands(n):
    s = []
    i = 1
    while n > 0:
        if n >= 2 * i + 1:
            s.append(i)
            n -= i
            i += 1
        else:
            s.append(n)
            return s
    return s


if __name__ == '__main__':
    inp = sys.stdin.read()
    m = int(inp)
    summands = optimal_summands(m)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
