def area_of_triangle(x1, y1, x2, y2, x3, y3):
    return abs(0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))

def total_area_of_triangles(triangles):
    total_area = 0
    for triangle in triangles:
        total_area += area_of_triangle(*triangle)
    return round(total_area, 6)

n = int(input())
triangles = []
for i in range(n):
    triangles.append((map(int, input().split())))
print(total_area_of_triangles(triangles))
