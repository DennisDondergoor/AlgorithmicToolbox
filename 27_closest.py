# Uses python3
import math
import sys


def dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def brute(ax):
    mi = dist(ax[0], ax[1])
    p1 = ax[0]
    p2 = ax[1]
    ln_ax = len(ax)
    if ln_ax == 2:
        return p1, p2, mi
    for i in range(ln_ax - 1):
        for j in range(i + 1, ln_ax):
            if i != 0 and j != 1:
                d = dist(ax[i], ax[j])
                if d < mi:
                    mi = d
                    p1, p2 = ax[i], ax[j]
    return p1, p2, mi


def closest_split_pair(p_x, p_y, delta, best_pair):
    ln_x = len(p_x)
    mx_x = p_x[ln_x // 2][0]
    s_y = [x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]
    best = delta
    ln_y = len(s_y)
    for i in range(ln_y - 1):
        for j in range(i + 1, min(i + 7, ln_y)):
            p, q = s_y[i], s_y[j]
            dst = dist(p, q)
            if dst < best:
                best_pair = p, q
                best = dst
    return best_pair[0], best_pair[1], best


def closest_pair(ax, ay):
    ln_ax = len(ax)
    if ln_ax <= 3:
        return brute(ax)
    mid = ln_ax // 2
    qx = ax[:mid]
    rx = ax[mid:]
    midpoint = ax[mid][0]
    qy = list()
    ry = list()
    for x in ay:
        if x[0] <= midpoint:
            qy.append(x)
        else:
            ry.append(x)
    (p1, q1, mi1) = closest_pair(qx, qy)
    (p2, q2, mi2) = closest_pair(rx, ry)
    if mi1 <= mi2:
        d = mi1
        mn = (p1, q1)
    else:
        d = mi2
        mn = (p2, q2)
    (p3, q3, mi3) = closest_split_pair(ax, ay, d, mn)
    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3


def minimum_distance(x, y):
    a = list(zip(x, y))
    ax = sorted(a, key=lambda x: x[0])
    ay = sorted(a, key=lambda x: x[1])
    p1, p2, mi = closest_pair(ax, ay)
    return math.sqrt(mi)


if __name__ == '__main__':
    inp = sys.stdin.read()
    data = list(map(int, inp.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
