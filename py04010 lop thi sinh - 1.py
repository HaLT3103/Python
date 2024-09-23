class Thisinh:
    def __init__(self, ten, ns, d1, d2, d3):
        self.ten = ten
        self.ns = ns
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
    def tong(self):
        return "{:.1f}".format(float(self.d1) + float(self.d2) + float(self.d3))

ten = input()
ns = input()
d1 = input()
d2 = input()
d3 = input()
a = Thisinh(ten, ns, d1, d2, d3)
print(a.ten + " " + a.ns + " " + a.tong())