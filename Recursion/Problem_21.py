'''
Given a matrix, start at top left
go to the * in the matrix.
The matrix contains X's that are walls.
Find the shortest path
If not possible, return -1
'''
import sys

def star(matrix, row, col):
    if row < 0 or col < 0:
        return sys.maxsize
    elif row >= len(matrix) or col >= len(matrix[0]):
        return sys.maxsize
    elif matrix[row][col] == "*":
        return 0
    elif matrix[row][col] == "X" or matrix[row][col] == 1:
        return sys.maxsize
    elif matrix[row][col] == 0:
        matrix[row][col] = 1
        return 1 + min(star(matrix,row+1,col),star(matrix,row,col+1),
        star(matrix,row-1,col),star(matrix,row,col-1))
    else:
        return sys.maxsize


m = [[0,0,0,0,0],[0,"X","X","X","X"],["*",0,0,0,0]]
print(star(m,0,0))

'''
[0,0,0,0,0]
[0,x,x,x,x]
[*,0,0,0,0]]
'''
