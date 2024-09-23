def check1(s):
    n = int(s)
    t = 0
    while n > 0:
        t += n%10
        n //= 10
    if t % 10 == 0:
        return True
    return False

def check2(s):
    l = len(s)
    for i in range(1, l):
        if abs(int(s[i]) - int(s[i-1])) != 2:
            return False
    return True

for i in  range(int(input())):
    s = input()
    if check1(s) and check2(s):
        print('YES')
    else:
        print('NO')