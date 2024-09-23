n = int(input())
a = list(map(int, input().split()))
ok = True
for i in range(1, n + 1):
    if a.count(i)  == 0:
        print(i)
        ok = False
        break
if ok == True:
    print(n + 1)