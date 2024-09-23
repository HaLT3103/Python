def tong(n):
    t = 0
    while n > 0:
        t += n % 10
        n //= 10
    return t

s = input()
n = 0
if s[0] == '-':
    n += - int(s[1])
    for i in range(2,len(s)):
        n += int(s[i])
else:
    for i in s:
        n += int(s[i])
cnt = 1
while n >= 10:
    print(n)
    n = tong(n)
    cnt += 1
print(cnt)