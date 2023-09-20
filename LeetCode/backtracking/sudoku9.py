"""
Given an incomplete Sudoku configuration in terms of a 9 x 9  2-D square matrix (grid[][]), 
the task to find a solved Sudoku. For simplicity, you may assume that there will be only one unique solution.

Sample Sudoku for you to get the logic for its solution:

"""


N = 9

class Solution:
    
    #Function to find a solved Sudoku. 
    
    
    def is_safe(self, grid, curr_row, curr_col, curr_num):
        
        for j in range(0, 9):
            if grid[curr_row][j] == curr_num:
                return False
            
        for i in range(0, 9):
            if grid[i][curr_col] == curr_num:
                return False
                
        
        start_row = curr_row - curr_row % 3
        start_col = curr_col - curr_col % 3
        
        
        for i in range(0, 3):
            for j in range(0, 3):
                if grid[i+start_row][j+start_col] == curr_num:
                    return False
                
        return True
        
    
    def dfs(self, grid, curr_row, curr_col):
        
        if curr_row == N-1 and curr_col == N:
            return True
            
        if curr_col == N :
            curr_col = 0
            curr_row += 1
    
        if grid[curr_row][curr_col] > 0:
            return self.dfs(grid, curr_row, curr_col+1)
        
        for num in range(1, 10, 1):
            if self.is_safe(grid, curr_row, curr_col, num):
                grid[curr_row][curr_col] = num
                if self.dfs(grid, curr_row, curr_col+1):
                    return True
            
            grid[curr_row][curr_col] = 0
            
        return False
        
    
    
    def SolveSudoku(self,grid):
        
        flag = self.dfs(grid, 0, 0)
        
        return flag
    
    
    #Function to print grids of the Sudoku.    
    def printGrid(self,arr):
        
        # Your code here
        
        ans = []
        for i in range(9):
            for j in range(9):
                ans.append(arr[i][j])
                
        for i in ans:
            print(i, end=" ")