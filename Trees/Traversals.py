class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.value)
        inorder(node.right)

def preorder(node):
    if node is not None:
        print(node.value)
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.value)



a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')

f.left = b
f.right = g
b.left = a
b.right = d
d.left = c
d.right = e
g.right = i
i.left = h

print("In-Order Traversal:")
inorder(f)
print("Pre-Order Traversal:")
preorder(f)
print("Post-Order Traversal:")
postorder(f)
