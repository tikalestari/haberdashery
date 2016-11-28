class Node:
    def __init__(self, value):
        self.value = value
        self.right = None

def merge(head_1, head_2):
    final_node = None
    answer = final_node
    if head_1.value < head_2.value:
        final_node = Node(head_1.value)
        head_1 = head_1.right
    else:
        final_node = Node(head_2.value)
        head_2 = head_2.right


    while head_1 is not None or head_2 is not None:
        if head_1 is None:
            while head_2 is not None:
                new_node = Node(head_2.value)
                final_node.right = new_node
                final_node = final_node.right
                head_2 = head_2.right
        elif head_2 is None:
            while head_1 is not None:
                new_node = Node(head_1.value)
                final_node.right = new_node
                final_node = final_node.right
                head_1 = head_1.right
        elif head_1.value < head_2.value:
            #if final_node is None:
            #    final_node = Node(head_1.value)
            new_node = Node(head_2.value)
            final_node.right = new_node
            final_node = final_node.right
            head_1 = head_1.right
            head_2 = head_2.right
        elif head_1.value > head_2.value:
            #if final_node is None:
            #    final_node = Node(head_2.value)
            new_node = Node(head_1.value)
            final_node.right = new_node
            final_node = final_node.right
            head_2 = head_2.right
            head_1 = head_1.right
        else:
            final_node.right = Node(head_1.value)
            head_1 = head_1.right
            head_2 = head_2.right
    return answer


'''
    1->3->5->7->None
    a  b  c  d

    2->4->6->8->None
    e  f  g  h

    1->2

    1->2->3->5->7->None


    1->2->3->4->5->6->7->8->None


    while head_1 is not None or head_2 is not None:
        if head_1.value < head_2.value:
            temp = head_2
            node_1.right =
            head_2 = head_2.right
            head_1 = head_1.right
        elif head_1.value > head_2.value:
            temp = head_1
            node_2.right = temp
            head_1 = head_1.right
            head_2 = head_2.right
        elif head_1.value == head_2.value:

            head_1 = head_1.right
            head_2 = head_2.right

    if node_1.value < node_2.value:
        return node_1
    else:
        return node_2


    pointer_1 = head_1
    pointer_2 = head_2
    node_1 = head_1
    node_2 = head_2
    while pointer_1 is not None and pointer_2 is not None:
        if pointer_1.value < pointer_2.value:
            temp = head_1.right
            head_1.right = head_2
            pointer_2.right = temp
            pointer_2 = pointer_2.right
            head_2 =
        elif pointer_2.value > pointer_1.value:
            temp = head_2.right
            head_2.right = pointer_1
            pointer_1.right = temp
            pointer_1 = pointer_1.right
        elif pointer_1.value == pointer_1.value:
            pointer_1 = pointer_1.right
            pointer_2 = pointer_2.right
    return head_1.value'''






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
