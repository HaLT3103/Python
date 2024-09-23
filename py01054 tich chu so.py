def Mul(s):
    t = 1
    for i in s:
        if i != '0':
            t *= int(i)
    return t

for i in range(int(input())):
    print(Mul(input()))