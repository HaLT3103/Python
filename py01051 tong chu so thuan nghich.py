def tong(s):
    sum = 0
    for i in s:
        sum += int(i)
    return sum
def solve(s):
    n = tong(s)
    if n < 10:
        return 'NO'
    s1 = str(n)
    if s1 == s1[::-1]:
        return 'YES'
    return 'NO'

for i in range(int(input())):
    print(solve(input()))