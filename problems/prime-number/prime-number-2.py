from math import sqrt
from bench import benchmark

def primes_upto(n):
    """
    Use Sieve of Erathostenes
    """
    # In the beginning we set all numbers to prime
    candidates = [x for x in range(2, n+1)]
    i = 0
    while i < len(candidates):
        # Remove numbers which are multiples of prime numbers
        prime = candidates[i]
        candidates = [j for j in candidates if j == prime or j % prime !=0]
        i += 1
    return candidates

#@benchmark
def is_prime(n):
    if n < 2:
        return False
    for prime in primes_upto(int(sqrt(n)+1)):
        if n % prime == 0:
            return False
    return True

def is_prime_brute(n):
    if n < 2:
        return False
    if n < 4:
        return True
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

print is_prime(0)
print is_prime(2)
print is_prime(4)
print is_prime(5)
print is_prime(101)
print is_prime(3461)
print is_prime(3467)
#print is_prime(2**57885161-1) # Heh
for i in range(50):
    print i, is_prime(i)

#primes = primes_upto(500)
