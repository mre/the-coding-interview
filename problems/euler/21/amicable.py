import collections
import functools
from prime_sieve import primes_upto

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
    # Include n itself?
    #if n > 1: factors.append((n,1))
    return factors

def divisors(n, primes):
    div = [1]
    factors = factorize(n, primes)
    for p,i in factors:
        div = [d * p**e for d in div for e in range(i+1) if d* p**e != n]
    return div

def find_amicable(d):
    amicable = set()
    for a,b in d.iteritems():
        try:
            if d[b] == a:
                if a != b:
                    amicable.update([a, b])
        except KeyError:
            pass
    return amicable

def main():
    MAX = 10001
    primes = [p for p in primes_upto(MAX)]
    d = {}
    for n in range(1,MAX):
        d[n] = sum(divisors(n, primes))
    amicable = find_amicable(d)
    print sum(amicable)

if __name__ == "__main__":
    main()
