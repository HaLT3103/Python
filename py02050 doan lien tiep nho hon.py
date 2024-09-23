for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print('1', end=' ')
    for i in range(1, n):
        x = 1
        l = i
        while a[l] >= a[l-1] and l > 0:
            l -= 1
            x += 1
        print(x, end=' ')
    print('')

'''
1
7
100 80 60 70 60 75 85
'''