
"""
iven an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

"""


"""
dfs solution
"""




class Solution:

    # diagonal including 8 direction

    def dfs_util(self, grid, row, col, n, m):
        #print("row, col", row, col)
        if row >= n or row<0 or col<0 or col >= m or grid[row][col] == 0:
            return

        if grid[row][col] == 1:
            grid[row][col] = 0
            self.dfs_util(grid, row, col+1, n, m)
            self.dfs_util(grid, row, col-1, n, m)
            self.dfs_util(grid, row+1, col, n, m)
            self.dfs_util(grid, row-1, col, n, m)
            self.dfs_util(grid, row+1, col+1, n, m)
            self.dfs_util(grid, row+1, col-1, n, m)
            self.dfs_util(grid, row-1, col+1, n, m)
            self.dfs_util(grid, row-1, col-1, n, m)


    def numIslands(self,grid):
        #code here

        if len(grid) <= 0 or len(grid[0])<=0:
            return 0

        n = len(grid)
        m = len(grid[0])

        cnt = 0
        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] == 1:
                    self.dfs_util(grid, i, j, n, m)
                    cnt += 1

        return cnt




class Solution:

    # diagonal excluding 4 direction
    def dfs_util(self, grid, row, col):

        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
            return

        grid[row][col] = "0"

        self.dfs_util(grid, row, col+1)
        self.dfs_util(grid, row, col-1)
        self.dfs_util(grid, row+1, col)
        self.dfs_util(grid, row-1, col)

    def numIslands(self, grid: List[List[str]]) -> int:

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs_util(grid, i, j)
                    cnt += 1
        return cnt

