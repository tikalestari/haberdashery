'''
LeetCode
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent
cell, where "adjacent" cells are those horizontally or vertically
neighboring. The same letter cell may not be used more than once.

Example
Given board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''

def search(board, word):
    letters = list(word)
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == letters[0]:
                if check(board, r, c, word, 1):
                    return True

    return False

def check(board, row, col, word, index):
    if row >= len(board) or col >= len(board[0]):
        return False
    if row < 0 or col < 0:
        return False
    if board[row][col] == 0:
        return False
    if index >= len(word):
        return False

    if board[row][col] == word[index]:
        board[row][col] = 0
        return True

    else:
        return check(board, row, col+1, word, index+1) or \
        check(board, row, col-1, word, index+1) or \
        check(board, row+1, col, word, index+1) or \
        check(board, row-1, col, word, index+1)

    return False



b = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
print(search(b,"ABCCED"))
print(search(b,"SEE"))
print(search(b,"ABCB"))
