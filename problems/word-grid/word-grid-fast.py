orig_grid = [
  "  oh my god it really  I   ",
  "  time I am soworks this   ",
  "finally made  happy that   ",
  "it. Google is not a friend ",
  "  enim os tahw   mine   fo ",
  "              ma I annog   ",
  "  I evah on ginkcuf do next",
  "     this is just  clue   l ",
  " wikipedia is co sooooo coo",
]

class Finder(object):
  """
  An efficient solution to the word-grid problem
  which uses caching to speed things up.
  Could be more space efficient with a trie for the suffixes
  """
  def __init__(self, grid, words):
    self.detected = set()
    self.grid = grid
    self.words = words
    # Cache some properties for fast lookup
    self.max_len = max(map(len, words))
    self.prefixes = self.get_prefixes()

  def get_prefixes(self):
    prefixes = set()
    for word in self.words:
      for end in range(0, len(word)+1):
        prefixes.update([word[0:end]])
    return prefixes

  def find_words(self):
    for y in range(0, len(self.grid)):
      for x in range(0, len(self.grid[0])):
        self.find_words_from(x, y)
    return self.detected

  def find_words_from(self, x, y, current = ""):
    try:
      char = self.grid[y][x]
    except:
      return
    if not char:
      return
    current += char
    if len(current) > self.max_len:
      return
    if current not in self.prefixes:
      return
    if current in self.words:
      self.detected.update([current])
    self.find_words_from(x, y-1, current) # Up
    self.find_words_from(x, y+1, current) # Down
    self.find_words_from(x-1, y, current) # Left
    self.find_words_from(x+1, y, current) # Right

words = set([word.strip() for word in open("/usr/share/dict/words")])
grid = []
for line in orig_grid:
  grid.append([c for c in line])
finder = Finder(grid, words)
print finder.find_words()
