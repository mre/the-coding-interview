"""
Find the product of the coefficients, a and b,
for the quadratic expression that produces the maximum number
of primes for consecutive values of n, starting with n = 0.
"""

from euler_math import primes_upto

sieve = list(primes_upto(20000))

def is_prime(x):
    return x in sieve

def consecutive_primes(a,b):
    n = 0
    while True:
        x = n**2 + a*n + b
        if is_prime(x):
            yield x
            n += 1
        else:
            break

# Tests
# print len(list(consecutive_primes(1, 41))) # 40
# print len(list(consecutive_primes(-79, 1601))) # 80

max = 0
for a in range(-1000, 1000):
    for b in primes_upto(1000):
        length = len(list(consecutive_primes(a,b)))
        if length > max:
            print a, b, max
            max = length

print max
