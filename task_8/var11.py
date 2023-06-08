def main(s):
    # Заменяю все служебные строки на пустые, но equ может быть как служебным, так и в контенте
    s = s.replace('::=', ':')\
        .replace('<<', '')\
        .replace('\n', '')\
        .replace('local', '')\
        .replace('end >>', '') \
        .replace('end>>', '') \
        .replace('begin', '') \
        .replace('#', '')
    # Делаю массив пар и потом в каждой паре удаляю все символы вне скобок, чтобы корректно удалить equ
    pairs = s.split('end')
    res = []
    for i in pairs:
        i = i.replace(' ', '')
        key_val = i.split(':')
        pair = (key_val[0], key_val[1])
        res.append(pair)
    return res

print(main('<<begin local leso ::=#-6465 end begin local gebe ::=#5855 end begin local oratve ::=#-658 end >>'))
