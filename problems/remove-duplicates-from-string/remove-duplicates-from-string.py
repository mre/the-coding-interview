# Python 2
from string import lower

def remove_duplicates(string):
  seen = []
  for ch in lower(string):
    if not ch in seen:
        seen.append(ch)
  return "".join(seen)

print remove_duplicates("tree traversal") # tre avsl

# Python 3
def remove_dupes(string):
    seen = []
    for ch in string.lower():
        if ch not in seen:
            seen.append(ch)
    return "".join(seen)

print(remove_dupes("tree traversal")) # tre avsl

# This is O(n^2) but one-liner
def remove_dupes(string):
    return ''.join(sorted(set(string), key=string.index))

print(remove_dupes("tree traversal")) # tre avsl

# Another approach using OrderedDict
from collections import OrderedDict

def remove_dupes(string):
    return "".join(OrderedDict.fromkeys(string)) 

print(remove_dupes("tree traversal")) # tre avsl
