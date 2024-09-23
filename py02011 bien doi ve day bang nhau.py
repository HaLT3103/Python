n = int(input())
a = list(map(int, input().split()))
a.sort()
t = 0
for i in a:
    t += i
c = float(t / n)
print(c)
k = a[0]
for i in range(1, n):
    if abs(c - a[i]) < abs(c - k):
        k = a[i]
print(k)