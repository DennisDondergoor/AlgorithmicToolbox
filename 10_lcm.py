# Uses python3
import sys


def gcd_fast(a, b):
    if b == 0:
        return a
    return gcd_fast(b, a % b)


if __name__ == "__main__":
    inp = sys.stdin.read()
    x, y = map(int, inp.split())
    print(x // gcd_fast(x, y) * y)
