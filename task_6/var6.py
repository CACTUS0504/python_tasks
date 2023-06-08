sols = (['OPAL', 'E', 1987, ''],
        ['ROUGE', 'E', 1987, ''],
        ['ADA', 'E', 1987, ''],
        ['', 'E', 1994, 'EC'],
        ['', 'E', 1994, 'LSL'],
        ['', 'E', 1994, 'GOSU'],
        ['', 'STATA', 1987, 'EC'],
        ['', 'STATA', 1994, 'EC'],
        ['', 'STATA', 1987, 'LSL'],
        ['', 'STATA', 1994, 'LSL'],
        ['', 'STATA', '', 'GOSU'])


def check(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] != arr2[i] and arr2[i] != '':
            return False
    return True


def main(x):
    for i in range(len(sols)):
        if check(x, sols[i]):
            return i

print(main(['ADA', 'STATA', 1994, 'GOSU']))
print(main(['OPAL', 'STATA', 1987, 'LSL']))
print(main(['ROUGE', 'E', 1987, 'EC']))
print(main(['ADA', 'E', 1987, 'LSL']))
print(main(['ADA', 'STATA', 1987, 'EC']))