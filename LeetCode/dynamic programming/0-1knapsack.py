"""
    Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
    In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively.
    Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.
    You cannot break an item, either pick the complete item or don’t pick it (0-1 property).

"""


"""
    Algorithm :
        we have given knapsack of capacity W
        and element with val = [] values and respective wt = [] weights

        so we have push element in knapsack such  values will be maximum and weight will we less than equal to capacity


        so in brute-force. we can go check all possibilities of whether current element is present or not


        dp:
            optimal structure:
                there are 2 cases
                if current element is present
                    then value = current_value + value[n-1] and w = W-current element weight
                else current element is not present:
                    value = values of [n-1] and w will same as W


        for dp will take 2d array
        row will be not element+1 that is n+1
        col will be capacity+1 that is W+1

        here we will go from 1 to n+1 element and capacity will go from  0 to W+1

        for i in range(n+1):
            for w in range(W+1):
                elem_not_present = dp[i-1][w] if element is not present then value will be same as last value
                ele_present = 0

                if w-wt[i-1] >=0  :  that means if current element capacity w[i-1] <= w current capacity

                    ele_presenr = val[i-1] + a[i-1][w-wt[i-1]]    ele_present values current_value + a[i-1][w-wt[i-1]] value of element last element whose weight is w-wt[i-1]
                    
                dp[i][w] = max(elem_not_present, ele_present)

        return dp[i][w] which will give you max sum of value with capacity W

"""










class Solution:

    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):


        dp = [[0 for _ in range(W+1)] for _ in range(n+1)]


        for i in range(1, n+1):
            for w in range(0, W+1):

                value_not_present = dp[i-1][w]
                value_present = 0

                if w-wt[i-1] >= 0:
                    value_present = dp[i-1][w-wt[i-1]] + val[i-1]

                dp[i][w] = max(value_present, value_not_present)

        return dp[n][w]

"""
    brute force:
        A simple solution is to consider all subsets of items and calculate the total weight and value of all subsets.
        Consider the only subsets whose total weight is smaller than W. From all such subsets, pick the maximum value subset.

        Optimal Sub-structure: To consider all subsets of items, there can be two cases for every item.

            Case 1: The item is included in the optimal subset.
            Case 2: The item is not included in the optimal set.

            Therefore, the maximum value that can be obtained from ‘n’ items is the max of the following two values.
                Maximum value obtained by n-1 items and W weight (excluding nth item).
                Value of nth item plus maximum value obtained by n-1 items and W minus the weight of the nth item (including nth item).


"""

def knapSack(W, wt, val, n):

    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))
