from itertools import islice

def sieve(n):
    yield 1
    yield 2
    multiples = set()
    for p in range(3,n, 2):
        if p not in multiples:
            yield p
            multiples.update(range(2*p, n, p))

def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)

print nth(sieve(100000000), 10001)
