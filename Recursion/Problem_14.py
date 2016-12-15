'''
Given a NxN matrix,
find the max sum path from top left corner to bottom right corner
only going down and right.
'''
def max_path(matrix, row, col):
    if row == len(matrix)-1 and col == len(matrix)-1:
        return matrix[row][col]
    elif row == len(matrix)-1:
        return matrix[row][col] + max_path(matrix, row, col+1)
    elif col == len(matrix)-1:
        return matrix[row][col] + max_path(matrix, row+1, col)
    else:
        return matrix[row][col] + max(max_path(matrix, row+1, col), max_path(matrix, row, col+1))


l = [[1,2,3],[1,2,3],[1,2,3]]
'''
[1,2,3]
[1,2,3]
[1,2,3]
'''
print(max_path(l,0,0))
