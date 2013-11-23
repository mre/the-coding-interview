def non_repeating(chars):
    """
    Runtime: O(n), Space: O(1)
    """
    r = 0
    it = 0
    for i, c in enumerate(chars):
        r ^= (ord(c) + ord("a"))
        it = (it + 1) % 2
        if it == 0 and r != 0:
            return chars[i-1]

print non_repeating("Daabbccdeffg")
