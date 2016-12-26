'''
Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes
and return its head.
For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space.
You may not modify the values in the list,
only nodes itself can be changed.

swap(a) >> b->a
>> swap(a.right.right) >> swap(c) >>
temp = None
c.right.right = c >> d.right = c
c.right = None
d->c

>> swap(c.right.right) >> swap(None) >> return
'''

class Node:
    def __init__(self, value):
        self.right = None
        self.value = value

def swap(node, prev):
    if node == None:
        return
    temp = node.right.right
    node.right.right = node
    prev.right = node.right
    node.right = temp
    swap(node.right, node)

def print_list(head):
    while head is not None:
        print(head.value)
        head = head.right


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.right = b
b.right = c
c.right = d

swap(a,a)
print_list(b)
