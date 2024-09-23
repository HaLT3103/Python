
n = int(input())
a = list(map(int, input().split()))
x = 0
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if a[i] % 2 == 0 and a[j] % 2 == 0 and a[i] > a[j]:
            x = a[i]
            a[i] = a[j]
            a[j] = x
        if a[i] % 2 == 1 and a[j] % 2 == 1 and a[i] < a[j]:
            x = a[i]
            a[i] = a[j]
            a[j] = x
for i in a:
    print(i, end=' ')