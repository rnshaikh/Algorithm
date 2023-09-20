"""
Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.

A = 6, B = 6
str1 = ABCDGH
str2 = AEDFHR
Output: 3
Explanation: LCS for input Sequences
“ABCDGH” and “AEDFHR” is “ADH” of
length 3.


"""

"""
    same as geek and bridges

"""













class Solution:

    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):

        # code here

        dp = [[0 for _ in range(y+1)] for _ in range(x+1)]

        for i in range(1, x+1):
            for j in range(1, y+1):

                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[x][y]
