def tong(s):
    t = 0
    for i in range(len(s)):
        if i % 2 == 0:
            t += int(s[i])
    return t

def tich(s):
    t = 1
    check = False
    for i in range(len(s)):
        if i % 2 == 1:
            if int(s[i]) > 0:
                t *= int(s[i])
                check = True
    if check == True:
        return t
    return 0


for i in range(int(input())):
    s = input()
    print(tong(s), end=' ')
    print(tich(s))