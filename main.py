import math


def main(y):
    n = len(y)
    res = 0
    y = [0] + y

    for i in range(1, n + 1):
        res += 26 * (1 - 20 * (y[n + 1 - math.ceil(i / 4)]) ** 2) ** 3
    return res


print(main([0.21, -0.01, 0.91]))