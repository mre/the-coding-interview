"""
Brute force
I realize this is not ideal but I can't figure out the
pattern behind the lexicographic permutations right now.

Something like shifting the rightmost digit to the left
and then doing switching two digits...

012345
012354
012453
012534
012543
"""

def get_permutations(digits):
    if not digits:
        yield ""
    if len(digits) == 1:
        yield digits
    for i, digit in enumerate(digits):
        for p in get_permutations(digits[:i] + digits[i+1:]):
            yield digit + p

permutations = sorted(set(p for p in get_permutations('0123456789')))
print permutations[999999]

#permutations = sorted(set(p for p in get_permutations('012345')))
#print permutations[:100]

