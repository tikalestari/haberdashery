'''
Binary Search Tree
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, node):
        r = self.root
        self.add_helper(r, node)

    def add_helper(self, current, node):
        if current is None:
            current = node
        elif node.value > current.value:
            if current.right is None:
                current.right = node
            else:
                self.add_helper(current.right, node)
        else:
            if current.left is None:
                current.left = node
            else:
                self.add_helper(current.left, node)

    def find(self, value):
        r = self.root
        self.find_helper(r, value)

    def find_helper(self, current, value):
        if current.value == value:
            print(str(value) + " is in this tree.")
        elif value > current.value:
            if current.right is None:
                print(str(value) + " is NOT in this tree.")
            else:
                self.find_helper(current.right, value)
        else:
            if current.left is None:
                print(str(value) + " is NOT in this tree.")
            else:
                self.find_helper(current.left, value)

    def remove(self, value):
        r = self.root
        self.remove_helper(r,r,value)

    def remove_helper(self, current, parent, value):
        if current.value == value:
            if node.left is None and node.right is None:
                node = None
            elif node.left is None and node.right:
                parent.right = node.right
            elif node.right is None and node.left:
                parent.left = node.left
        elif value > current.value:
                self.remove_helper(current.right, current, value)
        else:
            self.remove_helper(current.left, current, value)

    def print_tree(self):
        r = self.root
        self.print_tree_helper(r)

    def print_tree_helper(self, node):
        if not node:
            return
        self.print_tree_helper(node.left)
        print(node.value)
        self.print_tree_helper(node.right)

a = Node(5)
b = Node(4)
c = Node(3)
d = Node(7)

tree = BST()
tree.root = a
tree.add(b)
tree.add(c)
tree.add(d)

tree.print_tree()
tree.find(5)
tree.find(4)
