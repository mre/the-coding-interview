from string import lower
import sys

letters = "abcdefghijklmnopqrstuvwxyz"
digits  = "0123456789"

text = sys.stdin.read()
words = text.split()

num_letters = 0
for word in words:
  word = lower(word)
  print ">>" + word + "<<"
  num_letters += 1

print len(words), "words"
print letters, "letters"
