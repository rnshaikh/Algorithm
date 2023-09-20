"""
Given a set of N items, each with a weight and a value, represented by the array w[] and val[] respectively. Also, a knapsack with weight limit W.
The task is to fill the knapsack in such a way that we can get the maximum profit. Return the maximum profit.
Note: Each item can be taken any number of times.



"""






"""
Its an unbounded knapsack problem as we can use 1 or more instances of any resource. A simple 1D array, say dp[W+1] can be used such that dp[i] stores the maximum value which can achieved using all items and i capacity of knapsack. Note that we use 1D array here which is different from classical knapsack where we used 2D array. Here number of items never changes. We always have all items available.
We can recursively compute dp[] using below formula

dp[i] = 0
dp[i] = max(dp[i], dp[i-wt[j]] + val[j]
                   where j varies from 0
                   to n-1 such that:
                   wt[j] <= i

result = d[W]

"""



class Solution:
    def knapSack(self, N, W, val, wt):
        # code here

        dp = [0 for _ in range(W+1)]


        for i in range(1, W+1):
            for j in range(N):
                ele_not_present = dp[i]
                ele_present = 0

                if i-wt[j] >= 0:
                    ele_present = dp[i-wt[j]] + val[j]

                dp[i] = max(ele_present, ele_not_present)

        return dp[W]
