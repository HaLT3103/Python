def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primes = []
    for p in range(2, n):
        if prime[p]:
            primes.append(p)
    return primes

n , x = map(int, input().split())
a = list(SieveOfEratosthenes(1000000))
b = [x]
for i in range(1, n+1):
    b.append(b[i-1] + a[i-1])
for i in b:
    print(i, end=' ')
