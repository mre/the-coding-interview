def non_repeating(chars):
    """
    Runtime: O(n), Space: O(1)
    """
    r = 0
    it = 0
    for i, c in enumerate(chars):
        r ^= (ord(c))
        it = (it + 1) % 2
        if it == 0 and r != 0:
            return chars[i-1]
    if len(chars) % 2 == 0:
        return False
    else:
        return chars[-1]
          

def non_repeating2(string):
  """
  Runtime: O(n), Space: O(1)
  """
  i = 0
  while i < len(string):
    try:
      if string[i] == string[i+1]:
        i += 2
      else:
        return string[i]
    except Exception:
      return string[i]
  return True



print non_repeating("Daabbccdeffg")
print(non_repeating("AABBC"))
print(non_repeating("AABBCCDEEFF"))

print(non_repeating2("AABBC"))
print(non_repeating2("AABBCCDEEFF"))
print(non_repeating2("Daabbccdeffg"))
