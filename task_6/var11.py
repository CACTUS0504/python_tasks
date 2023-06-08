sols = ([1999, 'BOO', 1969, ''],
        [1999, 'BOO', 1986, ''],
        [1999, 'BOO', 2000, ''],
        [1999, 'NIX', '', 1992],
        [1999, 'NIX', '', 1987],
        [1999, 'NIX', '', 1986],
        [1985, 'BOO', 1969, ''],
        [1985, 'BOO', 1986, ''],
        [1985, 'BOO', 2000, ''],
        [1985, 'NIX', '', 1992],
        [1985, 'NIX', '', 1987],
        [1985, 'NIX', '', 1986])


def check(arr1, arr2):
    for i in range(len(arr1)):
        if arr2[i] == '':
            continue
        if arr1[i] != arr2[i]:
            return False
    return True


def main(x):
    tmp = 0
    res = 0
    for i in range(len(sols)):
        if check(x, sols[i]):
            return i


print(main([1999, 'NIX', 2000, 1992]))
print(main([1985, 'NIX', 1986, 1987]))
print(main([1985, 'BOO', 2000, 1986]))
print(main([1985, 'BOO', 1969, 1992]))
print(main([1985, 'NIX', 1986, 1986]))