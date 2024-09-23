def IsPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve(s):
    l = len(s)
    cnt = 0
    for i in s:
        if IsPrime(int(i)):
            cnt += 1
    if IsPrime(l) and cnt > int(l/2):
        return 'YES'
    return 'NO'
for i in range(int(input())):
    print(solve(input()))