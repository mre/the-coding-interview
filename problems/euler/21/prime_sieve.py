def primes_upto(n):
    # Our well known sieve...
    multiples = set()
    # Optimization: Add the even numbers
    multiples.update(range(4, n, 2))

    for p in range(3,n,2):
        if i not in multiples:
            # Found a prime!
            yield i
            multiples.update(range(i*2, n, i))
        i = i + 1
