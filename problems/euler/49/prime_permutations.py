from euler_math import permutations, primes_range
from collections import defaultdict
from itertools import combinations

all_primes = set(primes_range(1000, 10000))
prime_sequences = []

for p in all_primes:
  prime_permutations = set([p for p in permutations(p) if p in all_primes])
  if len(prime_permutations) < 3:
    continue
  differences = defaultdict(set)
  for p1, p2 in combinations(prime_permutations, 2):
    differences[abs(p2 - p1)].update(set([p1, p2]))
  for primes in differences.itervalues():
    if len(primes) == 3:
      if primes not in prime_sequences:
          print primes
          prime_sequences.append(primes)
