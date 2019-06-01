# Uses python3
import sys


def fibonacci_sum_squares(n):
    if n <= 1:
        return n
    if n % 30 == 0:
        return 0
    else:
        n = n % 30
    previous = 0
    current = 1
    prod = 1

    for _ in range(n - 1):
        previous, current, prod = current, (previous + current) % 10, (previous + current) * (
                previous + 2 * current) % 10
    return prod % 10


if __name__ == '__main__':
    inp = sys.stdin.read()
    x = int(inp)
    print(fibonacci_sum_squares(x))
