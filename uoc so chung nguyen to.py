from math import *
def check(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def tong(n):
    s = 0
    while n > 0:
        s = s + n%10
        n //= 10
    return s

for i in range(int(input())):
    a= int(input())
    b = int(input())
    x = gcd(a, b)
    if check(tong(x)):
        print('YES')
    else:
        print('NO')