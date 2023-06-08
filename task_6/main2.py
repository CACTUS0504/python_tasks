sols = ({1999, 'BOO', 1969},
        {1999, 'BOO', 1986},
        {1999, 'BOO', 2000},
        {1999, 'NIX', 1992},
        {1999, 'NIX', 1987},
        {1999, 'NIX', 1986},
        {1985, 'BOO', 1969},
        {1985, 'BOO', 1986},
        {1985, 'BOO', 2000},
        {1985, 'NIX', 1992},
        {1985, 'NIX', 1987},
        {1985, 'NIX', 1986},)


def main(x):
    x = set(x)
    tmp = 0
    res = 0
    for i in range(len(sols)):
        if not len(sols[i] - x) and tmp < len(sols[i]):
            tmp = len(sols[i])
            res = i
    return res


print(main([1999, 'NIX', 2000, 1992]))
print(main([1985, 'NIX', 1986, 1987]))
print(main([1985, 'BOO', 2000, 1986]))
print(main([1985, 'BOO', 1969, 1992]))
print(main([1985, 'NIX', 1986, 1986]))

# МБ брать не сеты