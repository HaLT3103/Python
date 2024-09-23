# Nhập vào số lượng bộ test T
T = int(input())
# Nhập vào thư viện scipy.signal
from scipy.signal import convolve2d
# Lặp qua từng bộ test
for t in range(T):
    # Nhập vào số nguyên N, M và K
    N, M, K = map(int, input().split())
    # Khởi tạo ma trận A
    A = []
    # Nhập vào các hàng của ma trận A
    for i in range(N):
        row = list(map(int, input()))
        A.append(row)
    # Tạo ma trận B có kích thước bằng với kích thước của ma trận con cần tìm
    B = [[1] * M] * N
    # Tính tích chập của A và B
    C = convolve2d(A, B)
    # Khởi tạo biến đếm kết quả
    count = 0
    # Duyệt qua các phần tử của C
    for i in range(N):
        for j in range(M):
            # Nếu phần tử nào bằng K, tăng biến đếm lên 1
            if C[i][j] == K:
                count += 1
    # In ra số lượng ma trận đơn vị con có tổng bằng K
    print(count)
