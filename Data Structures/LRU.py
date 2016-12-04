class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class LruCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.right = self.tail
        self.tail.left = self.head

    def get(self, value):
        temp = self.head.right
        while temp is not self.tail:
            if temp.value == value:
                temp_right = temp.right
                temp_left = temp.left
                temp_right.left = temp_left
                temp_left.right = temp.right
                self.count -= 1
            temp = temp.right
        self.add(value)


        # head->5->4->3->2->1->0->tail

    def add(self, value):
        new_node = Node(value)
        new_node.right = self.head.right
        new_node.left = self.head
        self.head.right = new_node
        new_node.right.left = new_node
        if self.count < self.capacity:
            self.count += 1
        else:
            second_to_last_node = self.tail.left.left
            second_to_last_node.right = self.tail
            self.tail.left = second_to_last_node

    def print_list(self):
        if self.count == 0:
            print("Empty")
            return
        temp_node = self.head.right
        while temp_node is not self.tail:
            print (temp_node.value)
            temp_node = temp_node.right



#[head<->1<->2<->3<->4<->5<->tail]
#add(0)
#[head<->0<->1<->2<->3<->4<->5<->tail]

a = LruCache(5)
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.add(0)
a.get(3)
a.get(5)
a.print_list()
