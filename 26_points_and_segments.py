# Uses python3
import sys


def fast_count_segments(starts, ends, points):
    lst = []
    for i in starts:
        lst.append([i, "u"])
    for i in ends:
        lst.append([i, "w"])
    for i in points:
        lst.append([i, "v"])
    lst.sort()
    cnt = []
    d = {}
    j = 0
    for i in range(len(lst)):
        if lst[i][1] == "u":
            j += 1
        if lst[i][1] == "w":
            j -= 1
        if lst[i][1] == "v":
            d[lst[i][0]] = j
    for i in p:
        cnt.append(d[i])
    return cnt


if __name__ == '__main__':
    inp = sys.stdin.read()
    data = list(map(int, inp.split()))
    n = data[0]
    m = data[1]
    s = data[2:2 * n + 2:2]
    e = data[3:2 * n + 2:2]
    p = data[2 * n + 2:]
    count = fast_count_segments(s, e, p)
    for x in count:
        print(x, end=' ')
