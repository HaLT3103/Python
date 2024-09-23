import numpy as np

class Matrix:
    def __init__(self, n, m, elements):
        self.n = n
        self.m = m
        self.elements = elements

def multiply_matrix_and_its_transpose(matrix):
    transpose = np.transpose(matrix.elements)
    result = np.dot(matrix.elements, transpose)
    return result

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    elements = []
    for _ in range(n):
        row = list(map(int, input().split()))
        elements.append(row)
    matrix = Matrix(n, m, elements)
    result = multiply_matrix_and_its_transpose(matrix)
    for i in range(n):
        for j in range(m):
            print(result[i][j], end= " ")
        print("")