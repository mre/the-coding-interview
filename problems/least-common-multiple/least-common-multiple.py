def least_common_multiple_brute(m, n):
  # Check for zero
  if not m or not n:
    return False
  mult_m = m
  mult_n = n
  fac_m = fac_n = 1
  while mult_m != mult_n:
    if mult_m < mult_n:
      fac_m += 1
      mult_m = m * fac_m
    else:
      # mult_m > mult_n
      fac_n += 1
      mult_n = n * fac_n
  return mult_m

def least_common_multiple_simple(m, n):
  # Check for zero
  if not m or not n:
    return False
  M, N = m, n
  while M != N:
    if M < N:
      M += m
    else:
      N += n
  return M


def gcd_orig(m,n):
  while m != n:
    if m > n:
      m = m - n
    else:
      n = n - m
  return m


def gcd(m,n):
  if n == 0:
    return m
  return gcd(n, m % n)

def least_common_multiple(m, n):
  if not m or not n:
    return False
  return abs(m*n)/gcd(m,n)


print least_common_multiple_simple(2, 3)
print least_common_multiple_simple(4, 20)
print least_common_multiple_simple(1, 3)
print least_common_multiple_simple(0, 3)

print least_common_multiple(2, 3)
print least_common_multiple(4, 20)
print least_common_multiple(1, 3)
print least_common_multiple(0, 3)
