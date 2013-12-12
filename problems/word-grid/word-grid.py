# Toy dictionary
words = ["so", "she", "solo", "he", "hell", "hello"]

# ...use nltk for real tasks
"""
from nltk.corpus import wordnet

def contains_word_nltk(word):
    return wordnet.synsets(word)
"""

def begins_with(prefix):
    for w in words:
        if w.startswith(prefix):
            return True
    return False

def contains_word(word):
    return word in words

def find_words(board, curr_pos, prefix = ""):
    wordlist = []
    x, y = curr_pos
    prefix += board[x][y]

    # Stop if last char is empty -> Word break
    if prefix[-1] == " ":
        return wordlist

    # Stop if no more words beginning with prefix
    if not begins_with(prefix):
        return wordlist

    if contains_word(prefix):
        # Prefix is a valid word
        wordlist.append(prefix)

    # Get words in each possible direction:
    # left, right, up, down
    directions = [(-1,0),(1,0),(0,1),(0,-1)]
    for dx, dy in directions:
        try:
            new_words = find_words(board, (x+dx, y+dy), prefix)
            wordlist.extend(new_words)
        except:
            # Ignore illegal board positions
            pass
    return wordlist

def find_all_words(board):
    # Get start positions
    wordlist = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            found = find_words(board, (x,y))
            wordlist.extend(found)
    return wordlist




board = [[" ", "s", "o"],
         [" ", "h", "l"],
         [" ", "e", "l"]]

print find_all_words(board)
