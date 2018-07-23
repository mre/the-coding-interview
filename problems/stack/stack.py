class Stack():
    """
    Simple LIFO stack
    """
    def __init__(self):
        self.stack = []

    def isEmpty(self):
		    return True if len(self.stack) == 0 else False

    def push(self, i):
        self.stack.append(i)

    def pop(self):
        if(self.isEmpty()):
			      return 'Underflow'
        return self.stack.pop()

s = Stack()
print s.pop() #Undeflow condition. No stack elements here. Should print 'Undeflow'
s.push(42)
s.push(23)
s.push(5)
print s.pop() # 5
print s.pop() # 23
print s.pop() # 43
