# Uses python3
import sys


def get_majority_element(b, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return b[left]
    mid = int(left + (right - left) / 2)
    p = get_majority_element(b, left, mid)
    q = get_majority_element(b, mid, right)
    if p == q:
        return p
    else:
        count = 0
        for i in range(left, right):
            if b[i] == p:
                count += 1
        if count > (right - left) / 2:
            return p
        count = 0
        for i in range(left, right):
            if b[i] == q:
                count += 1
        if count > (right - left) / 2:
            return q
        return -1


if __name__ == '__main__':
    inp = sys.stdin.read()
    n, *a = list(map(int, inp.split()))
    if get_majority_element(a, 0, n) == -1:
        print(0)
    else:
        print(1)
