# Nhập thư viện re để sử dụng biểu thức chính quy
import re

# Cách 1: Sử dụng re.split () và sorted ()
def split_and_sort_1(strings):
    numbers = []
    for s in strings:
        numbers.extend (re.split (r' (\\d+)', s) [1::2]) # chỉ lấy các phần số
    numbers = sorted (map (int, numbers)) # chuyển đổi sang số nguyên và sắp xếp
    return numbers

# Cách 2: Sử dụng re.findall () và sorted ()
def split_and_sort_2(strings):
    numbers = []
    for s in strings:
        numbers.extend (re.findall (r'\\d+', s)) # tìm tất cả các số
    numbers = sorted (map (int, numbers)) # chuyển đổi sang số nguyên và sắp xếp
    return numbers

# Cách 3: Sử dụng isdigit () và sorted ()
def split_and_sort_3(strings):
    numbers = []
    for s in strings:
        num = ""
        for c in s:
            if c.isdigit (): # nếu là số thì nối vào num
                num += c
            elif num: # nếu không phải số và num không rỗng thì thêm vào numbers
                numbers.append (num)
                num = ""
        if num: # nếu num không rỗng sau khi duyệt hết xâu thì thêm vào numbers
            numbers.append (num)
    numbers = sorted (map (int, numbers)) # chuyển đổi sang số nguyên và sắp xếp
    return numbers

# Danh sách các xâu ký tự để kiểm tra
n = int(input())
strings = []
for i in range(n):
    strings.append(input())

# Gọi hàm theo cách bạn muốn và in kết quả ra màn hình
#print (split_and_sort_1(strings))
#print (split_and_sort_2(strings))
res = (split_and_sort_3(strings))
for i in res:
    print(i)
