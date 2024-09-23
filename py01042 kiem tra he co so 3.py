def solve(s):
    cnt = 0
    for i in s:
        if i == '0' or i == '1' or i == '2':
            cnt += 1
    if cnt == len(s):
        return 'YES'
    return 'NO'
for i in range(int(input())):
    print(solve(input()))