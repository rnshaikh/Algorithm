# Unit Area of largest region of 1's


"""
    1) given adjacency matrix use dfs
    2) traverse all i and j in martrix if a[i][j] is 1 count = 0
    3) given l, m, i, j count to dfs
    4) in dfs if adj[i][j] = 1 and make it 2 to mark as visited then increment count
    5) make recursie call for i , j 8 combination
"""



class Solution:

    #Function to find unit area of the largest region of 1s.
    def __init__(self):
        self.count = 0
    def dfs(self, grid,l, m, i, j):

        if i>=0 and i<l and j>=0 and j<m and grid[i][j]==1:
            grid[i][j] = 2
            self.count = self.count+1
            self.dfs(grid, l, m, i, j+1)
            self.dfs(grid, l, m, i+1, j)
            self.dfs(grid, l, m, i+1, j+1)
            self.dfs(grid, l, m, i, j-1)
            self.dfs(grid, l, m, i-1, j)
            self.dfs(grid, l, m, i-1, j-1)
            self.dfs(grid, l, m, i-1, j+1)
            self.dfs(grid, l, m, i+1, j-1)


    def findMaxArea(self, grid):
        #Code here

        l = len(grid)
        m = len(grid[0])
        max_area = 0

        for i in range(l):
            for j in range(m):
                if grid[i][j] == 1:
                    self.count = 0
                    self.dfs(grid,l,m,i,j)
                    max_area = max(max_area, self.count)
        return max_area
