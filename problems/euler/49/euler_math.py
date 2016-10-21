import itertools

class Primes(object):
  """
  A dynamic (growing) Sieve of Erathostenes
  """

  def __init__(self, sieve_size = 2**22):
    self.primes = set()
    self.multiples = set()
    self.sieve_size = sieve_size # Initial sieve size
    self.curr = 2 # Start number to search for primes

  def all(self):
    return self.primes

  def __iter__(self):
    return self

  def upto(self, n):
    """
    Returns all primes up to the number n
    """
    for p in sorted(self.primes):
      if p > n:
        return
      yield p
    p = self.next()
    while p <= n:
      yield p
      p = self.next()

  def next(self):
    # Remove all even numbers first
    if self.curr == 2:
      self.primes.add(2)
      self.update_multiples(2)
      self.curr = 3
      return 2
    if self.curr >= self.sieve_size - 1:
      # Finished old sieve. Grow sieve.
      self.grow_sieve()
    # Skip to next prime
    while self.curr in self.multiples:
      self.curr += 2
    # Found a prime!
    prime = self.curr
    self.primes.add(prime)
    self.update_multiples(prime)
    self.curr = prime + 2
    return prime

  def grow_sieve(self):
    self.sieve_size *= 2
    for p in self.primes:
      self.update_multiples(p)

  def update_multiples(self, p):
    self.multiples.update(range(p*2, self.sieve_size, p))


def primes_upto(n):
    """
    Simple Sieve of Erathostenes
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

def primes_range(start, end):
  """ Generate all primes within the specified range """
  for p in primes_upto(end):
    if p < start:
      continue
    yield p

def is_prime(n):
    """ Returns True if n is prime. """
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def permutations(n):
  """ Genenerate all permutations of a number """
  s = str(n)
  for p in itertools.permutations(s):
    yield int("".join(p))

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

def is_pandigital(n):
  digits = str(n)
  unique_digits = set(digits)
  length = len(digits)
  return length == len(unique_digits) and str(length) in unique_digits and str(0) not in unique_digits

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite

def is_probably_prime(n):
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    else:
        # More sophisticated check would be required
        return False
