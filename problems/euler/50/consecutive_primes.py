from euler_math import primes_upto

"""
Note: This is a pretty slow solution.
Here's some profiling output (using https://github.com/rkern/line_profiler)
python -m line_profiler consecutive_primes.py.lprof       ✱ ◼
Timer unit: 1e-06 s

Total time: 30.2917 s
File: consecutive_primes.py
Function: find_prime_sequence at line 12

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    12                                           @profile
    13                                           def find_prime_sequence(biggest_number):
    14         1       600857 600857.0      2.0    primes = set(primes_upto(biggest_number))
    15         1        30150  30150.0      0.1    primes_sorted = sorted(primes)
    16         1            2      2.0      0.0    longest_streak = []
    17     78499        75310      1.0      0.2    for i, p in enumerate(primes_sorted):
    18     78498        62165      0.8      0.2      current_streak = [p]
    19     78498        33635      0.4      0.1      current_sum = p
    20    650999     15283088     23.5     50.5      for next_p in primes_sorted[i + 1:]:
    21    650998       325662      0.5      1.1        if current_sum + next_p > biggest_number:
    22     78497     12757345    162.5     42.1          break
    23    572501       338770      0.6      1.1        current_streak.append(next_p)
    24    572501       246141      0.4      0.8        current_sum = current_sum + next_p
    25    572501       318007      0.6      1.0        if len(current_streak) <= len(longest_streak):
    26    571935       220138      0.4      0.7          continue
    27       566          365      0.6      0.0        if current_sum in primes:
    28        53           83      1.6      0.0          longest_streak = current_streak[:]
    29         1            0      0.0      0.0    return longest_streak



"""


@profile
def find_prime_sequence(biggest_number):
  primes = set(primes_upto(biggest_number))
  primes_sorted = sorted(primes)
  longest_streak = []
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
  return longest_streak


longest_streak = find_prime_sequence(1000000)
print(sum(longest_streak), longest_streak)
