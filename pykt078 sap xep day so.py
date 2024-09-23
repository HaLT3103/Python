for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    max_value = max(a)
    index = a.index(max_value)
    a.insert(index, k)
    for i in a:
        if i < 0:
            print(i, end= " ")
    for i in a:
        if i >= 0:
            print(i, end= " ")
    print()