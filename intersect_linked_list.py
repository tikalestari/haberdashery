class Node:
    def __init__(self, value):
        self.value = value
        self.right = None

def intersect(a, b):
    len_a = 0
    len_b = 0
    a_ptr = a
    b_ptr = b

    while a_ptr is not None:
        len_a += 1
        a_ptr = a_ptr.right
    while b_ptr is not None:
        len_b += 1
        b_ptr = b_ptr.right

    diff = abs(len_a - len_b)

    if len_a < len_b:
        while len_a != len_b:
            len_a += 1
            b = b.right
    elif len_a > len_b:
        while len_b != len_a:
            len_b += 1
            a = a.right

    while a is not None:
        if a is b:
            a.right = b.right
            return a
        a = a.right
        b = b.right

    return Node(None)


def print_list(node):
    while node is not None:
        print (node.value)
        node = node.right

a = Node(1)
b = Node(2)
c = Node(4)
d = Node(4)
e = Node(5)
f = Node(6)
a.right = b
b.right = c
c.right = d
d.right = e
e.right = f
#1->2->4->4->5->6->None a.length = 6


h = Node(5)
h.right = c
#5->4->4->5->6->None b.length = 5


print_list(intersect(a,h))
