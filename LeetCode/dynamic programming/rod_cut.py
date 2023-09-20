"""
Given a rod of length N inches and an array of prices, price[] that contains prices of all pieces of size smaller than N.
Determine the maximum value obtainable by cutting up the rod and selling the pieces.

"""


class Solution:
    def cutRod(self, price, n):
        #code here
        if n == 1:
            return price[0]

        dp = [0 for _ in range(n+1)]

        for i in range(1, n+1):
            dp[i] = price[i-1]


        for i in range(1, n+1):
            for j in range(1, len(price)):
                if i >= j:
                    dp[i] = max(price[j-1]+dp[i-j], dp[i])

        return dp[n]
