# Uses python3
import random
import sys


def partition3(b, lo, hi):
    v = b[lo]
    lt = lo
    gt = hi
    i = lo
    while i <= gt:
        if b[i] == v:
            i += 1
        elif b[i] < v:
            b[lt], b[i] = b[i], b[lt]
            lt += 1
            i += 1
        else:
            b[gt], b[i] = b[i], b[gt]
            gt -= 1
    return lt, gt


def randomized_quick_sort(d, left, right):
    if left >= right:
        return
    r = random.randint(left, right)
    d[left], d[r] = d[r], d[left]
    m1, m2 = partition3(d, left, right)
    randomized_quick_sort(d, left, m1 - 1)
    randomized_quick_sort(d, m2 + 1, right)


if __name__ == '__main__':
    inp = sys.stdin.read()
    n, *a = list(map(int, inp.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
