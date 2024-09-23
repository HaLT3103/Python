def IsPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def dao(n):
    s = str(n)
    s1 = s[::-1]
    if IsPrime(int(s1)):
        return True
    return False

def tong(n):
    s = str(n)
    t = 0
    for i in s:
        if not IsPrime(int(i)):
            return False
        t += int(i)
    if IsPrime(t):
        return True
    return False


def solve():
    n = int(input())
    if IsPrime(n) and dao(n) and tong(n):
        return 'Yes'
    return 'No'

for i in range(int(input())):
    print(solve())