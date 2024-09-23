import math
def phanTichNguyenTo(n):
    primes = [i for i in range(2, int(math.sqrt(n)) + 1) if all(i % j != 0 for j in range(2, int(math.sqrt(i)) + 1))]

    # Tìm các số nguyên x sao cho x^2 - n là một bình phương hoàn hảo
    x_values = []
    for x in range(int(math.sqrt(n)), int(math.sqrt(n)) + len(primes)):
        if x ** 2 >= n and math.sqrt(x ** 2 - n) == int(math.sqrt(x ** 2 - n)):
            x_values.append(x)

    # Tìm các thừa số nguyên tố của n
    factors = []
    for x in x_values:
        y = int(math.sqrt(x ** 2 - n))
        factors.append(math.gcd(x - y, n))
        factors.append(math.gcd(x + y, n))

    # Loại bỏ các thừa số không hợp lệ và trả về kết quả
    factors = [f for f in factors if f != 1 and f != n]

    sum = 0
    for i in factors:
        sum += i
    return sum

n = int(input())
a = []
sum = 0
for i in range(n):
    a.append(int(input()))
for i in a:
    sum += int(phanTichNguyenTo(i))
print(sum)