'''
Binary Search Tree
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bst_add(root, node):
    if root is None:
        root = node
    elif root.value > node.value:
        if root.left is None:
            root.left = node
        else:
            bst_add(root.left, node)
    elif root.right is None:
        root.right = node
    else:
        bst_add(root.right, node)

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
bst_add(a,b)
bst_add(a,c)
bst_add(a,d)

print_tree(a)
