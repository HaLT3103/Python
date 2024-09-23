def solve():
    s = list(map(str, input().split('.')))
    for i in s:
        if int(i) < 0 or int(i) > 255:
            return "NO"
    return "YES"
for _ in range(int(input())):
    print(solve())