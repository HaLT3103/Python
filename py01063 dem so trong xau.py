def solve(s, n):
    l1 = len(s)
    l2 = len(str(n))
    cnt = 0
    check = True
    i = 0
    while i < l1 - l2 + 1:
        if check == False:
            i += l2
        res = ''
        res = s[i : i + l2]
        if int(res) == n:
            cnt += 1
            check = False
        i += 1
    return cnt
for i in range(int(input())):
    print(solve(input(), int(input())))