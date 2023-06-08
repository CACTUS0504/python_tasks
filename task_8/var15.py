def main(s):
    # Заменяю все служебные строки на пустые, но equ может быть как служебным, так и в контенте
    s = s.replace('done', '')\
        .replace('<block>', '')\
        .replace('</block>', '')\
        .replace('do', '')
    # Делаю массив пар и потом в каждой паре удаляю все символы вне скобок, чтобы корректно удалить equ
    pairs = s.split(';')
    res = {}
    pairs.pop()
    for i in pairs:
        i = i.replace('global', '')
        i = i.replace(' ', '')
        i = i.replace('#', '')
        i = i.replace('q(', '')
        i = i.replace(')', '')
        key_val = i.split('|>')
        pair = (key_val[0], key_val[1])
        res[key_val[1]] = key_val[0]
    return res

print(main('do <block> global #-9066|> q(isbive_121) </block>; <block>global#4237 |> q(rite_577)</block>;<block> global#8167 |> q(inle)</block>;done'))
print(main('do <block> global #2255 |> q(indi) </block>;<block> global#-7097|>q(edusin_615) </block>; <block> global #-5816 |> q(dila)</block>; done'))
