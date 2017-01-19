'''
Binary Search Tree
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def binary(root, node):
    if root is None:
        root = node
    elif root.value > node.value:
        if root.left is None:
            root.left = node
        else:
            binary(root.left, node)
    elif root.right is None:
        root.right = node
    else:
        binary(root.right, node)

def print_tree(root):
    if not root:
        return
    print_tree(root.left)
    print(root.value)
    print_tree(root.right)

a = Node(5)
b = Node(4)
c = Node(3)
d = Node(7)
binary(a,b)
binary(a,c)
binary(a,d)

print_tree(a)
