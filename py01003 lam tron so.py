def round_number(N):
    factor = 10
    while N > factor:
        N = round(N / factor) * factor
        factor *= 10
    return N

test_cases = int(input())
for _ in range(test_cases):
    N = int(input())
    print(round_number(N))
