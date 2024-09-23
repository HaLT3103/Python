def count_divisors(n):
    divisors = 1
    i = 2
    while i * i <= n:
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        divisors *= (count + 1)
        i += 1
    if n > 1:
        divisors *= 2
    return divisors

def next_antiprime(n):
    max_divisors = count_divisors(n)
    while True:
        n += 1
        divisors = count_divisors(n)
        if divisors > max_divisors:
            return n

antiprime_numbers = [1]
for _ in range(40): # replace 100 with the number of antiprimes you want to generate
    antiprime_numbers.append(next_antiprime(antiprime_numbers[-1]))
print(antiprime_numbers)
'''
for i in range(int(input())):
    x = int(input());
    for j in antiprime_numbers:
        if x < j:
            print(j)
            break
'''
