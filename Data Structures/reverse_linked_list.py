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
