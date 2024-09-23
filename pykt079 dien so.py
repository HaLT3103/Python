def solve():
    n = int(input())
    a = list(map(int, input().split()))
    max_value = max(a)
    min_value = min(a)
    return max_value - min_value + 1 - len(a)

for _ in range(int(input())):
    print(solve())