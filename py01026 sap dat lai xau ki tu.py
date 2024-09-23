def solve(s1, s2):
    a = []
    b = []
    for i in s1:
        a.append(i)
    for i in s2:
        b.append(i)
    a.sort()
    b.sort()
    if a == b:
        return 'YES'
    else:
        return 'NO'
for i in range(int(input())):
    s1 = input()
    s2 = input()
    print('Test ', end='')
    print(i + 1, end=': ')
    print(solve(s1, s2))