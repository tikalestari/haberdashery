'''
Given N, the length of the row and column of a NxN matrix,
find the number of paths from top left corner to bottom right corner
only going down and right

NxN matrix is
l = [[0 for i in range(n)] for i in range (n)]
[0,0,0,0,0]
[0,0,0,0,0]
[0,0,0,0,0]
[0,0,0,0,0]
[0,0,0,0,0]

'''

def path(n, row, col):
    if row > n-1 or col > n-1:
        return 0
    if row == n-1 and col == n-1:
        return 1
    return path(n, row + 1, col) + path(n, row, col + 1)


l = [[0 for i in range(3)] for i in range (3)]
print(path(3,0,0))
