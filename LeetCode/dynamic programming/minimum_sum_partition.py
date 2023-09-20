"""
Given an array arr of size n containing non-negative integers, 
the task is to divide it into two sets S1 and S2 such that the 
absolute difference between their sums is minimum and find the minimum difference

"""


class Solution:
	
	
    def dfs(self, dp, arr, index, sum_, curr_sum):
	    
        if index == len(arr):
            return abs((sum_-curr_sum) - curr_sum)
        
        if dp[index][curr_sum] != -1:
            return dp[index][curr_sum]
        
        dp[index][curr_sum] = min(self.dfs(dp, arr, index+1, sum_, curr_sum), self.dfs(dp, arr, index+1, sum_, curr_sum+arr[index]))
	    return dp[index][curr_sum]
	    
	
	def minDifference(self, arr, n):
		# code here
    
        sum_ = sum(arr)
        dp = [[-1 for _ in range(sum_)] for _ in range(n)]
        
        aa = self.dfs(dp, arr, 0, sum_, 0)
        return aa
        