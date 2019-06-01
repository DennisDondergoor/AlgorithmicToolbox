# Uses python3
import sys


def pisano(m):
    previous = 0
    current = 1
    i = 0
    while True:
        previous, current = current, (previous + current) % m
        i += 1
        if previous == 0:
            if current == 1:
                return i


def fib_mod(n, m):
    n = n % pisano(m)
    previous = 0
    current = 1
    if n < 2:
        return n
    else:
        for i in range(2, n + 1):
            previous, current = current, (previous + current) % m
    return current


def fibonacci_sum(c):
    if c <= 1:
        return c
    return (fib_mod(c + 2, 10) - 1) % 10


def fibonacci_partial_sum(j, k):
    if j == 0:
        return fibonacci_sum(k)
    elif j == k:
        return fib_mod(j, 10)
    else:
        return (fibonacci_sum(k) - fibonacci_sum(j - 1)) % 10


if __name__ == '__main__':
    inp = sys.stdin.read()
    x, y = map(int, inp.split())
    print(fibonacci_partial_sum(x, y))
