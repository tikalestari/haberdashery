'''
Return a list of leaf nodes for a binary tree

      1
    /   \
   2     3
  /     /
 4      6

 leaf(1) = [4,6]
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def leaf(node, leaf_list):
    if node == None:
        return
    if node.left == None and node.right == None:
        leaf_list.append(node)
        return
    leaf(node.left, leaf_list)
    leaf(node.right, leaf_list)




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
c.left = f

l = []
leaf(a,l)
for leaf in l:
    print(leaf.value)
