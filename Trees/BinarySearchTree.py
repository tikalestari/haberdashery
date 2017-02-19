'''
Binary Search Tree
       8
     /   \
    3     10
   / \      \
  1   6      14
     /  \    /
     4   7 13

pic of binary tree
https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/300px-Binary_search_tree.svg.png
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
        return None

    def remove(self, value):
        r = self.root
        self.remove_helper(r,value)

    def remove_helper(self, current, value):
        if current.value == value:
            if not current.left and not current.right: # leaf node
                if current.value > current.parent.value:
                    current.parent.right = None
                else:
                    current.parent.left = None
                return
            elif not current.left and current.right: # only has right child
                if current.value > current.parent.value:
                    current.parent.right = current.right
                else:
                    current.parent.left = current.right
                return
            elif not current.right and current.left: # only has left child
                if current.value > current.parent.value:
                    current.parent.right = current.left
                else:
                    current.parent.left = current.left
                return
            elif current.right and current.left: # has two children
                right_child = current.right
                left_child = current.left
                min_right_subtree = self.find_min_helper(right_child)
                self.remove_helper(right_child, min_right_subtree.value)
                self.print_tree()
                if self.root.value == value:
                    new_root = Node(min_right_subtree.value)
                    new_root.left = left_child
                    new_root.right = right_child
                    self.root = new_root
                    return
                elif current.value > current.parent.value:
                    current.parent.right = min_right_subtree
                    min_right_subtree.left = left_child
                    min_right_subtree.right = right_child
                    return
                else:
                    current.parent.left = min_right_subtree
                    min_right_subtree.left = left_child
                    min_right_subtree.right = right_child
                    return
        elif value > current.value:
            if current.right:
                self.remove_helper(current.right, value)
            else:
                print("oops node not found")
                return
        else:
            if current.left:
                self.remove_helper(current.left, value)
            else:
                print("oops node not found")
                return
        print("removed" + str(value))
        return


    def find_min(self):
        r = self.root
        return self.find_min_helper(r)

    def find_min_helper(self, root):
        if root.left is None:
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

    def find_closest_element(self, k):
        r = self.root
        return self.find_closest_element_helper(r, k)

    def find_closest_element_helper(self, current, k):
        if not current:
            return
        if current.value == k:
            return current.value
        elif k < current.value:
            find_closest_element_helper(current.left, k)
        elif k > current.value:
            find_closest_element_helper(current.right, k)
        return

    def print_tree(self):
        r = self.root
        self.print_tree_helper(r)

    def print_tree_helper(self, node):
        if not node:
            return
        self.print_tree_helper(node.left)
        print(node.value)
        self.print_tree_helper(node.right)

def inorder(node):
    if node is not None:
        yield from inorder(node.left)
        yield node.value
        yield from inorder(node.right)

def verify_if_bst(root):
    inorder_traversal = inorder(root)
    node = next(inorder_traversal)
    next_node = next(inorder_traversal)
    while node < next_node:
        node = next_node
        try:
            next_node = next(inorder_traversal)
        except StopIteration:
            break
    if node > next_node:
        return False
    else:
        return True

def is_sum_tree(root):
# return True if the value of the root is equal to sum of the nodes
# in its left and right subtrees.
    if not root:
        return True
    if not root.left and not root.right:
        return True
    left_sum = sum_helper(root.left)
    right_sum = sum_helper(root.right)
    if root.value == left_sum + right_sum:
        return True
    return False

def sum_helper(root):
    if not root:
        return 0
    else:
        return sum_helper(root.left) + root.value + sum_helper(root.right)


def two_node_sum(value, root): #not finished
    if value == root.value:
        return True
    if root.left:
        return two_node_sum(value,root.left)
    if root.right:
        return two_node_sum(value,root.left)
    else:
        c = value - root.value
        if root.left and root.right:
            if two_node_sum(c, root.left):
                return True
            if two_node_sum(c, root.left):
                return True
        elif root.left:
            if two_node_sum(c, root.left):
                return True
        elif root.right:
            if two_node_sum(c, root.right):
                return True
        else:
            return False


    return False


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


aa = Node(8)
bb = Node(1)
cc = Node(10)
dd = Node(4)

aa.left = cc
aa.right = bb
bb.right = dd

sum_tree = BST()
sum_tree.root = Node(30)
sum_tree.add(Node(10))
sum_tree.add(Node(5))
sum_tree.add(Node(7))
sum_tree.add(Node(8))


tree.print_tree()
tree.find(5)
tree.find_min()
tree.find_max()
tree.find_successor(10)
tree.remove(8)
print()
tree.print_tree()
print(verify_if_bst(aa))
print(is_sum_tree(sum_tree.root))
sum_tree.print_tree()
