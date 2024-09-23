from math import *

class Phanso:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def Rutgon(self):
        t = gcd(self.tu, self.mau)
        self.tu = self.tu / t
        self.mau = self.mau / t
        print(int(self.tu), end="")
        print("/", end="")
        print(int(self.mau))

a, b = map(int, input().split())
p = Phanso(a, b)
p.Rutgon()