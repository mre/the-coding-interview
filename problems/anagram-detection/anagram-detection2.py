from itertools import permutations

def anagram_brute(parent, child):
    """ 
    Runtime:
    Generate permutations: O(n!)
    Check permutations: O(n)
    => O(n!)
    """
    count = 0
    needles = permutations(child)
    for n in needles:
        n = "".join(n)
        for start in range(len(parent)-len(child)):
            end = start + len(child)
            token = parent[start:end]
            if token == n:
                count += 1
    return count

def anagram_brute2(parent, child):
    """ 
    Runtime:
    Generate permutations: O(n!)
    Check permutations: O(n)
    => O(n!)
    """
    count = 0
    needles = ["".join(perm) for perm in permutations(child)]
    for start in range(len(parent)-len(child)):
        end = start + len(child)
        token = parent[start:end]
        for n in needles:
            if token == n:
                count += 1
    return count

print anagram_brute2('AdnBndAndBdaBn', 'dAn') # 4 ("Adn", "ndA", "dAn", "And")
print anagram_brute2('AbrAcadAbRa', 'cAda') # 2
