def solve():
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(d, n):
        print(a[i], end=" ")
    for i in range(d):
        print(a[i], end=" ")
    return ('')
for i in range(int(input())):
    print(solve())