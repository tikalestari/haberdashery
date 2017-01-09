'''
Determine if a tree can be split into two equal parts
'''

class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.subtree_count = 0

def count_subtree(root):
    for node in root.children:
        root.subtree_count += 1 + count_subtree(node)
    return root.subtree_count

def check_split(root):
    if root.subtree_count % 2 == 0:
        return False
    return split(root, (root.subtree_count + 1)/2)

def split(root, half):
    for node in root.children:
        if node.subtree_count == half - 1:
            return True
        if node.subtree_count > 0:
            split(node, half)
    return False

j = Node('j',[])
i = Node('i',[])
h = Node('h',[])
g = Node('g',[h,i,j,k])
f = Node('f',[])
e = Node('e',[])
d = Node('d',[g])
c = Node('c',[])
b = Node('b',[])
a = Node('a',[b,c,d,e,f])
count_subtree(a)
print(check_split(a))
