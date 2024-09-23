
n = int(input())
a = []
for i in range(n):
    a.append(str(input()))
row = [0] * n
column = [0] * n
for i in range(n):
    for j in range(n):
        if a[i][j] == 'C':
            row[i] += 1
            column[j] += 1
t = 0
for i in row:
    t += i * (i - 1) / 2
for i in column:
    t += i * (i - 1) / 2
print(int(t))