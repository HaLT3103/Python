from math import *
def solve(s):
    a = int(s)
    b = int(s[::-1])
    if gcd(a, b) == 1:
        print('YES')
    else:
        print('NO')

for i in range(int(input())):
    solve(input())