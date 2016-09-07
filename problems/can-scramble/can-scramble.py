from collections import Counter

def can_scramble(source, dest):
  if len(source) != len(dest):
    return False
  return Counter(source) == Counter(dest)


assert(can_scramble("abc", "cba") == True)
assert(can_scramble("abc", "ccc") == False)
assert(can_scramble("aab", "bbc") == False)
assert(can_scramble("aabaaaa", "bbc") == False)
