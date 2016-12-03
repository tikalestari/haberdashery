class Node:
    def __init__(self, value):
        self.value = value
        self.right = None

def reverse(head):
    prev = None
    while head is not None:
        temp = head.right
        head.right = prev
        prev = head
        head = temp
    return prev

def reverse_recursive(current, prev):
    if current is None:
        return prev
    next_right = current.right
    current.right = prev
    return reverse_recursive(next_right, current)

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.right = b
b.right = c
c.right = d
new_head = reverse(a)

while new_head is not None:
    print(new_head.value)
    new_head = new_head.right
