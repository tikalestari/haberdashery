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
    # iterate through row and col, checking each cell
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                # counts as one island
                count += 1
                # clear out island
                zero_out_island(matrix, row, col)
    return count

def zero_out_island(matrix, row, col):
    # if row/col index is out of bounds, return.
    # also known as flood fill algorithm
    if row >= len(matrix) or col >= len(matrix[0]):
        return
    elif row < 0 or col < 0:
        return
    elif matrix[row][col] == 0:
        return
    # update cell to 0
    matrix[row][col] = 0
    # clear attached islands in directions down, right, up, left
    zero_out_island(matrix, row+1, col)
    zero_out_island(matrix, row, col+1)
    zero_out_island(matrix, row-1, col)
    zero_out_island(matrix, row, col-1)
    # all diagonal directions
    zero_out_island(matrix, row+1, col+1)
    zero_out_island(matrix, row-1, col-1)
    zero_out_island(matrix, row-1, col+1)
    zero_out_island(matrix, row+1, col-1)


m = [[1,0,0,0,1],[1,1,1,0,1],[1,1,0,0,1]]
print(num_islands(m))
