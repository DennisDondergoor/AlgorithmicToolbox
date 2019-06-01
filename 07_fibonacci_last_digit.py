# Uses python3


def calc_fib(n):
    f = []
    if n >= 0:
        f.append(0)
    if n >= 1:
        f.append(1)
    if n >= 2:
        for i in range(2, n + 1):
            f[i] = (f[i - 1] + f[i - 2]) % 10
    return f[n]


m = int(input())
print(calc_fib(m))
