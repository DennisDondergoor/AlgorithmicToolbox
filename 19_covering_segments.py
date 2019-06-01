# Uses python3
import sys


def optimal_points(segments):
    pts = []
    while segments:
        point = min(s[1] for s in segments)
        pts.append(point)
        t = []
        for s in segments:
            if s[0] > point:
                t.append(s)
        segments = t
    return pts


if __name__ == '__main__':
    inp = sys.stdin.read()
    n, *data = map(int, inp.split())
    segm = list(map(lambda x: (x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segm)
    print(len(points))
    for p in points:
        print(p, end=' ')
