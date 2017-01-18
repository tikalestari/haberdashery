'''
Determine the number of connected components in a graph
'''
class Node:
    self __init__(self, value, nodes):
        self.value = value
        self.nodes = nodes
        self.visited = False

def dfs(node):
    n.visited = True
    for n in node.nodes:
        dfs(n)

def connected(graph):
    result = 0
    for node in graph:
        if not node.visited:
            dfs(node)
            result += 1

    return result
