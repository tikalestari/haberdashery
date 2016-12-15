'''
Given a grid of 1's and 0's, return the number of blobs
made up of 1's.

Example:
[1,0,0,1,1]
[1,1,1,0,1]
[1,1,0,1,1] = 1 blob

[1,0,0,0,1]
[1,1,1,0,1]
[1,1,0,0,1] = 2 blobs

'''

def num_blobs(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                zero_out_blob(matrix, row, col)

def zero_out_blob(matrix, row, col):
