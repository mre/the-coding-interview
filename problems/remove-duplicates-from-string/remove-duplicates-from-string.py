from string import lower

def remove_duplicates(string):
  seen = []
  for ch in lower(string):
    if not ch in seen:
        seen.append(ch)
  return "".join(seen)

print remove_duplicates("tree traversal")
