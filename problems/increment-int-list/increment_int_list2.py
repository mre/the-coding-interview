def increment(l):
  i = int("".join([str(n) for n in l]))
  return [int(n) for n in str(i+1)]

def increment2(digits):
  i = len(digits)-1
  carry = 1
  while i >= 0:
    new_value = digits[i] + carry
    if new_value == 10:
      digits[i] = 0
      carry = 1
    else:
      digits[i] = new_value
      carry = 0
    i -= 1
    if not carry:
      break
  if carry:
    digits.insert(0, carry)
  return digits

print increment([8,7,9,9])
print increment2([8,7,9,9])
