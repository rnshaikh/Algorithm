#Given an integer. Find how many structurally unique binary search trees are there 
# that stores the values from 1 to that integer (inclusive).


"""
        1) intialize dp array with n+1 0
        2) first 2 0, 1 store 1
        3) for i in range(2, n+1) and j 1 to i+1
        4) for any i there will be i-1 nodes in left tree and n-i in right subtree
        5) sum of product of (i-1) * (n-i)  will be unqiue bst for i

"""

class Solution:
    #Function to return the total number of possible unique BST.
    def numTrees(self,n):


        dp = [0] * (n + 1)

        # Base case
        dp[0], dp[1] = 1, 1

        # fill the dp table in top-down
        # approach.
        for i in range(2, n + 1):
            for j in range(1, i + 1):

                # n-i in right * i-1 in left
                res=(dp[i - j] * dp[j - 1])%1000000007
                dp[i] = (dp[i] + res)%1000000007

        return dp[n]
