from euler_math import primes_upto

# Warning: Ugly, imperative code ahead.
# Don't do this at home kids.
# I just wanted to get the solution quickly.
# This should really be done using at least some functions.

maximum = 10000
primes = primes_upto(maximum)
primes_ordered = list(primes)
primes_set = set(primes_ordered)

for i in range(9, maximum, 2):
  if i in primes_set:
    # Only checking composite numbers
    continue
  #print i
  found = False
  for p in primes_ordered:
    # i = p + 2*x^2 with min(x) = 1
    # Therefore the upper bound
    # for the prime numbers is as follows:
    if p > i - 2:
      break
    for square_num in range(1, (i - p)/2 + 1):
      if i == p + 2*square_num**2:
        #print "{} = {} + 2*{}^2".format(i, p, square_num)
        found = True
        break
    if found:
      break
  if found:
    found = False
    continue
  else:
    print "Not matching:", i
    break
