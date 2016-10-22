from euler_math import primes_upto

"""
Note: This is a pretty slow solution.
time python consecutive_primes.py
python consecutive_primes.py  26,19s user 0,16s system 99% cpu 26,370 total

Most time is spent slicing `primes_sorted`, I suppose. Didn't profile the code, though.
"""

biggest_number = 1000000
primes = set(primes_upto(biggest_number))
primes_sorted = sorted(primes)
longest_streak = []

current_sum = 1
for i, p in enumerate(primes_sorted):
  current_streak = [p]
  current_sum = p
  for next_p in primes_sorted[i + 1:]:
    if current_sum + next_p > biggest_number:
      break
    current_streak.append(next_p)
    current_sum = current_sum + next_p
    if len(current_streak) <= len(longest_streak):
      continue
    if current_sum in primes:
      longest_streak = current_streak[:]

print(sum(longest_streak), longest_streak)
