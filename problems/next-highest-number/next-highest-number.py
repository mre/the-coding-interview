from itertools import permutations

def next_highest_number_brute(n):
    all_perms = sorted([int("".join(p)) for p in permutations(str(n))])
    for p in all_perms:
        if p > n: return p

def next_highest_number(n):
    next_highest = float("inf")
    for p in permutations(str(n)):
        p = int("".join(p))
        if n < p < next_highest:
            next_highest = p
    return next_highest


print next_highest_number_brute(1234)
print next_highest_number_brute(939184829)

print next_highest_number(1234)
print next_highest_number(939184829)
