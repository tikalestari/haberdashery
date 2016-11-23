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

    def print_list(self):
        if self.count == 0:
            print("Empty Queue")
            return
        temp_node = self.head.right
        while temp_node is not self.tail:
            print(temp_node.value)
            temp_node = temp_node.right
