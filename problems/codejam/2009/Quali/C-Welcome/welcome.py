from collections import defaultdict

"""
welcome
[0 1 2 3 4 5 6 7 8 9]
[w e l c o m e w e w]
[0 1 2 3 4 5 1 0 1 0]

[0 1 2 3 4 5 6 7 8 9]
[0 1 2 3 4 5 1 0 1 0]

w = 0, 7, 9
e = 1, 6, 8
l = 2
c = 3
o = 4
m = 5
"""

def positions(letters, haystack):
    positions = defaultdict(list)
    for i, h in enumerate(haystack):
        if h in letters:
            positions[h].append(i)
    return positions

def count_matches(needle, haystack, positions, i=0, sum=0):
    needle_rest = needle[i:]
    haystack_rest = haystack[i:]
    if len(needle_rest) > len(haystack_rest):
        # No matches, haystack too short 
        return 0

    if len(needle_rest) == len(haystack_rest):
        # Exactly one match
        return 1

    current_char = needle[i]
    for p in positions[current_char]:
        if p < i:
            # Char is before our current position
            return 0
        count = count_matches(needle, haystack, positions, p+1, sum)
        sum += count
    return sum

def matches(needle, haystack):
    letters = set(needle)
    # positions: {"a": [0, 1, 2], "b": [3, 4], ...}
    pos = positions(letters, haystack)
    return count_matches(needle, haystack, pos)

def main():
    needle = "welcome to codejam"
    haystack = "wwelcome to codejam"
    print matches(needle, haystack)

if __name__ == "__main__":
    main()
