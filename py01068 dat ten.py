N, k = map(int, input().split())
s = input()
c = s.split()
d = {'0'}
for i in c:
    d.add(i)
d.remove('0')
a = [0] * 50
b = ['0']
for i in d:
    b.append(i)
b.sort()
n = len(b)
def kq():
    s = ''
    for i in range(1, k + 1):
        s += b[int(a[i])] + ' '
    print(s)
def Try(i):
    for j in range(a[i-1] + 1, n - k + 1 + i):
        a[i] = j
        if i == k:
            kq()
        else:
            Try(i + 1)
Try(1)