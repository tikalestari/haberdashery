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
                if steps < 0:
                    return False
                matrix[row][col] = steps
    for row in matrix:
        print(row)
    return True

def bfs(matrix,cell,k):
    q = deque()
    q.append(cell)
    steps = 0
    directions = [-1,0,1]
    while len(q) > 0:
        steps += 1
        size = len(q)
        for i in range(size):
            current = q.popleft()
            row = current[0]
            col = current[1]
            for r in directions:
                for c in directions:
                    if r != c and r - c != 0 and c + r != 0:
                        print("current: "+ str(r) + " "+ str(c))
                        print("row: "+ str(row+r))
                        print("col: "+str(col+c))
                        print("steps: "+str(steps))
                        if row+r >= len(matrix) or col+c >= len(matrix[0]):
                            pass
                        elif row+r < 0 or col+c < 0:
                            pass
                        elif str(matrix[row+r][col+c]) == 'x':
                            pass
                        elif str(matrix[row+r][col+c]) == 'm' and steps <= k:
                            return steps
                        elif int(matrix[row+r][col+c]) >= 0:
                            q.append((row+r,col+c))
                        print(q)
                        print()
    return -1



m = [[0,0,'m',0,0],[0,'x','x',0,0],['m',0,'m',0,0],[0,0,'x',0,0]]
print(main(m,3))
