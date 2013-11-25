from string import lower

def longest_word(words):
  """
  Runtime: O(n)
  """
  longest = [""]
  for w in words.split(" "):
    w = lower(w)
    if len(w) == len(longest[0]):
      if w not in longest:
        longest.append(w)
    if len(lower(w)) > len(longest[0]):
      longest = [w]
  return longest

print longest_word("You are just an old antidisestablishmentarian") # ["antidisestablishmentarian"]
print longest_word("I gave a present to my parents") # ["present", "parents"]
print longest_word("Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo") #["buffalo"] or ["Buffalo"]

