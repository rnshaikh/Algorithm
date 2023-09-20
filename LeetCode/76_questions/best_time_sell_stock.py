"""
121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, Return 0.

"""

"""
    Array
    find local min and search for local max, sliding window;
    
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_p = 0

        while r < len(prices):

            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_p = max(max_p, profit)
            else:
                l = r
            r = r+1
        return max_p
