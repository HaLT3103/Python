def IsPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve(s):
    l = len(s)
    t = ''
    p = ''
    t += s[l-3] + s[l-2] + s[l-1]
    p += s[0] + s[1] + s[2]
    if IsPrime(int(t)) and IsPrime(int(p)):
        return 'YES'
    return 'NO'

for i in range(int(input())):
    print(solve(input()))