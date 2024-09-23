def solve(a, n ,m):
    max_value = max(map(max, a))
    min_value = min(map(min, a))
    print(max_value - min_value)
    check = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == max_value - min_value:
                check += 1
                print("Vi tri [", end= "")
                print(i, end= "")
                print("][", end= "")
                print(j, end= "")
                print(']')
    if check == 0:
        print("NOT FOUND")

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
solve(a, n, m)

'''
6 4
23 21 77 10
13 13 22 14
28 67 28 23
29 77 11 67
16 51 24 21
13 25 77 77
'''