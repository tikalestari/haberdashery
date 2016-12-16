'''
Given a grid of 1's and 0's, return the number of islands
made up of 1's.

Example:
[1,0,0,1,1]
[1,1,1,0,1]
[1,1,0,1,1] = 1 island

[1,0,0,0,1]
[1,1,1,0,1]
[1,1,0,0,1] = 2 islands

'''

def num_islands(matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                count += 1
                zero_out_island(matrix, row, col)
    return count

def zero_out_island(matrix, row, col):
    if row >= len(matrix) or col >= len(matrix[0]):
        return
    elif row < 0 or col < 0:
        return
    elif matrix[row][col] == 0:
        return
    matrix[row][col] = 0
    zero_out_island(matrix, row+1, col)
    zero_out_island(matrix, row, col+1)
    zero_out_island(matrix, row-1, col)
    zero_out_island(matrix, row, col-1)



m = [[1,0,0,0,1],[1,1,1,0,1],[1,1,0,0,1]]
print(num_islands(m))
