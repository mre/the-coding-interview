def permutations(n):
  if not n:
    yield ""
  for i, x in enumerate(n):
    for p in permutations(n[:i] + n[i+1:]):
      yield x + p


print list(permutations(""))
print list(permutations("1"))
print list(permutations("1234"))
