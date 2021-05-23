def anagram(words):
    anagrams = {}
    for word in words:
        sortedword = "".join(sorted(word))
        if sortedword in anagrams:
            anagrams[sortedword].append(word)
        else:
            anagrams[sortedword] = [word]
    return list(anagrams.values())
 
words = ["cinema","iceman","foo","oof"]
print(anagram(words))

#output
#[['cinema', 'iceman'], ['foo', 'oof']]

