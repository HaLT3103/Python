def solve(s):
    l = len(s)
    if l % 2 == 0:
        return 'NO'
    if s[0] == s[1]:
        return 'NO'
    for i in range(2, l, 2):
        if s[0] != s[i]:
            return ('NO')
    return 'YES'

for i in range(int(input())):
    print(solve(input()))