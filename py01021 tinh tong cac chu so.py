for i in range(int(input())):
    s = input()
    t = 0
    a = []
    for i in s:
        if not i.isdigit():
            a.append(i)
        else:
            t += int(i)
    a.sort()
    for i in a:
        print(i, end='')
    print(t)