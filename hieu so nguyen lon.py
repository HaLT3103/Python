# Nhập vào thư viện gmpy2
import gmpy2
# Nhập vào hai xâu ký tự A và B từ bàn phím
A = input()
B = input()
# Chuyển đổi hai xâu thành hai số nguyên lớn bằng hàm mpz của gmpy2
A = gmpy2.mpz(A)
B = gmpy2.mpz(B)
# Thực hiện phép trừ hai số nguyên lớn bằng toán tử -
result = A - B
# In ra kết quả dưới dạng một xâu ký tự bằng hàm str của gmpy2
result = gmpy2.str(result)
print(result)
