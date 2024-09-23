from math import gcd

class PhanSo:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def rut_gon(self):
        ucln = gcd(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln

    def __add__(self, other):
        tu_so = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        mau_so = self.mau_so * other.mau_so
        return PhanSo(tu_so, mau_so)

# Nhập vào hai phân số p và q
a, b, c, d = map(int, input().split())
p = PhanSo(a, b)
q = PhanSo(c, d)

# Tính tổng p + q
tong = p + q

# Rút gọn phân số tổng
tong.rut_gon()

# In ra kết quả
print(f"{tong.tu_so}/{tong.mau_so}")
