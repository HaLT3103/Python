while True:
    if input() == '-1':
        break
    l, r = map(int, input().split())
    n = int(input())
    cnt = r - l + 1
    for i in range(2, n + 1):
        if l % i == 0:
            cnt += 1
        else:
            cnt = cnt - (r//i - l//i)
    print(cnt)