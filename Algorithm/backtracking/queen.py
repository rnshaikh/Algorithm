


class NQueen:


    def __init__(self):

        pass

    def is_safe(self, row, col, ans):
        if 1 in ans[row]:
            return False

        temp_row = 0
        while temp_row < len(ans):
            if ans[temp_row][col] == 1 :
                return False
            temp_row = temp_row+1

        temp_row = row
        temp_col = col
        while temp_row <= len(ans)-1 and temp_col <= len(ans)-1:
            if ans[temp_row][temp_col] == 1:
                return False
            temp_row = temp_row+1
            temp_col = temp_col+1

        temp_row = row
        temp_col = col
        while temp_row >= 0 and temp_col >= 0:
            if ans[temp_row][temp_col] == 1:
                return False
            temp_row = temp_row-1
            temp_col = temp_col-1

        temp_row = row
        temp_col = col
        while temp_row <= len(ans)-1 and temp_col >= 0:
            if temp_col >= 0:
                if ans[temp_row][temp_col] == 1:
                    return False
            temp_row = temp_row+1
            temp_col = temp_col-1

        temp_row = row
        temp_col = col
        while temp_row>=0 and temp_col <= len(ans)-1:
            if temp_col >= 0:
                if ans[temp_row][temp_col] == 1:
                    return False
            temp_row = temp_row-1
            temp_col = temp_col+1

        return True

    def recurse(self, ans, row, col, queens):

        if queens == 0:
            print("Answer of queens", ans)
            exit()

        if col >= len(ans):
            row = row+1
            col = 0

        if row >= len(ans):
            return

        if(self.is_safe(row, col, ans) == True):
            ans[row][col] = 1
            self.recurse(ans, row, col, queens-1)
            ans[row][col] = 0

        self.recurse(ans, row, col+1, queens)


    def solve(self, n):

        ans = [[0 for _ in range(n)]  for _ in range(n)]
        ans = self.recurse(ans, 0, 0, n)






if __name__ == "__main__":

    n = int(input("Enter a number of Queen:"))
    que = NQueen()
    que.solve(n)




class Solution:

    def __init__(self):
        self.ans = []    
    
    def is_safe(self, board, row, col):
        
        n = len(board)
        for i in range(0, n):
            if board[i][col] == 1:
                return False
        
        for j in range(0, n):
            if board[row][j] == 1:
                return False
        
        i = row
        j = col

        while i < n and j < n:
            if board[i][j] == 1:
                return False
            i = i+1
            j = j+1

        i = row
        j = col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i = i-1
            j = j-1
        
        i = row
        j = col 

        while i < n and j >= 0:
            if board[i][j] == 1:
                return False
            i = i+1
            j = j-1
        
        i = row
        j = col

        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i = i-1
            j = j+1
        
        return True


    def dfs(self, board, row, col, n):
        
        if n == 0:
            self.ans.append(copy.deepcopy(board))
            return True
        
        if col >= len(board):
            row += 1
            col = 0
        
        if row >= len(board):
            return False

        if self.is_safe(board, row, col):
            board[row][col] = 1
            self.dfs(board, row, col, n-1)
            board[row][col] = 0

        self.dfs(board, row, col+1, n)


    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [[0 for _ in range(n)] for _ in range(n)]
        self.dfs(board, 0, 0, n)
        
        solutions = []
        for bo in self.ans:
            sols = []
            for i in range(n):
                st = ""
                for j in range(n):
                    if bo[i][j] == 0:
                        st += "."
                    else:
                        st +="Q"
                sols.append(st)
            solutions.append(sols)    
        return solutions
        