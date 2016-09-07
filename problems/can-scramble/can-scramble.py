from collections import Counter

def can_scramble(source, dest):
  if len(source) != len(dest):
    return False
  counter_source = Counter(source)
  counter_dest = Counter(dest)
  for k, v in counter_dest.items():
    if counter_source[k] != v:
      return False
  return True

assert(can_scramble("abc", "cba") == True)
assert(can_scramble("abc", "ccc") == False)
assert(can_scramble("aab", "bbc") == False)
assert(can_scramble("aabaaaa", "bbc") == False)
