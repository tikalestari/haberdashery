class Node:
    def __init__(self, container_size):
        self.array = [-1 for i in range(container_size)]
        self.right = None
        self.left = None
        self.count = 0

    def is_full(self):
        return self.count == len(self.array)

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
        pass

    def pop(self, index):
        pass

    def print_list(self):
        if self.count == 0:
            print("Empty")
            return
        temp_node = self.head.right
        while temp_node is not self.tail:
            print (temp_node.array)
            temp_node = temp_node.right

'''[1,2,3]->[1,2,3]->[1,2,3]

index = count - (size * (num_nodes - 1)) - 1
  1          5   -   (3   *    1)  - 1


head<->[-1,-1,-1]<->tail
add(1)
count = 1
index = 0 = count % size - 1
add(2)
count = 2
index = 1 = count % size - 1
add(3)
count = 3
index = 2 = count % size - 1
add(4)
index = 0

head<->[1,2,3]<->[4,5,-1]<->tail
5 = last_node[index]
add(1)
add(2)
add(3)
add(4)
add(5)
pop()
'''
a = LinkedArray(3)
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.print_list()
