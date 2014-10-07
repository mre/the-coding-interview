def primes_upto(n):
    """
    Sieve of Drathostenes
    """
    multiples = set()
    yield 2
    # Optimization: Add the even numbers
    multiples.update(range(4, n, 2))
    for p in range(3,n,2):
        if p not in multiples:
            # Found a prime!
            yield p
            multiples.update(range(p*2, n, p))

def factorize(n, primes):
    factors = []
    for p in primes:
        if p > n:
            break
        i = 0
        while n % p == 0:
            n //= p
            i += 1
        if i > 0:
            factors.append((p,i))
    if n > 1: factors.append((n,1))
    return factors

def divisors(z, primes):
    n = z
    div = [1]
    factors = factorize(n, primes)
    for p,i in factors:
        div = [d * p**e for d in div for e in range(i+1) if d* p**e != n]
    return div

if __name__ == "__main__":
    p = list(primes_upto(28124))
    print divisors(5690, p)
    print divisors(5691, p)
