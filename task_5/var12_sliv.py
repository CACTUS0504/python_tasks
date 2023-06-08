import math


def main(z, y, x):
    n = len(z)
    z = [0] + z
    y = [0] + y
    x = [0] + x
    res = 0
    for i in range(1, n + 1):
        res += 80 * pow((math.ceil(55 * pow(y[n + 1 - i], 3) - pow(x[n+1-i], 2) - z[n + 1 - i])), 7)
    return res * 45


print(main([0.02, 0.18, -0.92], [0.89, 0.1, 0.09], [0.97, 0.43, -0.97]))
