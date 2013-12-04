def pairs(string):
    pairs = []
    for i in range(len(string)-1):
        pairs.append("".join(string[i] + string[i+1]))
    return pairs

def string_transformations(string):
    # Transformations:
    substitutions = {"AB": "AA",
                     "BA": "AA",
                     "CB": "CC",
                     "BC": "CC"}
    reductions = {"AA": "A", "CC": "C"}
    for pair in pairs(string):
        if pair in substitutions.keys():
            print pair
        if pair in reductions.keys():
            print pair


print string_transformations("AABBCC")
