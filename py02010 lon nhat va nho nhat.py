while True:
    n = int(input())
    if n == 0:
        break
    a = []
    for i in range(n):
        a.append(input().lstrip('0'))
    a.sort()
    if a[0] == a[n - 1]:
        print('BANG NHAU')
    else:
        print(a[0], end= ' ')
        print(a[n - 1])