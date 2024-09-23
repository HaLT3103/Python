def solve():
    s = input()
    if s[0] == s[len(s) - 1]:
        return 'YES'
    return 'NO'
for i in range(int(input())):
    print(solve())