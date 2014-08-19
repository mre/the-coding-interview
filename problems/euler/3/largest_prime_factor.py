def sieve_upto(n):
    multiples = set()
    for i in range(2, n+1):
        if not i in multiples:
            yield i
            multiples.update(range(i*i,n+1,i))

import numpy
def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = numpy.ones(n/2, dtype=numpy.bool)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1

def prime_factors(n):
    factors = [] 
    d = 2
    while n > 1:
        while n%d==0:
            factors.append(d)
            n /= d
        d = d + 1
    return factors

n = 600851475143
print prime_factors(n)
