def main(s):
    s = s.replace('<section>', '')\
        .replace('</section>', '')\
        .replace('|', '')\
        .replace('define', '')\
        .replace('q(', '')\
        .replace(').', '') \
        .replace(' ', '')
    pairs = s.split(';')
    pairs.pop()
    res = {}
    for i in pairs:
        val_key = i.split('=>')
        res[val_key[1]] = int(val_key[0])
    return res

print(main('<section>|define 142 =>q(erte). |; | define 7364 => q(soma). |;|define -6641 => q(esgera_688).|; </section>'))
print(main('<section>| define 971=> q(quanla_662). |; | define -7444 => q(veve).|; | define -7599 => q(aonve). |; </section>'))