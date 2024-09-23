def solve(s):
    for i in range(0, len(s), 2):
        for j in range(int(s[i+1])):
            print(s[i], end="")
    print('')

t = int(input())
while t > 0:
    s = input()
    solve(s)
    t -= 1
