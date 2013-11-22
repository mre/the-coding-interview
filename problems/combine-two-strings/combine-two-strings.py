def is_shuffle(s1, s2, s3):
  """
  Runtime: O(n)
  """
  if len(s3) != len(s1) + len(s2):
    return False
  i1 = i2 = i3 = 0
  while i1 < len(s1) and i2 < len(s2):
    c = s3[i3]
    if s1[i1] == c:
      i1 += 1
    elif s2[i2] == c:
      i2 += 1
    else:
      return False
    i3 += 1
  return True

print is_shuffle("abc", "def", "dabecf")
print is_shuffle("bac", "def", "dabecf")
print is_shuffle("otto", "anna", "")
print is_shuffle("otto", "anna", "ottoanna")
print is_shuffle("otto", "anna", "oatntnoa")
print is_shuffle("aabb", "aabb", "aaaabbbb")
print is_shuffle("aabb", "aabb", "abaaabbb")
