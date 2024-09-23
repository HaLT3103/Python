# Hàm kiểm tra một số có phải là số nguyên tố hay không
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Hàm đếm các số nguyên dương không lớn hơn N và có đúng 9 ước số
def countNumbers(N):
    count = 0 # Biến đếm kết quả
    primes = [] # Danh sách các số nguyên tố nhỏ hơn hoặc bằng căn bậc hai của N
    for i in range(2, int(N**0.5) + 1):
        if isPrime(i):
            primes.append(i)
    # Duyệt các cặp (x, y) trong danh sách các số nguyên tố
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            x = primes[i]
            y = primes[j]
            # Kiểm tra xem (xy)^2 có nhỏ hơn hoặc bằng N hay không
            if (x * y)**2 <= N:
                count += 1
            else:
                break # Nếu không thì dừng vòng lặp con
    # Duyệt các số x trong danh sách các số nguyên tố
    for x in primes:
        # Kiểm tra xem x^8 có nhỏ hơn hoặc bằng N hay không
        if x**8 <= N:
            count += 1
        else:
            break # Nếu không thì dừng vòng lặp
    return count

# Nhập vào số N từ bàn phím
N = int(input())
# In ra kết quả
print(countNumbers(N))
