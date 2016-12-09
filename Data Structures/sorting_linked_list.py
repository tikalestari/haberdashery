class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def insertion_sort(a):
    current = a.next
    start_node = None
    temp = None
    head = a.prev

    while current is not tail:
        left = current.prev
        temp = current
        while left is not head and temp.value < left.value:
            left = left.prev
        current_right = current.next #connecting current's left and right nodes
        current_left = current.prev
        current_right.left = current_left
        current_left.next = current_right

        right = left.next #placing temp in the correct spot
        left.next = temp
        right.prev = temp
        temp.next = right
        temp.prev = left

        current = current.next

    return head.next

def print_list(node):
    while node is not None:
        print(node.value)
        node = node.next



head = Node(None)
a = Node(6)
b = Node(5)
c = Node(3)
d = Node(1)
e = Node(8)
f = Node(7)
g = Node(2)
h = Node(4)
tail = Node(None)

a.next = b
a.prev = head
b.next = c
b.prev = a
c.next = d
c.prev = b
d.next = e
d.prev = c
e.next = f
e.prev = d
f.next = g
f.prev = e
g.next = h
g.prev = f
h.prev = g
h.next = tail
#6->5->3->1->8->7->2->4->None

print_list(a)
print_list(insertion_sort(a))
