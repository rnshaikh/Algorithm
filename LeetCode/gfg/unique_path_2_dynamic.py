"""
    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
    The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
    Now consider if some obstacles are added to the grids. How many unique paths would there be?
    An obstacle and space is marked as 1 and 0 respectively in the grid.
"""

"""
    this is similiar to unique_path problem in dynamice programming just 1 condition there is obstacle.

    so here also we are going to use dynamic programming bottom-up apporach starting from first position to last position

    heere ans is store in ans[m][n] matrix

    intial case:
        in 1 st row we can reach at cell in one way only right so all value will be 1
        in 1 st col we can reach at cell in one way only down  so all value will be 1

        in initial case if there is obstacle in 1st row then from there to last cell in row will be 0
        in intial  case if there is obstacle in 1st col then from there to last cell in col will be 0

    we going to travese from 2 row and 2nd col:
        if obstacl is there then:
            ans[i][j] = 0
        else:
            ans in [i][j] = lastrow,currcol + currrow,lastcol ex. ans[i-1][j] + ans[i][j-1]


    last ans will be in m-1,n-1 cell

"""






class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        ans_grid = [[0 for _ in range(n)] for _ in range(m)]
        flag = False
        for i in range(n):
            if flag==True or obstacleGrid[0][i] == 1:
                ans_grid[0][i] = 0
                flag = True
            else:
                ans_grid[0][i] = 1

        flag = False

        for i in range(m):
            if flag == True or obstacleGrid[i][0] == 1:
                ans_grid[i][0] = 0
                flag = True
            else:
                ans_grid[i][0] = 1


        for i in range(1, m):
            for j in range(1, n):

                if obstacleGrid[i][j] == 1:
                    ans_grid[i][j] = 0
                else:
                    ans_grid[i][j] = ans_grid[i-1][j] + ans_grid[i][j-1]


        return ans_grid[m-1][n-1]



class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        
        is_obstacle = 0
        for i in range(m):
            if obstacleGrid[0][i] == 1:
                is_obstacle = 1
                dp[0][i] = 0
                continue
                
            if is_obstacle:
                dp[0][i] = 0
            else:
                dp[0][i] = 1
                
        is_obstacle = 0
        for j in range(n):
            if obstacleGrid[j][0] == 1:
                is_obstacle = 1
                dp[j][0] = 0
                continue
            
            if is_obstacle:
                dp[j][0] = 0
            else:
                dp[j][0] = 1
        
        
        for i in range(1, n):
            for j in range(1, m):
                
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        
        return dp[n-1][m-1]