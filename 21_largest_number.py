# Uses python3

import sys


def is_greater_or_equal(x, y):
    x = int(x)
    y = int(y)
    p = y + x * 10 ** (len(str(y)))
    q = x + y * 10 ** (len(str(x)))
    return p >= q


def largest_number(digits):
    res = ""
    while digits:
        max_digit = 0
        for digit in digits:
            if is_greater_or_equal(digit, max_digit):
                max_digit = digit
        res += max_digit
        digits.remove(max_digit)
    return res


if __name__ == '__main__':
    inp = sys.stdin.read()
    data = inp.split()
    a = data[1:]
    print(largest_number(a))
