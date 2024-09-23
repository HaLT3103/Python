import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def distance(self, point1, point2):
        return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

    def perimeter(self):
        return self.distance(self.p1, self.p2) + self.distance(self.p2, self.p3) + self.distance(self.p3, self.p1)

s = []
for i in range(int(input())):
    a = list(map(float, input().split()))
    p1 = Point(a[0], a[1])
    p2 = Point(a[2], a[3])
    p3 = Point(a[4], a[5])
    if (a[0] == a[2] and a[2] == a[4]) or (a[1] == a[3] and a[3] == a[5]):
        s.append("INVALID")
    else:
        triangle = Triangle(p1, p2, p3)
        s.append(round(triangle.perimeter(), 3))
for i in s:
    print(i)
