'''
Find the minimum path sum from the root to a leaf node
aka the sum of the node values along a path
to a leaf node
      1
    /   \
   2     3
  / \   / \
 4   5  6  7

 min_path(1) = 7
 min_path(2) = 6
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def min_path(node):
    if node == None:
        return 0
    return node.value + min(min_path(node.left), min_path(node.right))




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

print(min_path(a))
print(min_path(b))
