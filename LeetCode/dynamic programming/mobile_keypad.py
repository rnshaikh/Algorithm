"""

Given the mobile numeric keypad. You can only press buttons that are up, left, right, or down to the current button.
You are not allowed to press bottom row corner buttons (i.e. * and # ). Given a number N,
the task is to find out the number of possible numbers of the given length.
"""

"""
    algorithm:
        1) negative case if i,j is outside keypad or # or * return -1
        2) ifn=1 return 1
        3) if i,j,n in dp return dp[i,j,n]
        4) dp[i,j,N] = for all four combination sum

"""




dp = {}

class Solution:

    def dfs(self, dp, keypad, i, j, N):

        if i<0 or j<0 or i >=4 or j >= 3 or keypad[i][j] == -1:
            return 0

        if N == 1:
            return 1

        if (i,j,N) in dp:
            return dp[(i,j,N)]

        dp[(i,j,N)] = (self.dfs(dp,keypad, i, j, N-1) +
                      self.dfs(dp, keypad, i+1, j, N-1) +
                      self.dfs(dp, keypad, i-1, j, N-1) +
                      self.dfs(dp, keypad, i, j-1, N-1) +
                      self.dfs(dp, keypad, i, j+1, N-1))

        return dp[(i,j,N)]


    def getCount(self, N):
        # code here

        keypad = [[1,2,3], [4,5,6], [7,8,9],[-1,0,-1]]

        dp = {}
        count = 0

        for i in range(4):
            for j in range(3):
                if keypad[i][j] != -1:
                    count = count + self.dfs(dp, keypad, i, j, N)
                    #print("count after add", count, N)

        return count
