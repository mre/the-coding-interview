def is_palindrom(n):
  n_word = str(n)
  return n_word == n_word[::-1]

maximum = 0
n1 = 999
n2 = 999
n = n1*n2
for n1 in range(1,999):
  for n2 in range(1,999):
    prod = n1*n2
    if is_palindrom(prod):
      if prod > maximum:
        maximum = prod
print maximum
