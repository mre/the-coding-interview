import collections
import functools
from prime_sieve import primes_upto

def factorize(n, primes):
    factors = []
    for p in primes:
        if p*p > n:
            break
        i = 0
        while n % p:
            n //= p
            i += 1
        if i > 0:
            factors.append((p,i))
    if n > 1: factors.append((n,1))
    return factors

def divisors(n, primes):
    div = [1]
    for (p,i) in factorize(n):
        div = [d * p**e for d in div for e in range(i+1)]
    return div

def main():
    MAX = 100
    primes = [p for p in primes_upto(MAX)]
    for n in range(1,MAX):
        print n, divisors(n, primes)

if __name__ == "__main__":
    main()
