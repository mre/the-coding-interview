from euler_math import Primes


class PrimeFactors(object):
  def __init__(self):
    self.primes = Primes()

  def count(self, number):
    factors = 0
    remain = number
    for p in self.primes.upto(number):
      if p * p > remain:
        factors += 1
        break
      if remain % p == 0:
        factors += 1
      while remain % p == 0:
        remain = remain / p
      if remain == 1:
        break
    return factors


target_streak = 4  # Minimum sequence of integers in a row
distinct_primes = 4  # Number of distinct primes forming each integer
curr = 2 * 3 * 5 * 7
streak = 0
factors = PrimeFactors()
while streak < target_streak:
  curr += 1
  if factors.count(curr) >= distinct_primes:
    streak += 1
  else:
    streak = 0

# Print the first number in the streak
print curr - target_streak + 1
