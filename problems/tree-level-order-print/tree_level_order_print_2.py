class Tree():
  def __init__(self, val, left = None, right = None):
    self.val, self.left, self.right = val, left, right

def level_order_print(node_list):
  level_values = []
  child_list = []
  for node in node_list:
    level_values.append(str(node.val))
    if node.left:
      child_list.append(node.left)
    if node.right:
      child_list.append(node.right)
  print " ".join(level_values)
  if child_list:
    level_order_print(child_list)

#                      50
#                  20      70
#               10    30  60  90
#
#          level_order_print:
#          50, 20, 70, 10, 30, 60, 90

t = Tree(50, Tree(20, Tree(10), Tree(30)), Tree(70, Tree(60), Tree(90)))
level_order_print([t])
