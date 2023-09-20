"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


"""


"""

    first use dfs to get cell which can reach pacific ocean
    then use dfs to get cell which can reach atlantic ocean

    then check which cells are common in both
    return ans


"""



class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:


        m = len(heights)
        n = len(heights[0])

        pacific = set()
        atlantic = set()


        def dfs_utils(i, j, prevHeight, visit):

            if i<0 or i>=m or j<0 or j>=n or (i,j) in visit or heights[i][j] < prevHeight:
                return

            visit.add((i,j))

            dfs_utils(i+1, j, heights[i][j], visit)
            dfs_utils(i, j+1, heights[i][j], visit)
            dfs_utils(i-1, j, heights[i][j], visit)
            dfs_utils(i, j-1, heights[i][j], visit)


        for col in range(n):
            dfs_utils(0, col, heights[0][col], pacific)
            dfs_utils(m-1, col, heights[m-1][col], atlantic)

        for row in range(m):
            dfs_utils(row,0, heights[row][0], pacific)
            dfs_utils(row, n-1, heights[row][n-1], atlantic)


        ans = []
        
        for i in pacific:
            if i in atlantic:
                ans.append(i)
        
        return ans


