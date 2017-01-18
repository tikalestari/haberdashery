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
'''

class Node:
    def __init__(self, value, nodes):
        self.value = value
        self.nodes = nodes

def dfs(node,word):
    for n in node.nodes:
        if n.value == word[0,1]:
            if main(n,word,0,[]):
                return True
    return False 

def main(node,word,index,nodes_list,total_nodes):
    if index == len(word):
        if len(nodes_list) == total_nodes:
            return True

    if node.value == word[index]:
        visited.add(node)
        main(node,word,index,nodes_list,total_nodes)

    already_in_visited = node in nodes_list
    nodes_list.add(node)

    for n in node.nodes:
        if main(n,word,index,nodes_list,total_nodes):
            return True
        return False

    main(node,word,index,nodes_list)

    return False




a = Node('a',[])
t = Node('t',[a])
tt = Node('t',[a])
c = Node('c',[a])
a.nodes.append(c)
a.nodes.append(t)
a.nodes.append(tt)
s = set()
print(main(c,"catt",0,s))
for i in s:
    print(i.value)
