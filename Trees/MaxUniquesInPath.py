from collections import deque

class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children

def max_unique(root):
    q = deque()
    q.append(root)
    while len(q) > 0:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            for n in node.children:
                q.append(n)
                




g = Node(13,[])
f = Node(11,[])
e = Node(9,[])
d = Node(7,[])
c = Node(5,[f,g])
b = Node(3,[d,e])
a = Node(1,[b,c])
bfs(a)
