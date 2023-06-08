def main(s):
    s = int(s, base=16)
    w1 = 2 ** 2 - 1
    w2 = 2 ** 12 - 2 ** 2
    w4 = 2 ** 25 - 2 ** 20
    return str(int((w1 & s) << 23 | (w2 & s) << 11 | (w4 & s) >> 20))

