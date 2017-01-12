'''
Given a matrix with an office layout, return True if every empty space
in the office can reach a micro-kitchen in K or less steps.

[0,0,m,0,0]
[0,x,x,0,0]
[m,0,m,0,0]
[0,0,x,0,0] = True
'''
from collections import deque

def main(matrix,k):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                steps = bfs(matrix,(row,col),k)
                if not steps:
                    return False
                matrix[row][col] = steps
    for row in matrix:
        print(row)
    return True

def bfs(matrix,cell,k):
    q = deque()
    q.append(cell)
    steps = 0
    directions = [[1,0],[0,1],[-1,0],[0,-1]]
    while len(q) > 0:
        steps += 1
        size = len(q)
        for i in range(size):
            current = q.popleft()
            row = current[0]
            col = current[1]
            for d in directions:
                r = d[0]
                c = d[1]
                if row+r >= len(matrix) or col+c >= len(matrix[0]):
                    pass
                elif row+r < 0 or col+c < 0:
                    pass
                elif str(matrix[row+r][col+c]) == 'x':
                    pass
                elif str(matrix[row+r][col+c]) == 'm' and steps > k:
                    return -1
                elif str(matrix[row+r][col+c]) == 'm' and steps <= k:
                    return steps
                else:
                    q.append((row+r,col+c))
    return -1



m = [[0,0,'m',0,0],[0,'x','x',0,0],['m',0,'m',0,0],[0,0,'x',0,0]]
print(main(m,3))
