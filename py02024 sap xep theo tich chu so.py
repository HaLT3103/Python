def tich(n):
    s = 1
    while n > 0:
        s = s * (n % 10)
        n //= 10
    return s
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key= lambda x:(tich(x), x))
    for j in a:
        print(j, end=' ')
    print('')