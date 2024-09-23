MOD = 10**9 + 7

def power(x, y):
    res = 1
    while y > 0:
        if y & 1:
            res = res * x % MOD
        y >>= 1
        x = x * x % MOD
    return res

def solve(N, K, A):
    A.sort()
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % MOD
    invfact = [0] * (N + 1)
    invfact[N] = power(fact[N], MOD - 2)
    for i in range(N - 1, -1, -1):
        invfact[i] = invfact[i + 1] * (i + 1) % MOD
    def C(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * invfact[k] * invfact[n - k] % MOD
    ans = 0
    for i in range(N):
        ans = (ans + A[i] * (C(i, K - 1) - C(N - i - 1, K - 1))) % MOD
    return ans

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))
