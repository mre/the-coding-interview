from itertools import islice

def sieve(n):
    yield 2
    multiples = set()
    for p in range(3,n, 2):
        if p not in multiples:
            yield p
            multiples.update(range(2*p, n, p))

print sum(sieve(2000000))
