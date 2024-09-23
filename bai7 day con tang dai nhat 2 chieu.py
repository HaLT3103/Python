from bisect import bisect_left

def longest_increasing_subsequence(pairs):
 #   pairs.sort()  # Sắp xếp các cặp số
    lis = [pairs[0][1]]  # Khởi tạo dãy con tăng dài nhất

    for x, y in pairs[1:]:
        if y > lis[-1]:  # Nếu y lớn hơn phần tử cuối cùng trong dãy con tăng
            lis.append(y)  # Thêm y vào cuối dãy con tăng
        else:
            # Tìm vị trí để chèn y vào dãy con tăng sao cho dãy vẫn duy trì tính chất tăng dần
            lis[bisect_left(lis, y)] = y

    return len(lis)

n = int(input())
pairs = []
for i in range(n):
    x, y = map(int, input().split())
    pairs.append((x, y))
print(longest_increasing_subsequence(pairs))
'''
8
1 3
3 2
1 1
4 5
6 3
9 9
8 7
7 6
'''