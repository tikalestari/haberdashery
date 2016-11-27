class Node:
    def __init__(self, container_size):
        self.array = [-1 for i in range(container_size)]
        self.container_size = container_size
        self.right = None
        self.left = None
        self.count = 0

    def is_full(self):
        return self.count == len(self.array)

    def is_empty(self):
        return self.count == 0

class LinkedArray:
    def __init__(self, container_size):
        self.count = 0
        self.count_nodes = 1
        self.container_size = container_size
        self.head = Node(0)
        self.tail = Node(0)
        initial_node = Node(container_size)
        self.head.right = initial_node
        self.tail.left = initial_node
        initial_node.right = self.tail
        initial_node.left = self.head

    def add(self, value):
        last_node = self.tail.left
        if last_node.is_full():
            new_last = Node(self.container_size)
            last_node.right = new_last
            self.tail.left = new_last
            new_last.left = last_node
            new_last.right = self.tail
            last_node = new_last
        self.count += 1
        index = self.count % self.container_size - 1
        last_node.array[index] = value
        last_node.count += 1

    def get(self, index):
        if index >= self.count:
            return None
        temp_node = self.head.right
        i = 1
        while i * self.container_size <= index:
            temp_node = temp_node.right
            i += 1
        return temp_node.array[index % self.container_size]

    def pop(self):
        index = (self.count - 1) % self.container_size
        last_node = self.tail.left
        value = last_node.array[index]
        last_node.array[index] = -1
        self.count -= 1
        if index == 0:
            new_last = last_node.left
            self.tail.left = new_last
            new_last.right = self.tail
        return value

    def print_list(self):
        if self.count == 0:
            print("Empty")
            return
        temp_node = self.head.right
        while temp_node is not self.tail:
            print (temp_node.array)
            temp_node = temp_node.right

a = LinkedArray(3)
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.print_list()
