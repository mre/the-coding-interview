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


def longest_compound(words):
    for word in words:



longest_compound(['cat', 'cats', 'catsdogcats', 'catxdogcatsrat', 'dog',
                  'dogcatsdog', 'hippopotamuses', 'rat', 'ratcat', 'ratcatdog',
                  'ratcatdogcat'])
