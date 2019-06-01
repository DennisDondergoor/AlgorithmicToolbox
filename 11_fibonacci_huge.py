# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = [current, previous + current]

    return current % m


if __name__ == '__main__':
    inp = sys.stdin.read()
    x, y = map(int, inp.split())
    print(get_fibonacci_huge_naive(x, y))
