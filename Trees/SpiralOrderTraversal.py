'''
Print the spiral order traversal of a tree using BFS
    1
  /    \
  3      5
 / \    /  \
7   9  11  13

spiral(1) = 1 5 3 7 9 11 13
'''
from collections import deque

class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children

def spiral(root):
    s = 
    q = deque()


g = Node(13,[])
f = Node(11,[])
e = Node(9,[])
d = Node(7,[])
c = Node(5,[f,g])
b = Node(3,[d,e])
a = Node(1,[b,c])
level_order(a)
