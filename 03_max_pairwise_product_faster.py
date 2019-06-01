# Uses python3


def max_pairwise_product_faster(a):
    n = len(a)
    index = 0
    for i in range(n):
        if a[i] > a[index]:
            index = i
    a[index], a[n - 1] = a[n - 1], a[index]
    index = 0
    for i in range(n - 1):
        if a[i] > a[index]:
            index = i
    a[index], a[n - 2] = a[n - 2], a[index]
    return a[n - 2] * a[n - 1]


if __name__ == '__main__':
    input_n = int(input())
    numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_faster(numbers))
