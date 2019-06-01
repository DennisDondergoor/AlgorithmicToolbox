# Uses python3
import sys


def merge_sort(a):
    if len(a) <= 1:
        return a, 0
    count_both = 0
    mid = len(a) // 2
    left_half = a[:mid]
    right_half = a[mid:]
    left_half, count_l = merge_sort(left_half)
    right_half, count_r = merge_sort(right_half)
    i = 0
    j = 0
    k = 0
    b = [0] * len(a)
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            b[k] = left_half[i]
            i = i + 1
            k = k + 1
        else:
            b[k] = right_half[j]
            count_both += len(left_half) - i
            j = j + 1
            k = k + 1
    while i < len(left_half):
        b[k] = left_half[i]
        i = i + 1
        k = k + 1
    while j < len(right_half):
        b[k] = right_half[j]
        j = j + 1
        k = k + 1
    count = count_l + count_r + count_both
    return b, count


if __name__ == '__main__':
    inp = sys.stdin.read()
    n, *num_list = list(map(int, inp.split()))
    print(merge_sort(num_list)[1])
