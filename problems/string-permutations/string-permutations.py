import itertools

def permutations(word):
  all_perms = []
  for i, start in enumerate(word):
    rest = word[:i] + word[i+1:]
    curr_perms = [start + p for p in permutations(rest)]
    all_perms.extend(curr_perms)
  return all_perms


word = "mummy"

# Lazy itertools version
#for p in itertools.permutations(word):
#  print "".join(p)

# Own version
print permutations(word)
for p in permutations(word):
  print p
