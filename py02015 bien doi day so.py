while True:
    a = list(map(int, input().split()))
    if a.count(0) == 4:
        break
    cnt = 0
    while True:
        cnt += 1
        for i in range(3):
            a[i] = abs(a[i] - a[i+1])
        a[3] = abs(a[3] - a[0])
        if a.count(a[0]) == 4:
            break
    print(cnt)