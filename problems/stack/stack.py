class Stack():
    """
    Simple LIFO stack
    """
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, i):
        self.stack.append(i)

    def pop(self):
        if(self.is_empty()):
            return None
        return self.stack.pop()

s = Stack()
print s.pop() #Undeflow condition. 
s.push(42)
s.push(23)
s.push(5)
print s.pop() # 5
print s.pop() # 23
print s.pop() # 43
