n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

k = int(input())

nuaTren, nuaDuoi = 0, 0

for i in range(n):
    for j in range(n):
        if j > n - i - 1:
            nuaTren += a[i][j]
        elif j < n - i - 1:
            nuaDuoi += a[i][j]

if abs(nuaTren - nuaDuoi) <= k:
    print('YES')
else:
    print('NO')

print(abs(nuaTren - nuaDuoi))

'''
5
2 8 10 6 7
6 3 2 6 9
10 2 6 2 8
9 9 7 9 8
9 6 5 6 9
5
'''