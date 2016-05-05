def is_pandigital(n):
  numbers = str(n)
  unique_numbers = set(numbers)
  for i in range(1, len(numbers) + 1):
    if str(i) not in unique_numbers:
      return False
  return True

assert(is_pandigital(123456789))
assert(is_pandigital(1))
assert(is_pandigital(12))
assert(is_pandigital(13) == False)
assert(is_pandigital(12345679) == False)

pandigital_numbers = []

for i in range(2,9999):
  p = "".join([str(i * mult) for mult in range(1, 7 - len(str(i)))])
  if is_pandigital(p):
    pandigital_numbers.append(p)

print max(p for p in pandigital_numbers if len(str(p)) == 9)

