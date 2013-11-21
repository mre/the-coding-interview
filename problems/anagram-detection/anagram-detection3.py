def is_anagram(token, child):
  hits = 0
  for t in token:
    for i, c in enumerate(child):
      if c == t:
        child = child[:i] + child[i+1:]
        hits += 1
        break
  return hits == len(token)

def anagram(parent, child):
  count = 0
  for start in range(len(parent)-len(child)):
      end = start + len(child)
      token = parent[start:end]
      if is_anagram(token, child):
          count += 1
  return count

print anagram('AdnBndAndBdaBn', 'dAn') # 4 ("Adn", "ndA", "dAn", "And")
print anagram('AbrAcadAbRa', 'cAda') # 2
