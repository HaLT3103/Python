for i in range(int(input())):
    n = input()
    cnt = 0
    for j in range(len(n)):
        if n[j] == '4' or n[j] == '7':
            cnt += 1
    if cnt == len(n):
        print('YES')
    else:
        print('NO')