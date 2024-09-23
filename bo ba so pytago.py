def count_pythagorean_triples(N):
    count = 0
    for a in range(1, N):
        for b in range(a, N):
            c = (a*a + b*b) % N
            if c < N and a*a + b*b == c*c:
                count += 1
    return count

N = int(input())
print(count_pythagorean_triples(N))
