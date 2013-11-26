class Trie():
    def __init__(self):
        self.root = {}
        self.endword = ""

    def add(self, word):
        curr = self.root
        for letter in word:
            # Create dict if key does not exist
            curr = curr.setdefault(letter, {})
        # Mark end of current word
        curr.setdefault(self.endword, self.endword)

    def __contains__(self, word):
        curr = self.root
        for letter in word:
            try:
                curr = curr[letter]
            except KeyError:
                return False
        # Make sure it's a complete word
        if self.endword in curr:
            return True
        else: # an incomplete string
            return False

    def __str__(self):
        return str(self.root)

"""
def longest_compound(words):
    index = {}
    min_length = float('inf')
    for word in words:
        length = len(word)
        min_length = min(min_length, length)
        if length in index.keys():
            index[length].append(word)
        else:
            index[length] = [word]
    longest_compound = ""
    for k in index.keys():
        if k > min_length * 2:
            for w in index[k]:
                if is_compound(w, index):
                    longest_compound = w
    return longest_compound
"""

def longest_sub(word, trie):
    longest_subword = None
    for end in range(len(word)):
        if word[:end] in trie:
            longest_subword = word[:end]
    return longest_subword


def subwords(word, trie):
    remaining = word
    subwords = []
    while remaining:
        sub = longest_sub(remaining, trie)
        if not sub:
            # Find last part of the word
            if remaining in trie:
                subwords.append(remaining)
            break
        # Remove longest subword
        subwords.append(sub)
        remaining = remaining[len(sub):]
    return subwords


def longest_compound(words):
    longest = ""
    trie = Trie()
    for word in words:
        trie.add(word)
    for word in words:
        subwords = subwords(word, trie)
        if len(subwords) > 1:
            compound = "".join(subwords)
            longest = max(longest, compound)
    return longest


def longest_compound_brute(words):
    longest = ""
    for word in words:
        remaining = word
        # Look if we can combine other
        # words to create this word
        while True:
            has_changed = False
            for fill in words:
                if fill != word and fill == remaining[:len(fill)]:
                    remaining = remaining[len(fill):]
                    has_changed = True
                if remaining == "":
                    if len(word) > len(longest):
                        longest = word
                    break
            if not has_changed:
                break
    return longest


words = ['cat', 'cats', 'catsdogcats', 'catxdogcatsrat', 'dog',
        'dogcatsdog', 'hippopotamuses', 'rat', 'ratcat', 'ratcatdog',
        'ratcatdogcat']
#print longest_compound_brute(words)
print longest_compound(words)


