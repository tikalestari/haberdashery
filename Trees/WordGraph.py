'''
Given a graph of characters and a string, determine
if you can make the string using a traversal of the graph
that includes all nodes. You must use all nodes at least once.
You can't skip a node in the traversal

"catt"
    c
   /
  a
 / \
t   t   = True

"catt"

    c
   / \
  a   t = False

'''

class Node:
    def __init__(self, value, nodes):
        self.value = value
        self.nodes = nodes


def main(node,word,index,visited):
    if index == len(word):
        return True
    elif node.value == word[index:index+1]:
        visited.add(node)
        return main(node,word,index+1,visited)
    else:
        for n in node.nodes:
            if n.value == word[index:index+1]:
                visited.add(n)
                if main(n,word,index+1,visited):
                    return True
            elif n not in visited:
                return False

    return False




a = Node('a',[])
t = Node('t',[a])
tt = Node('t',[a])
c = Node('c',[a])
a.nodes.append(c)
a.nodes.append(t)
a.nodes.append(tt)
s = set()
print(main(c,"catet",0,s))
for i in s:
    print(i.value)
