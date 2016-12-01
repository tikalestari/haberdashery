class Node:
    def __init__(self, value):
        self.value = value
        self.right = None

def merge(head_1, head_2):
    current_1 = head_1
    current_2 = head_2
    # 1->2->3->4->5->6->7->None
    # 8->None
    while head_1.right is not None and head_2.right is not None:
        if head_1.value <= head_2.value:
            temp = head_1.right
            head_1.right = head_2
            head_1 = temp
        else:
            temp = head_2.right
            head_2.right = head_1
            head_2 = temp
    if head_1.right is None:
        if head_1.value <= head_2.value:
            temp = head_1.right
            head_1.right = head_2
            head_2.right = temp
        else:
            temp = head_2.right
            head_2.right = head_1
            head_1.right = temp

    if head_2.right is None:
        if head_1.value <= head_2.value:
            temp = head_1.right
            head_1.right = head_2
            head_2.right = temp
        else:
            temp = head_2.right
            head_2.right = head_1
            head_1.right = temp

    if current_1.value < current_2.value:
        return current_1
    else:
        return current_2

    '''current_1 = head_1
    current_2 = head_2
    new_head = Node(None)
    current = new_head

    while current_1 is not None and current_2 is not None:
        if current_1.value <= current_2.value:
            current.right = Node(current_1.value)
            current = current.right
            current_1 = current_1.right

        elif current_1.value > current_2.value:
            current.right = Node(current_2.value)
            current = current.right
            current_2 = current_2.right

    while current_1 is not None:
        current.right = Node(current_1.value)
        current_1 = current_1.right
        current = current.right

    while current_2 is not None:
        current.right = Node(current_2.value)
        current_2 = current_2.right
        current = current.right

    return new_head'''

a = Node(1)
b = Node(3)
c = Node(5)
d = Node(7)
a.right = b
b.right = c
c.right = d

e = Node(2)
f = Node(4)
g = Node(6)
h = Node(8)
e.right = f
f.right = g
g.right = h

new_head = merge(a,e)
while new_head is not None:
    print(new_head.value)
    new_head = new_head.right
#print(merge(a,e).value)
