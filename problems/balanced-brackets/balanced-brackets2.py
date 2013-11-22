def bb(s):
    """
    Use a stack to keep track of the brackets, yo!
    Runtime: O(n)
    """
    brackets = []
    matching = {")":"(", "]":"[", "}":"{"}
    for p in s:
        if p in matching.values():
            brackets.append(p)
        else:
            try:
                top = brackets[-1]
                if top == matching[p]:
                    brackets.pop()
            except:
                return False
    return not brackets

print bb('()[]{}(([])){[()][]}') # True
print bb('())[]{}') # False
print bb('[(])') # False
