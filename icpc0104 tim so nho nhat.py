def solve(s):
    a = []
    tmp = ''
    for i in s:
        if i.isdigit():
            tmp += i
        else:
            if tmp != '':
                a.append(int(tmp))
            tmp = ''
    if tmp != '':
        a.append(int(tmp))
    return min(a)

for i in range(int(input())):
    print(solve(input()))