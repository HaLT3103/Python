def check(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
b = {}
for i in a:
    if check(i):
        if i not in b:
            b[i] = 1
        else:
            b[i] += 1
for x, y in b.items():
    print(x, end=' ')
    print(y)