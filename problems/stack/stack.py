class Stack():
    """
    Simple LIFO stack
    """
    def __init__(self):
        self.stack = []

    def push(self, i):
        self.stack.append(i)

    def pop(self):
        return self.stack.pop()

s = Stack()
s.push(42)
s.push(23)
s.push(5)
print s.pop() # 5
print s.pop() # 23
print s.pop() # 43
