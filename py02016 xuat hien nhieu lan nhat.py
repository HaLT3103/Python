def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in a:
        b.append(a.count(i))
    b.sort()
    if b[n-1] <= n / 2:
        return 'NO'
    for i in a:
        if a.count(i) == b[n-1]:
            return i
for i in range(int(input())):
    print(solve())