'''
Given a graph of characters and a string, determine
if you can make the string using a traversal of the graph
that includes all nodes. You must use all nodes at least once.
You can't skip a node in the traversal

"catt"
    c
   /
  a
   \
    t   = True

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
        print("tru")
        return True
    if node.value == word[index:index+1]:
        print("yas")
        s.add(node)
        main(node,word,index+1,visited)
    for n in node.nodes:
        if n.value == word[index:index+1]:
            print("woo")
            s.add(n)
            main(n,word,index+1,visited)
    for n in node.nodes:
        if n not in visited:
            return False

    for n in visited:
        print(n.value)
    return True



a = Node('a',[])
t = Node('t',[a])
c = Node('c',[a])
a.nodes.append(c)
a.nodes.append(t)
s = set()
print(main(c,"catte",0,s))
