class Khachhang:
    def __init__(self,id, name, old_idx, new_idx):
        self.id = id
        self.name = name
        self.old_idx = old_idx
        self.new_idx = new_idx
        self.cost = self.calc_money()

    def __lt__(self, other):
        return self.cost > other.cost

    def calc_money(self):
        cost = 0
        num = self.new_idx - self.old_idx
        if 0 <= num <= 50:
            cost = int(num * 100 * 1.02)
        elif num <= 100:
            cost = int(50 * 100 * 1.03 + (num - 50) * 150 * 1.03)
        else:
            cost = int((50 * 100 + 50 * 150 + (num - 100) * 200) * 1.05)
        return cost

n = int(input())
khachhang = []
for i in range(n):
    id = f'KH{i + 1:02d}'
    name = input()
    old_idx = int(input())
    new_idx = int(input())
    khachhang.append(Khachhang(id, name, old_idx, new_idx))
khachhang.sort()
for i in range(n):
    print(f'{khachhang[i].id} {khachhang[i].name} {khachhang[i].cost}')

'''
3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612
'''