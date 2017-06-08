class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.isEmpty(): return None
        return self.data.pop(0)

    def peek(self):
        if self.isEmpty(): return None
        return self.data[0]

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack1.push(x)

    # @return nothing
    def pop(self):
        while not self.stack1.isEmpty():
            self.stack2.push(self.stack1.pop())
        self.stack2.pop()

    # @return an integer
    def peek(self):
        while not self.stack1.isEmpty():
            self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    # @return an boolean
    def empty(self):
        return self.stack1.isEmpty() and self.stack2.isEmpty()
