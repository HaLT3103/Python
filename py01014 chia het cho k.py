a, k, n = map(int, input().split())
x = int(a / k)
y = int(n / k)
if x >= y:
    print('-1')
else:
    for i in range(x + 1, y + 1):
        print(k * i - a, end=' ')