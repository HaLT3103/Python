class Matrix:
    def __init__(self, n, m, elements):
        self.n = n
        self.m = m
        self.elements = elements

def multiply_matrix_and_its_transpose(matrix):
    # Khởi tạo ma trận kết quả
    result = [[0 for _ in range(matrix.n)] for _ in range(matrix.n)]
    # Tính tích của ma trận và ma trận chuyển vị
    for i in range(matrix.n):
        for j in range(matrix.n):
            for k in range(matrix.m):
                result[i][j] += matrix.elements[i][k] * matrix.elements[j][k]
    return result

# Số bộ test
t = int(input())
for _ in range(t):
    # Kích thước ma trận
    n, m = map(int, input().split())
    # Phần tử của ma trận
    elements = []
    for _ in range(n):
        row = list(map(int, input().split()))
        elements.append(row)
    # Tạo ma trận
    matrix = Matrix(n, m, elements)
    # Tính tích của ma trận và ma trận chuyển vị
    result = multiply_matrix_and_its_transpose(matrix)
    # In kết quả
    for row in result:
        print(' '.join(map(str, row)))
