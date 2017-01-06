'''
Invert a binary tree

      1
    /   \
   2     3
  / \   / \
 4   5  6  7

Invert:

       1
     /   \
    3     2
   / \   / \
  7   6  5  4

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def invert(node):
    if node == None:
        return
    temp = node.right
    node.right = node.left
    node.left = temp
    invert(node.left)
    invert(node.right)

def print_tree(node):
    if node == None:
        return

    print(node.value)
    print_tree(node.left)
    print_tree(node.right)




a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

invert(a)
print_tree(a)
