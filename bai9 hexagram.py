def count_ways(numbers):
    # Tính tổng của tất cả các số
    total = sum(numbers)

    # Nếu tổng không chia hết cho 6 thì không có cách nào để xếp các số thành Hexagram
    if total % 6 != 0:
        return 0

    # Tính tổng mỗi cạnh của Hexagram
    side_sum = total // 6

    # Khởi tạo ma trận quy hoạch động
    dp = [[0] * (side_sum + 1) for _ in range(len(numbers) + 1)]

    # Khởi tạo giá trị ban đầu của ma trận
    for i in range(len(numbers) + 1):
        dp[i][0] = 1

    # Điền vào ma trận quy hoạch động
    for i in range(1, len(numbers) + 1):
        for j in range(1, side_sum + 1):
            if numbers[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - numbers[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    # Trả về kết quả cuối cùng
    return dp[-1][-1]

for _ in range(int(input())):
    numbers = list(map(int, input().split()))
    print(count_ways(numbers))
'''
2
3 17 15 18 11 22 12 23 21 7 9 13
1 2 3 4 5 6 7 8 9 10 11 13
'''