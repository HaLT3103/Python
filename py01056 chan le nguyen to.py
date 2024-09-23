def IsPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve(s):
    for i in range(len(s)):
        if i % 2 == 0 and int(s[i]) % 2 == 1:
            return 'NO'
        if i % 2 == 1 and int(s[i]) % 2 == 0:
            return 'NO'
    t = 0
    for i in s:
        t += int(i)
    if IsPrime(t):
        return 'YES'
    return 'NO'
for i in range(int(input())):
    print(solve(input()))