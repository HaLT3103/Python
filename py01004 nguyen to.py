from math import *
def check(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(int(input())):
    cnt = 0
    n = int(input())
    for j in range(1, n):
        if(gcd(j, n) == 1):
            cnt += 1
    if check(cnt) == True:
        print('YES')
    else:
        print('NO')