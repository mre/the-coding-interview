import operator
# A slightly efficient superset of primes.
def PrimesPlus():
  yield 2
  yield 3
  i = 5
  while True:
    yield i
    if i % 6 == 1:
      i += 2
    i += 2
# Returns a dict d with n = product p ^ d[p]
def GetPrimeDecomp(n):
  d = {}
  primes = PrimesPlus()
  for p in primes:
    while n % p == 0:
      n /= p
      d[p] = d.setdefault(p, 0) + 1
    if n == 1:
      return d

def divisors(n):
  d = GetPrimeDecomp(n)
  powers_plus = map(lambda x: x+1, d.values())
  return reduce(operator.mul, powers_plus, 1)

def find_triangle_number(estimate, min_divisors):
    curr_divisors = divisors(estimate)
    while curr_divisors < min_divisors:
        # Estimate the distance to the
        # triangle number with more than
        # min_divisors
        factor = min_divisors / curr_divisors +1 
        print "Estimate", estimate
        print "Divisors", curr_divisors
        print "Factor", factor
        last = estimate
        estimate *= factor
        curr_divisors = divisors(estimate)
    print estimate
    print last
    for n in xrange(last+1, estimate+1):
        print n
        if divisors(n) >= min_divisors:
            break
    print "Estimate", n
    print "Divisors", divisors(n)

find_triangle_number(393600000, 500)
