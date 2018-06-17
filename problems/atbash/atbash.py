import string

def translator():
    d = {}    
    for i in range(len(list(string.ascii_lowercase))):
        d[list(string.ascii_lowercase)[i]] = list(reversed(string.ascii_uppercase))[i]
    return d

def atBash(string):
    """
        Uses dictionary helper function.
    """
    translate_dict = translator()
    res = ""
    for i in list(string):
        res += translate_dict[i]
    return res



def atBash2(string):
    """
        No helper dictionary used.
    """
    start = ord('a')
    final = ord('Z')
    res = ""
    for char in string:
        sub = ord(char) - start
        res += chr(final - sub)
    return res

assert(atBash("old") == "LOW")
assert(atBash2("old") == "LOW")
assert(atBash("irk") == "RIP")
assert(atBash2("irk") == "RIP")