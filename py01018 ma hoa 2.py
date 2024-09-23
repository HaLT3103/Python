p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    k, s = map(str, input().split())
    if k[0] == '0':
        break
    res = ""
    for i in s:
        index = (p.index(i) + int(k)) % 28
        res += p[index]
    print(res[::-1])
