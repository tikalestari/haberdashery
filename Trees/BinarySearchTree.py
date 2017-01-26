'''
Binary Search Tree
       8
     /   \
    3     10
   / \      \
  1   6      14
     /  \    /
     4   7 13
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

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
                node.parent = current
            else:
                self.add_helper(current.right, node)
        else:
            if current.left is None:
                current.left = node
                node.parent = current
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

    def find_min(self):
        r = self.root
        return self.find_min_helper(r)

    def find_min_helper(self, root):
        if root.left is None:
            print("The minimum of this tree is "+ str(root.value))
            return root
        return self.find_min_helper(root.left)

    def find_max(self):
        r = self.root
        return self.find_max_helper(r)

    def find_max_helper(self, root):
        if root.right is None:
            print("The maximum of this tree is "+ str(root.value))
            return root
        return self.find_max_helper(root.right)


    def find_successor(self, value):
        r = self.root
        m = self.find_max()
        if value == m.value:
            print("No successor")
            return None
        return self.find_successor_helper(r,value)

# if value is max, no successor
# if value has a right subtree, successor is minimum of that subtree,
# if doesnt have subtree and is not max, the successor is one of its ancestors

    def find_successor_helper(self, current, value):
        if current.value == value:
            if current.left is None and current.right is None:
                p = current.parent
                while p.value < value:
                    p = p.parent
                result = p
                print("Successor of "+str(value)+" is "+ str(result.value))
            if current.right:
                result = self.find_min_helper(current.right)
                print("Successor of "+str(value)+" is "+ str(result.value))
                return result
        elif value > current.value:
            if current.right is None:
                print(str(value) + " is NOT in this tree.")
            else:
                self.find_successor_helper(current.right, value)
        else:
            if current.left is None:
                print(str(value) + " is NOT in this tree.")
            else:
                self.find_successor_helper(current.left, value)

    def print_tree(self):
        r = self.root
        self.print_tree_helper(r)

    def print_tree_helper(self, node):
        if not node:
            return
        self.print_tree_helper(node.left)
        print(node.value)
        self.print_tree_helper(node.right)

a = Node(8)
b = Node(3)
c = Node(1)
d = Node(6)
e  = Node(4)
f  = Node(7)
g = Node(10)
h  = Node(14)
i  = Node(13)

tree = BST()
tree.root = a
tree.add(b)
tree.add(c)
tree.add(d)
tree.add(e )
tree.add(f )
tree.add(g)
tree.add(h )
tree.add(i )

tree.print_tree()
tree.find(5)
tree.find_min()
tree.find_max()
tree.find_successor(10)
