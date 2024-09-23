def solve(s):
    if s[0] == s[1]:
        return 'NO'
    for i in range(len(s)):
        if s[i] != s[i & 1]:
            return 'NO'
    return 'YES'
for i in range(int(input())):
    print(solve(input()))