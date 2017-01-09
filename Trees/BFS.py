'''
Print a tree in BFS.
      1
   /    \
  3      5
 / \    /  \
7   9  11  13

bfs(1) = 1 3 5 7 9 11 13
'''
from collections import deque

class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children

def bfs(root):
    q = deque()
    q.append(root)
    while len(q) > 0:
        node = q.popleft()
        print(node.value)
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
