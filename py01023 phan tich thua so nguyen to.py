import math


def nto(n):
    s = "1"
    for i in range(2, n):
        t = 0
        while n % i == 0:
            t += 1
            n /= i
        if t != 0:
            s += ' * ' + str(i) + '^' + str(t)
    return s

t = int(input())
for _ in range(t):
    n = int(input())
    print(nto(n))