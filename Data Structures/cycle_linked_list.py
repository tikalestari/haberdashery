class Node:
    def __init__(self, value):
        self.value = value
        self.right = None

def cycle(a):
    ptr_1 = a
    ptr_2 = a.right.right

    while ptr_1 is not ptr_2:
        ptr_1 = ptr_1.right
        ptr_2 = ptr_2.right.right

    return ptr_1

def print_list(node):
    start_node = node
    while node.right is not start_node:
        print(node.value)
        node = node.right
    print(node.value)
    print(node.right.value)

a = Node(1)
b = Node(2)
c = Node(4)
d = Node(5)
e = Node(6)
f = Node(7)
a.right = b
b.right = c
c.right = d
d.right = e
e.right = f
f.right = b

#1->2->4->5->6->7->2

print_list(cycle(a))
