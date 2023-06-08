sols = (['CIRRU', '', 'TLA', 1963, 'LSL'],
        ['SHELL', '', 'TLA', 1963, 'LSL'],
        ['NUMPY', '', 'TLA', 1963, 'LSL'],
        ['', '', 'TLA', 2003, 'LSL'],
        ['', '', 'TLA', 1960, 'LSL'],
        ['', '', 'TLA', '', 'JSON'],
        ['', 2016, 'TLA', '', 'NIX'],
        ['', 1989, 'TLA', '', 'NIX'],
        ['', '', 'LSL', '', ''],
        ['CIRRU', 2016, 'SASS', '', 'LSL'],
        ['CIRRU', 1989, 'SASS', '', 'LSL'],
        ['SHELL', '', 'SASS', '', 'LSL'],
        ['NUMPY', '', 'SASS', '', 'LSL'],
        ['', '', 'SASS', '', 'JSON'],
        ['', '', 'SASS', '', 'NIX'])


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


print(main(['SHELL', 1989, 'TLA', 1960, 'JSON']))
print(main(['CIRRU', 2016, 'LSL', 1963, 'NIX']))
print(main(['CIRRU', 2016, 'SASS', 1963, 'NIX']))
print(main(['NUMPY', 2016, 'SASS', 2003, 'LSL']))
print(main(['SHELL', 2016, 'SASS', 1963, 'LSL']))

print(main(['SHELL', 2016, 'TLA', 1963, 'LSL']))

# МБ выбирает самое длинное решение?