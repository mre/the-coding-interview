def char_val(c):
    return ord(c) - ord('A') + 1

def score(name):
    return sum(char_val(c) for c in name)

with open("p022_names.txt") as names_file:
    names = sorted([name.replace('"','') for name in names_file.read().split(',')])
    print sum((i+1) * score(name) for i, name in enumerate(names))
