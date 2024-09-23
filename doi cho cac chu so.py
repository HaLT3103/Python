# Hàm sinh ra tất cả các hoán vị của một danh sách
def generate_permutations(a, size, result):
    # Nếu kích thước của danh sách bằng 1, thêm danh sách vào kết quả
    if size == 1:
        result.append(a.copy())
        return
    # Duyệt qua từng phần tử trong danh sách
    for i in range(size):
        # Sinh ra các hoán vị của danh sách con từ phần tử thứ 0 đến phần tử thứ size - 1
        generate_permutations(a, size - 1, result)
        # Nếu kích thước là chẵn, đổi chỗ phần tử cuối cùng với phần tử thứ i
        if size % 2 == 0:
            a[i], a[size - 1] = a[size - 1], a[i]
        else:
            # Nếu kích thước là lẻ, đổi chỗ phần tử cuối cùng với phần tử đầu tiên
            a[0], a[size - 1] = a[size - 1], a[0]

# Hàm so sánh hai danh sách các chữ số
def compare(a, b):
    # Nếu hai danh sách có độ dài khác nhau, trả về kết quả dựa trên độ dài
    if len(a) > len(b):
        return 1 # a lớn hơn b
    elif len(a) < len(b):
        return -1 # a nhỏ hơn b
    else:
        # Nếu hai danh sách có độ dài bằng nhau, so sánh từng chữ số từ trái sang phải
        for i in range(len(a)):
            if a[i] > b[i]:
                return 1 # a lớn hơn b
            elif a[i] < b[i]:
                return -1 # a nhỏ hơn b
        return 0 # a bằng b

# Hàm tìm số lớn nhất nhỏ hơn N bằng cách đổi chỗ các chữ số
def find_max_smaller(N):
    # Chuyển đổi xâu N thành danh sách các chữ số
    digits = [int(c) for c in N]
    # Khởi tạo biến lưu kết quả và danh sách lưu các hoán vị của các chữ số
    result = -1
    permutations = []
    # Sinh ra tất cả các hoán vị của các chữ số trong xâu N
    generate_permutations(digits, len(digits), permutations)
    # Duyệt qua từng hoán vị trong danh sách
    for p in permutations:
        # Chuyển đổi hoán vị thành số nguyên
        num = int("".join([str(d) for d in p]))
        # Kiểm tra xem số này có nhỏ hơn N và lớn hơn kết quả hiện tại hay không
        if num < int(N) and num > result:
            # Cập nhật kết quả
            result = num
    return result

# Nhập vào số lượng test T
T = int(input())
# Lặp qua từng test
for t in range(T):
    # Nhập vào xâu N
    N = input()
    # In ra số lớn nhất nhỏ hơn N tìm được
    print(find_max_smaller(N))
