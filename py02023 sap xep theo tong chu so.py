def tong(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key= tong)
    for j in a:
        print(j, end=" ")
    print('')