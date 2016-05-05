from euler_math import is_prime
from itertools import permutations

def is_divisible(num):
  divisors = [2, 3, 5, 7, 11, 13, 17]
  for i, slice_start in enumerate(range(1, 8)):
    s = int(num[slice_start: slice_start + 3])
    divisor = divisors[i]
    if s % divisor != 0:
      return False
  return True

def prime_pans():
    matches = set()
    pandigital_numbers = ["".join(map(str, p)) for p in permutations(range(0, 10))]
    for num in pandigital_numbers:
      if is_divisible(num):
        matches.add(int(num))
    return matches

matches = prime_pans()
print sum(matches)

