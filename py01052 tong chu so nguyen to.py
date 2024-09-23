fdef IsPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def tong(s):
    sum = 0
    for i in s:
        sum += int(i)
    return sum

def solve(s):
    if IsPrime(tong(s)):
        return 'YES'
    return 'NO'

or i in range(int(input())):
    print(solve(input()))