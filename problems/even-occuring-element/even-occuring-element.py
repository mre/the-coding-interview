def increment(occurences, i):
  if i in occurences.keys():
    occurences[i] += 1
  else:
    occurences[i] = 1

def even_element(l):
  """
  Runtime: O(n)
  """
  occurences = {}
  [increment(occurences, i) for i in l]
  for k in occurences:
    if occurences[k] % 2 == 0:
      return k

print even_element([1,2,32,634,664,32])
