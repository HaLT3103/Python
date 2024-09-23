def solve():
    s = input()
    for i in s:
        if i != '6' and i != '8':
            return 'NO'
    for i in range(len(s) - 2):
        if s[i] == '8' and s[i + 1] == '8' and s[i + 2] == '8':
            return 'NO'
    return 'YES'
print(solve())