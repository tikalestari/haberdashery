'''
SUDOKU SOLVER
Determine if the board is solvable
'''

def sudoku(matrix, row, col):
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == 0:
        # if it's blank
        # try each of 9 options
        # if one doesnt work, undo and move to next
        # if it's valid and you can solve the rest
        # of the board, return true
        # otherwise, return false
        for k in range(1,10):
            matrix[i][j] = k
            if is_valid(matrix,i,j,k) and sudoku(matrix,i,j):
                return True
        return False
