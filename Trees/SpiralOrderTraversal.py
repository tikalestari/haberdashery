'''
Print the spiral order traversal of a tree using BFS
     1
   /    \
  3      5
 / \    /  \
7   9  11  13

spiral(1) = 1 3 5 13 11 9 7
'''
from collections import deque

class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children

def spiral(root):
    s = []
    q = deque()
    s.append(root)
    while len(q) > 0 or len(s) > 0:
        size_s = len(s)
        for i in range(size_s):
            node = s.pop()
            print(str(node.value)+" ",end="")
            for n in node.children:
                q.append(n)
        size_q = len(q)
        for j in range(size_q):
            node = q.popleft()
            print(str(node.value)+" ",end="")
            for n in node.children:
                s.append(n)


g = Node(13,[])
f = Node(11,[])
e = Node(9,[])
d = Node(7,[])
c = Node(5,[f,g])
b = Node(3,[d,e])
a = Node(1,[b,c])
spiral(a)
