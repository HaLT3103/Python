n = int(input())
a = list(map(float, input().split()))
a.sort()
x = a[0]
y = a[n - 1]
s = 0.0
for i in a:
    if i != x and i != y:
        s += i;
print("%.2f" % (s / (n - a.count(x) - a.count(y))))