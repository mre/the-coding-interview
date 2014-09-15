def primes_upto(n):
    # Our well known sieve...
    multiples = set()
    yield 2
    # Optimization: Add the even numbers
    multiples.update(range(4, n, 2))

    for p in range(3,n,2):
        if p not in multiples:
            # Found a prime!
            yield p
            multiples.update(range(p*2, n, p))
