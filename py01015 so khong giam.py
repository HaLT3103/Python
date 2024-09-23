def check(s):
    l = len(s)
    for i in range(l - 1):
        if s[i] > s[i + 1]:
            return False
    return True

t = int(input())
while t > 0:
    s = input()
    if check(s):
        print('YES')
    else:
        print('NO')
    t -= 1

