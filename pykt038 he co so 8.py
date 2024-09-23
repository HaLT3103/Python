def chuyen(s):
    t = 0
    for i in range(3):
        t += int(s[2 - i]) * (2 ** i)
    return t

s = input()
while len(s) % 3 != 0:
    s = "0" + s
i = 0
while i < len(s):
    res = s[i:i + 3]
    print(chuyen(res), end= "")
    i += 3