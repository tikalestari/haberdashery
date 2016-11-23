#implement a queue using 2 stack (list with pop and append)
class Queue:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        self.size = 0

    def add(self, value):
        self.stack_1.append(value)
        self.size += 1

    def poll(self):
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        if self.stack_2:
            return self.stack_2.pop()
        return None

    def size(self):
        return self.size
