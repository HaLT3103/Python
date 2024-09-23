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
def dao(n):
    s = str(n)
    s1 = s[::-1]
    return int(s1)
def solve():
    n = int(input())
    a = SieveOfEratosthenes(n)
    for i in a:
        if a.count(dao(i)) != 0 and i != dao(i):
            print(i, end=' ')
            print(dao(i), end=' ')
            #a.remove(i)
            a.remove(dao(i))
    return ''
for i in range(int(input())):
    print(solve())