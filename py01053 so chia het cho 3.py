def tong(s):
    sum = 0
    for i in s:
        sum += int(i)
    return sum

def solve(s):
    if tong(s) % 3 == 0:
        return 'YES'
    return 'NO'

for i in range(int(input())):
    print(solve(input()))