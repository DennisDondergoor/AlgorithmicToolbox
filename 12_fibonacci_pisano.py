# Uses python3
import sys


def pisano(m):
    previous = 0
    current = 1
    i = 0
    while True:
        (previous, current) = (current, (previous + current) % m)
        i += 1
        if previous == 0:
            if current == 1:
                return i


def fib_mod(n, m):
    n = n % pisano(m)
    f = [0] * (n + 1)
    if n >= 0:
        f[0] = 0
    if n >= 1:
        f[1] = 1
    if n >= 2:
        for i in range(2, n + 1):
            f[i] = (f[i - 1] + f[i - 2]) % m
    return f[n]


if __name__ == '__main__':
    inp = sys.stdin.read()
    x, y = map(int, inp.split())
    print(fib_mod(x, y))
