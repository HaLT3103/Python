from math import *
def solve():
    n = int(input())
    s = str(n)
    t = 0
    for i in s:
        t += factorial(int(i))
    if t == n:
        return 'Yes'
    return 'No'
for i in range(int(input())):
    print(solve())