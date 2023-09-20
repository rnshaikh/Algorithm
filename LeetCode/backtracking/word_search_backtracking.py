

"""
Given an m x n grid of characters board and a string word, 
return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

class Solution:

    def __init__(self):
        self.flag = False

    def check_correct(self, board, rows, cols, curr_row, curr_col, word, no_word, nwp):
        if nwp == no_word:
            self.flag = True
            return

        if curr_row > rows or curr_row <0:
            return

        if curr_col > cols or curr_col < 0:
            return

        if board[curr_row][curr_col] == word[nwp]:
            temp = board[curr_row][curr_col]
            board[curr_row][curr_col] = "#"
            self.check_correct(board, rows, cols, curr_row-1, curr_col, word, no_word, nwp+1)
            self.check_correct(board, rows, cols, curr_row, curr_col-1, word, no_word, nwp+1)
            self.check_correct(board, rows, cols, curr_row+1, curr_col, word, no_word, nwp+1)
            self.check_correct(board, rows, cols, curr_row, curr_col+1, word, no_word, nwp+1)
            board[curr_row][curr_col] = temp


    def find_puzzle(self, board, rows, cols, curr_row, curr_col, word, no_word, nwp):

        if len(word) > len(board) * len(board[0]):
            return self.flag

        if self.flag:
            return True

        if curr_col > cols:
            curr_row = curr_row+1
            curr_col = 0

        if curr_row > rows:
            return

        if board[curr_row][curr_col] == word[nwp]:
            self.check_correct(board, rows, cols, curr_row, curr_col, word, no_word, nwp)

        self.find_puzzle(board, rows, cols, curr_row, curr_col+1, word, no_word, nwp)

        if self.flag:
            return True
        else:
            return False



    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)-1
        n = len(board[0])-1

        flag = self.find_puzzle(board, m, n, 0, 0, word, len(word), 0)
        return flag
        or 

        "you find first word in board call dfs with i,j as current row"
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    self.dfs(board,word,i,j,m,n,0) 
                    if self.flag:
                        return True

        if self.flag:
            return True
        else:
            return False
