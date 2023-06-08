def main(s):
    s = int(s)
    t1 = 2 ** 5 - 1
    t2 = 2 ** 8 - 2 ** 5
    t3 = 2 ** 14 - 2 ** 8
    t4 = 2 ** 16 - 2 ** 14
    res = {'T1': s & t1, 'T2': (s & t2) >> 5, 'T3': (s & t3) >> 8, 'T4': (s & t4) >> 14}
    return res


print(main('58675'))

