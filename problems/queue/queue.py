class Queue():
    """
    Simple FIFO queue
    """
    def __init__(self):
        self.queue = []

    def add(self, i):
        self.queue.append(i)

    def remove(self):
        if self.queue:
            i, self.queue = self.queue[0], self.queue[1:]
            return i

q = Queue()
q.add(1)
q.add(2)
q.add(3)
print q.remove()
print q.remove()
