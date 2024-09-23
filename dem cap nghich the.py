# Hàm trộn hai mảng con và đếm số cặp nghịch thế
def merge_and_count(a, left, mid, right):
    # Khởi tạo biến đếm kết quả
    count = 0
    # Tạo hai mảng tạm để lưu các phần tử của hai mảng con
    left_part = a[left:mid+1]
    right_part = a[mid+1:right+1]
    # Khởi tạo các chỉ số i, j, k cho hai mảng con và mảng gốc
    i = 0 # Chỉ số của mảng con bên trái
    j = 0 # Chỉ số của mảng con bên phải
    k = left # Chỉ số của mảng gốc
    # Lặp qua từng phần tử của hai mảng con
    while i < len(left_part) and j < len(right_part):
        # Nếu phần tử bên trái nhỏ hơn hoặc bằng phần tử bên phải
        if left_part[i] <= right_part[j]:
            # Gán phần tử bên trái vào vị trí k của mảng gốc
            a[k] = left_part[i]
            # Tăng chỉ số i lên 1
            i += 1
        else:
            # Nếu phần tử bên trái lớn hơn phần tử bên phải
            # Gán phần tử bên phải vào vị trí k của mảng gốc
            a[k] = right_part[j]
            # Tăng chỉ số j lên 1
            j += 1
            # Tăng biến đếm lên bằng số phần tử còn lại của mảng con bên trái
            count += len(left_part) - i
        # Tăng chỉ số k lên 1
        k += 1
    # Nếu còn phần tử nào trong mảng con bên trái, chèn vào cuối mảng gốc
    while i < len(left_part):
        a[k] = left_part[i]
        i += 1
        k += 1
    # Nếu còn phần tử nào trong mảng con bên phải, chèn vào cuối mảng gốc
    while j < len(right_part):
        a[k] = right_part[j]
        j += 1
        k += 1
    return count

# Hàm sắp xếp và đếm số cặp nghịch thế bằng Merge Sort
def sort_and_count(a, left, right):
    # Khởi tạo biến đếm kết quả
    count = 0
    # Nếu chỉ có một phần tử hoặc không có phần tử nào, không cần sắp xếp và không có nghịch thế nào
    if left < right:
        # Tìm vị trí chia đôi của mảng hiện tại
        mid = (left + right) // 2
        # Sắp xếp và đếm số cặp nghịch thế trong mảng con bên trái và bên phải
        count += sort_and_count(a, left, mid)
        count += sort_and_count(a, mid + 1, right)
        # Trộn hai mảng con và đếm số cặp nghịch thế trong quá trình trộn
        count += merge_and_count(a, left, mid, right)
    return count

# Nhập vào số nguyên n
n = int(input())
# Nhập vào n số nguyên của mảng a
a = list(map(int, input().split()))
# In ra số cặp nghịch thế tìm được
print(sort_and_count(a, 0, n - 1))
