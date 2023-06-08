def main(s):
    h1 = int(s[0][1])
    h3 = int(s[1][1])
    h4 = int(s[2][1])
    print(h3)

    return int(h1 | h3 << 10 | h4 << 12)

print(main([('H1', '115'), ('H3', '0'), ('H4', '103')]))