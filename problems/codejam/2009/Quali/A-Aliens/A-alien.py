def combinations(pattern, words, prefix=''):
    """ Enumerate all valid words from a pattern """
    if not any(w.startswith(prefix) for w in words):
        return
    if not pattern:
        if len(prefix) == len(words[0]):
            yield prefix
        return
    GROUP_START = '('
    GROUP_END   = ')'
    c = pattern[0]
    if c == GROUP_START:
        # Remove the group start symbol
        pattern = pattern[1:]
        group, rest = pattern.split(GROUP_END, 1)
        for choice in group:
            # No yield from in PyPy...
            for c in combinations(rest, words, prefix+choice):
                yield c
    else:
        # No yield from in PyPy...
        for c in combinations(pattern[1:], words, prefix+c):
            yield c


def main():
    with open("A-large-practice.in") as f:
        lines = [line.rstrip() for line in f.readlines()]
        L, D, N = map(int, lines[0].split(" "))
        # Read valid alien words
        words = lines[1:D+1]
        patterns = lines[D+1:]
        for i, pattern in enumerate(patterns):
            #print(pattern)
            valid = set(c for c in combinations(pattern, words))
            print("Case #{nr}: {count}".format(nr=i+1, count=len(valid)))

if __name__ == "__main__":
    main()
