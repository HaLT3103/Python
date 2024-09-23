def check(s):
    l = len(s)
    if s[l-2] == '8' and s[l-1] == '6':
        return True
    else:
        return False

for i in  range(int(input())):
    if check(input()):
        print('YES')
    else:
        print('NO')