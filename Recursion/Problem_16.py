'''
Given a 2D grid of 1's and 0's, find the LARGEST island of 1's.
Will solve in a bit.

[1,0,0,0,1]
[1,1,1,0,1]
[1,1,0,0,1] = 6

[1,0,1,0,1]
[1,1,1,0,1]
[1,1,0,0,1] = 7

[1,0,1,0,1,0,0,0,0,1]
[1,1,1,0,1,0,0,1,1,1]
[1,1,0,0,1,0,1,1,1,1] = 8

'''

def num_islands(matrix):
    largest = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                current = zero_out_island(matrix, row, col)
                if current > largest:
                    largest = current
    return largest

def zero_out_island(matrix, row, col):
    if row >= len(matrix) or col >= len(matrix[0]):
        return 0
    elif row < 0 or col < 0:
        return 0
    elif matrix[row][col] == 0:
        return 0

    matrix[row][col] = 0
    result = 1
    for i in range(-1,2):
        for j in range(-1,2):
                result += zero_out_island(matrix, row+i, col+j)

    return result


m = [[1,0,1,0,1,0,0,0,0,1],[1,1,1,0,1,0,0,1,1,1],[1,1,0,0,1,0,1,1,1,1]]
print(num_islands(m))
