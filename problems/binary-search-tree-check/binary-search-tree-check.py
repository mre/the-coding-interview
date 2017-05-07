class Tree(object):

    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def is_search_tree(tree, minval=float('-inf'), maxval=float('inf')):
    if not tree:
        # Empty
        return True
    if not (minval < tree.val < maxval):
        return False
    return  is_search_tree(tree.left, minval, tree.val) and \
        is_search_tree(tree.right, tree.val, maxval)

t1 = Tree(15,
          Tree(12,
               None,
               Tree(13)),
          Tree(22,
               Tree(18),
               Tree(100))
          )

t2 = Tree(15,
          Tree(18),
          None
          )

assert(is_search_tree(t1) == True)
assert(is_search_tree(t2) == False)
