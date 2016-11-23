class Stack:
    def __init__(self, container_size = 10, load_factor = 0.75):
        self.container_size = container_size
        self.load_factor = load_factor
        self.container = [0 for i in range(container_size)]
        self.count = 0

    def pop(self):
        self.count -= 1
        return self.container[self.count+1]

    def push(self, item):
        self.container[self.count] = item
        self.count += 1
        if self.count / self.container_size > self.load_factor:
            self.redistribute()

    def size(self):
        return self.count + 1

    def redistribute(self):
        new_container = [0 for i in range(2 * len(self.container))]
        for index in range(len(self.container)):
            new_container[index] = self.container[index]
        self.container = new_container
        self.container_size *= 2




s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s.container)
