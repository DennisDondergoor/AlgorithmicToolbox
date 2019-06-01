# Uses python3
import sys


def optimal_sequence(n):
    v = [0] * (n + 1)
    for i in range(1, n + 1):
        indices = [i - 1]
        if i % 2 == 0:
            indices.append(i // 2)
        if i % 3 == 0:
            indices.append(i // 3)
        min_v = min([v[x] for x in indices])
        v[i] = min_v + 1
    pt = n
    solution = [pt]
    while pt != 1:
        candidates = [pt - 1]
        if pt % 2 == 0:
            candidates.append(pt // 2)
        if pt % 3 == 0:
            candidates.append(pt // 3)
        pt = min([(c, v[c]) for c in candidates], key=lambda x: x[1])[0]
        solution.append(pt)
    return reversed(solution)


inp = sys.stdin.read()
n = int(inp)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
