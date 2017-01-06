class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def inorder(node):
    if node is not None:
        yield from inorder(node.left)
        yield node.value
        yield from inorder(node.right)

def preorder(node):
    if node is not None:
        yield node.value
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        yield node.value



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
t1 = inorder(f)
print(next(t1))
print(next(t1))
print(next(t1))
print("Pre-Order Traversal:")
t2 = preorder(f)
next(t2)
print("Post-Order Traversal:")
t3 = postorder(f)
next(t3)
