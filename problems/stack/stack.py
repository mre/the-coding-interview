"""
This is a simple implementation of the Stack data structure
Use it as you please ^_^
"""

class Stack():
    """
    Simple LIFO Stack data structure
    """

    def __init__(self):
        """Constructor declaring the private variable"""
        self._items = []
    
    def is_empty(self):
        """Check the emptiness of the stack"""
        return len(self._items) == 0

    def size(self):
        """Get the number of items in the stack"""
        return len(self._items)

    def push(self, item):
        """Push an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Pop an item from the end of the stack"""
        if self.is_empty():
            raise RuntimeError("Attempt to pop an empty Stack!")
        return self._items.pop()

    def show(self):
        """Show the contents of the stack"""
        res = "Stack (["
        if self.is_empty():
            print(res + "])")
            return
        for i in range(len(self._items)-1):
            res += str(self._items[i]) + ', '
        res += str(self._items[len(self._items)-1]) + "])"
        print(res)
        return


def main():
    stack = Stack()

    stack.show()          # Stack ([])
    stack.push(42)        # At this point, the stack looks like this: Stack ([42])
    stack.push(23)        # At this point, the stack looks like this: Stack ([42, 23])
    stack.push(5)         # At this point, the stack looks like this: Stack ([42, 23, 5])
    print(stack.size())   # 3
    stack.show()          # Stack ([42, 23, 5])
    print(stack.pop())    # 5
    stack.show()          # Stack ([42, 23])
    print(stack.pop())    # 23
    print(stack.size())   # 1
    stack.show()          # Stack ([42])
    print(stack.pop())    # 42
    stack.show()          # Stack ([])
    print(stack.pop())    # Underflow condition, should raise the RuntimeError exception and print "Attempt to pop an empty Stack!"


if __name__ == "__main__":
    main()
