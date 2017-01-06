'''
given two nodes in a binary tree
find the lowest common ancestor between them
i.e. the lowest node that they are both under
      1
    /   \
   2     3
  / \   / \
 4   5  6  7
 ancestor(4,5) = 2
 ancestor(5,6) = 1
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def ancestor(node, node_1, node_2):
    if node == None:
        return None

    if node == node_1 or node == node_2:
        return node

    if ancestor(node.left,node_1,node_2) and ancestor(node.right,node_1,node_2):
        return node

    return ancestor(node.left,node_1,node_2) or ancestor(node.right,node_1,node_2)





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

result = ancestor(a,f,g)
print(result.value)
