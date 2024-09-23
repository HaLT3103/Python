
def solve(n, matrix, k):
    upper_sum = 0
    lower_sum = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                upper_sum += matrix[i][j]
            elif i > j:
                lower_sum += matrix[i][j]
    if abs(upper_sum - lower_sum) <= k:
        print("YES")
    else:
        print("NO")
    print(abs(upper_sum - lower_sum))

n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
k = int(input())
solve(n, matrix, k)