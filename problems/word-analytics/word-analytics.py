from string import upper
import sys

letters = "abcdefghijklmnopqrstuvwxyz"
digits  = "0123456789"

text = sys.stdin.read()
words = text.split()

num_letters = num_symbols = 0
letter_count = [0]*len(letters)

for word in words:
  word = upper(word)
  for letter in word:
    if letter in letters + digits:
      num_letters += 1
      try:
        # Find most common letters
        letter_count[letters.index(letter)] += 1
      except:
        pass
    else:
      if letter != " ":
        num_symbols += 1
top_three_letters = sorted(letter_count)[-3:]

print len(words), "words"
print num_letters, "letters"
print num_symbols, "symbols"
print "Top three most common letters:", ", ".join([letters[letter_count.index(top)] for top in top_three_letters])
