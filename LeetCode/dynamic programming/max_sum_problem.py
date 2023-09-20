
"""
Given an array arr[] of integers and an integer sum, 
the task is to count all subsets of the given array with a sum equal to a given sum.

Note: Answer can be very large, so, output answer modulo 109+7

"""

"""
    similar to knapsack problem here also we have check if current element is present or not

    if element not present that mean a[w-1] > w then dp[i][w] = dp[i-1][w]
    else element present dp[i][w] = dp[i-1][w-a[w-1]] + dp[i-1][w]  (in knapsack we take maximum of both  here we add)

    base case is d[0][0] = 1 else for row 0 all col from 1 will be 0

    here dp[i][j] store count of subset with sum j from element list from 0 to i
    dp[1][2] will store count of subset with sum 2 for element list from 0 to 1


    row are element col are sums

    row start from 1 to n+1
        col start from 0 to w+1

            if a[w-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = dp[i-1][w] + dp[i-1][w-a[w-1]]

"""








class Solution:

    def perfectSum(self, arr, n, sum):
        # code here

        dp = [[-1 for _ in range(sum+1)] for _ in range(n+1)]

        dp[0][0] = 1

        for j in range(1, sum+1):
            dp[0][j] = 0

#       print("dp b", dp)
        for i in range(1, n+1):
            for j in range(0, sum+1):
                if arr[i-1]> j:
                    dp[i][j] = dp[i-1][j] %  ((10**9)+7)
                elif arr[i-1] <= j:
                    dp[i][j] = (dp[i-1][j] + dp[i-1][j-arr[i-1]]) %  ((10**9)+7)

        #print("dp", dp)
        return dp[n][sum] %  ((10**9)+7)



def perfectSum(self, arr, n, sum):
		# code here
	    
        w = sum
        
        dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
        
        dp[0][0] = 1
        
        for i in range(1, n+1):
            for w in range(w+1):
                if w-arr[i-1] >= 0:
                    dp[i][w] = (dp[i-1][w-arr[i-1]] + dp[i-1][w])
                else:
                    dp[i][w] = dp[i-1][w]
                
                dp[i][w] = dp[i][w] % (10**9+7)
                
        
        return dp[n][w]