def main(s):
    s = s.replace('option', '') \
         .replace('array', '') \
         .replace('q(', '') \
         .replace('(', '') \
         .replace(')', '')
    res = []
    pairs = s.split('||;')
    pairs.pop()
    for item in pairs:
        item = item.replace('||', '')
        item = item.replace(' ', '')
        item = item.replace('.', '')
        vals_key = item.split('=>')
        vals = vals_key[0].split(';')
        pair = (vals_key[1], vals)
        res.append(pair)
    return res


print(main(' || option array( erus_981 ; usxe) =>q(arxeso_423). ||; ||option array(raan; onrain_135; eden_649; maso_394) => q(isorre). ||; '))