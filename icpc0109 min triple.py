def solve():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                x = a[i]
                a[i] = a[j]
                a[j] = x
    return a[0] + a[1] + a[2]
for i in range(int(input())):
    print(solve())