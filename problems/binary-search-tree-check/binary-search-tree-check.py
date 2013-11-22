def is_search_tree(tree, minval = float('-inf'), maxval = float('inf')):
    if not tree:
        # Empty
        return True
    if tree.left:
        l = tree.left.value
        if l and not (minval < l < tree.value):
            return False
    if tree.right:
        r = tree.right.value
        if r and not (tree.value < r < maxval):
            return False
    return  is_search_tree(tree.left, minval, tree.value) and \
            is_search_tree(tree.right, tree.value, maxval)

class Tree(object):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

t1 =    Tree(15, 
            Tree(12, 
                None, 
                Tree(13)), 
            Tree(22, 
                Tree(18), 
                Tree(100))
        )

t2 =    Tree(15, 
            Tree(18),
            None
        )

print is_search_tree(t1)
print is_search_tree(t2)
