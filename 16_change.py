# Uses python3
import sys


def get_change(m):
    num_coins = 0
    q, r = divmod(m, 10)
    num_coins += q
    if r != 0:
        q, r = divmod(r, 5)
        num_coins += (q + r)
    return num_coins


if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))
