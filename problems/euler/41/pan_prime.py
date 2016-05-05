from euler_math import is_prime
from itertools import permutations

def max_pan_prime(n):
  for num_digits in range(n, 1, -1):
    pandigital_numbers = [int("".join(map(str, p))) for p in permutations(range(1, num_digits+1))]
    for num in sorted(pandigital_numbers, reverse=True):
      if is_prime(num):
        return num

print max_pan_prime(9)
