from random import randint


def max_pairwise_product_naive(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])
    return max_product


def max_pairwise_product_faster(numbers):
    n = len(numbers)
    index = 0
    for i in range(n):
        if numbers[i] > numbers[index]:
            index = i
    numbers[index], numbers[n - 1] = numbers[n - 1], numbers[index]
    index = 0
    for i in range(n - 1):
        if numbers[i] > numbers[index]:
            index = i
    numbers[index], numbers[n - 2] = numbers[n - 2], numbers[index]
    return numbers[n - 2] * numbers[n - 1]


def stress_test(x, y):
    while True:
        n = randint(2, x)
        a = []
        for i in range(n):
            a.append(randint(2, y))
        print(a)
        result1 = max_pairwise_product_naive(a)
        result2 = max_pairwise_product_faster(a)
        if result1 == result2:
            print("OK")
        else:
            print("Wrong answer: ", result1, result2)


if __name__ == '__main__':
    p, q = map(int, input().split())
    stress_test(p, q)
