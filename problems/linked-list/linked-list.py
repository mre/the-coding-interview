class Node():
    def __init__(self, val, next=None, prev=None):
        self.val, self.next, self.prev = val, next, prev

class List():
    def __init__(self, head=None):
        self.head = None

    def add(self, val):
        node = Node(val)
        if self.head:
            node.next = self.head
            self.head.prev = node
        self.head = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def __str__(self):
        curr = self.head
        vals = []
        while(curr):
            vals.append(curr.val)
            curr = curr.next
        return str(vals)

l = List()
l.add(12)
l.add(13)
l.add(14)
print l
