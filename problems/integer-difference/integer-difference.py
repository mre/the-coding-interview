def diff_brute(n, l):
  count = 0
  for c1, i in enumerate(l):
    for c2, j in enumerate(l):
      if abs(i-j) == n and c1 != c2:
        count += 1
  return count/2

def diff(n, l):
  """
  Runtime: O(n)
  """
  occurences = {}
  count = 0
  for i in l:
    if i in occurences.keys():
      occurences[i] += 1
    else:
      occurences[i] = 1
  for i in occurences.keys():
    if i + n in occurences.keys():
      c1 = occurences[i]
      c2 = occurences[i+n]
      count += c1 * c2
  return count



print diff(4, [1, 1, 5, 6, 9, 16, 27]) # 3 (Due to 2x [1, 5], and [5, 9])
print diff(2, [1, 1, 3, 3]) # 4 (Due to 4x [1, 3])
