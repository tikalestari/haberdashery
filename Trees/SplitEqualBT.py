'''
Determine if a tree can be split into two equal parts

'''

class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.subtree_count = 0

def count_subtree(root):
    count = 0
    for node in root.children:
        count += 1 + count_subtree(node)
    root.subtree_count = count
    return count + 1

def split(root):
    for node in root.children:
        if root.subtree_count == node.subtree_count:
            return True
        return False


j = Node('j',[])
i = Node('i',[])
h = Node('h',[])
g = Node('g',[h,i,j])
f = Node('f',[])
e = Node('e',[])
d = Node('d',[g])
c = Node('c',[])
b = Node('b',[])
a = Node('a',[b,c,d,e,f])
count_subtree(a)
print(a.subtree_count)
print(d.subtree_count)
print(g.subtree_count)
print(i.subtree_count)
