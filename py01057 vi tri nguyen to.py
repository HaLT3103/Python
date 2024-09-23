def IsPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve(s):
    for i in range(len(s)):
        if IsPrime(i) and not IsPrime(int(s[i])):
            return 'NO'
        if not IsPrime(i) and IsPrime(int(s[i])):
            return 'NO'
    return "YES"

for i in range(int(input())):
    print(solve(input()))