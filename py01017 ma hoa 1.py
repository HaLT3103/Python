def solve(s):
    l = len(s)
    cnt = 1
    for i in range(l-1):
        if s[i+1] != s[i]:
            print(cnt, end="")
            print(s[i], end="")
            cnt = 1
        else:
            cnt += 1
    print(cnt, end="")
    print(s[l-1])
for i in range(int(input())):
    solve(input())