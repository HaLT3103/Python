n = int(input())
a = []
b = []
for i in range(n):
    a.append(input())
for i in range(1, n):
    s1 = list(map(str, a[i].split()))
    s2 = list(map(str, a[i-1].split()))
    if (len(s1) == 7 and len(s2) == 8) or (len(s1) == 8 and i == n - 1):
        b.append(1)
    if (len(s1) == 6 and len(s2) == 7) or (len(s1) == 7 and i == n - 1):
        b.append(2)
print(len(b))
for i in b:
    print(i)
'''
12
Mot canh hai canh lai ba canh
Tran troc ban khoan giac chang lanh
Canh bon canh nam vua chop mat
Sao vang nam canh mong hon bay
Minh ve minh co nho ta
Muoi lam nam ay thiet tha man nong
Minh ve minh co nho khong
Nhin cay nho nui nhin song nho nguon
Mot canh hai canh lai ba canh
Tran troc ban khoan giac chang lanh
Canh bon canh nam vua chop mat
Sao vang nam canh mong hon bay
'''
