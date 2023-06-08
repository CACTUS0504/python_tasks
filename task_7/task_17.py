def main(s):
    s = int(s, base = 16)
    j1 = 2 ** 5 - 1
    j3 = 2 ** 15 - 2 ** 12
    j4 = 2 ** 24 - 2 ** 15

    return hex((j1 & s) | (j3 & s) << 9 | (j4 & s) >> 3)

print(main('0x14a631'))
print(main('0x5d996e'))
print(main('0x9e506'))
print(main('0x956c5d'))