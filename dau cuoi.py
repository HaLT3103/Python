for i in range(int(input())):
    s = input()
    l = len(s)
    s1 = s[0] + s[1]
    s2 = s[l-2] + s[l-1]
    if s1 == s2:
        print('YES')
    else:
        print('NO')