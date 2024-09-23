def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def solve(n):
    if is_prime(int(n[len(n) - 4:])):
        return 'YES'
    return 'NO'

for i in range(int(input())):
    print(solve(input()))