class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.right = self.tail
        self.tail.left = self.head
        self.count = 0

    def add(self, value):
        new_node = Node(value)
        last_node = self.tail.left
        new_node.right = self.tail
        new_node.left = last_node
        last_node.right = new_node
        self.tail.left = new_node
        self.count += 1

    def poll(self):
        if self.count > 0:
            temp_value = self.head.right
            self.head.right = self.head.right.right
            self.head.right.left = self.head
            self.count -= 1
            return temp_value.value
        return None

    def remove(self, index):
        node = self.get_node(index)
        if node is None:
            return None
        node.left.right = node.right
        node.right.left = node.left
        return node.value

    def get_node(self, index):
        if index >= self.count:
            return None
        i = 0
        temp_node = self.head.right
        while i < index:
            temp_node = temp_node.right
            i += 1
        return temp_node

    def get(self, index):
        node = self.get_node(index)
        if node is not None:
            return node.value
        else:
            return None


    def print_list(self):
        if self.count == 0:
            print("Empty Queue")
            return
        temp_node = self.head.right
        while temp_node is not self.tail:
            print(temp_node.value)
            temp_node = temp_node.right

q = Queue()
q.add(3)
q.add(4)
q.add(8)
q.add(9)
print(q.get(0))
print(q.get(1))
q.remove(2)
q.print_list()
