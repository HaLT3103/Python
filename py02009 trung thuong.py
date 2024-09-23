def solve():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a.sort()
    b = [0] * n
    for i in range(n):
        b[i] = a.count(a[i])
    b.sort()
    for i in a:
        if a.count(i) == b[n-1]:
            return(i)
            break

for i in range(int(input())):
    print(solve())