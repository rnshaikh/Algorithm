"""
Given a gold mine called M of (n x m) dimensions. 
Each field in this mine contains a positive integer which is the amount of gold in tons. 
Initially the miner can start from any row in the first column. From a given cell, the miner can move

to the cell diagonally up towards the right
to the right
to the cell diagonally down towards the right
Find out maximum amount of gold which he can collect.


"""






# User function Template for Python3

class Solution:
    def maxGold(self, n, m, M):
        # code here

        dp = [[0 for _ in range(m)] for _ in range(n)]
        max_col = -10

        for i in range(n):
            dp[i][0] = M[i][0]
            if max_col < dp[i][0]:
                max_col = dp[i][0]

        for i in range(1, m):
            for j in range(n):
                up_right_digonal = 0
                down_right_digonal = 0
                right = 0
                if i-1 >= 0:
                    #print("right", dp[j][i-1], M[j][i])
                    right = dp[j][i-1]
                if j+1>=0 and j+1<n and i-1>=0:
                    #print("down_right_digonal", dp[j+1][i-1], M[j][i])
                    down_right_digonal = dp[j+1][i-1]
                if j-1 >= 0 and j-1<n and i-1>=0:
                    #print("up_right_digonal", dp[j-1][i-1], M[j][i])
                    up_right_digonal = dp[j-1][i-1]

                dp[j][i] = max(right, down_right_digonal, up_right_digonal) + M[j][i]

                if max_col <= dp[j][i]:
                    max_col = dp[j][i]

        #print("dp", dp)
        return max_col


