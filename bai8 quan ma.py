def count_ways(n, m):
    MOD = 10 ** 9 + 7
    dp = [[0] * m for _ in range(n)]
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    # Khởi tạo ma trận dp với giá trị ban đầu là 1
    for i in range(n):
        for j in range(m):
            dp[i][j] = 1

    # Tính toán số cách đặt con mã cho mỗi ô trên bàn cờ
    for _ in range(3):
        dp_new = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                for dx, dy in moves:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m:
                        dp_new[x][y] += dp[i][j]
                        dp_new[x][y] %= MOD
        dp = dp_new

    # Tính tổng số cách đặt con mã
    total_ways = sum(sum(row) for row in dp) % MOD

    return total_ways


# Test với bộ test từ ví dụ của bạn
print(count_ways(1, 2))
