# Khởi tạo danh sách rỗng để lưu trữ thông tin về các môn học
danh_sach_mon_hoc = []

# Nhập số lượng môn học
so_luong_mon_hoc = int(input())

# Nhập thông tin cho từng môn học
for i in range(so_luong_mon_hoc):
    ma_mon = input()
    ten_mon = input()
    hinh_thuc_thi = input()

    # Lưu trữ thông tin về môn học trong danh sách
    danh_sach_mon_hoc.append((ma_mon, ten_mon, hinh_thuc_thi))

# Sắp xếp danh sách theo mã môn
danh_sach_mon_hoc.sort()

# In ra danh sách đã sắp xếp
for mon_hoc in danh_sach_mon_hoc:
    print(f"{mon_hoc[0]} {mon_hoc[1]} {mon_hoc[2]}")
