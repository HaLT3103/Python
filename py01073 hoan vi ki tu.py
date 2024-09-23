from itertools import permutations

def all_permutations(s):
    perms = [''.join(p) for p in permutations(s)]
    perms.sort()

    for perm in perms:
        print(perm)

all_permutations(input())
