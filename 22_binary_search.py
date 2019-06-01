# Uses python3
import sys


def binary_search(b, y):
    low, high = 0, len(b) - 1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if y == b[mid]:
            return mid
        elif y < b[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    inp = sys.stdin.read()
    data = list(map(int, inp.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1:n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end=' ')
