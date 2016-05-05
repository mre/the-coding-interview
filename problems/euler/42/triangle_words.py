import string


class TriangleCheck():

  def __init__(self):
    # Lookup table for the first 1000 triangle numbers
    # That's enough to check all triangle words
    # up to a length of 40 characters
    self.triangle_numbers = self.gen_triangle_numbers(1000)

  def gen_triangle_numbers(self, maximum):
    triangle_numbers = set()
    for n in range(1, maximum+1):
      t = n * (n+1)/2
      triangle_numbers.add(t)
    return triangle_numbers

  def is_triangle_number(self, n):
    return n in self.triangle_numbers

  def is_triangle_word(self, word):
    digits = [string.uppercase.index(c) + 1 for c in word]
    return self.is_triangle_number(sum(digits))


checker = TriangleCheck()
with open("p042_words.txt") as f:
  triangle_words = set()
  words = f.read()
  for word_raw in words.split(","):
    # Remove quotes
    word = word_raw[1:-1]
    if checker.is_triangle_word(word):
      triangle_words.add(word)
print len(triangle_words)
