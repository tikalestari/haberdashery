'''
Find shortest path using BFS
     1
   /    \
  3      5
 / \    /  \
7   9  11  13

shortest(13,9) = 2
'''

from collections import deque

class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children

def shortest(node1, node2):
    q = deque()
    q.append(node1)
    edges = 0
    while len(q) > 0:
        edges += 1
        size = len(q)
        for i in range(size):
            node = q.popleft()
            for n in node.children:
                if n is node2:
                    return edges
                q.append(n)

    return -1







g = Node(13,[])
f = Node(11,[])
e = Node(9,[])
d = Node(7,[])
c = Node(5,[f,g])
b = Node(3,[d,e])
a = Node(1,[b,c])
g.children.append(c)
f.children.append(c)
e.children.append(b)
d.children.append(b)
b.children.append(a)
c.children.append(a)
print(shortest(e,g))
