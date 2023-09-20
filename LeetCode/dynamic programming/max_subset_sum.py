"""
Given an array A of size N. Find the maximum subset-sum of elements that you can make from the given array such that for every two consecutive elements in the array, at least one of the elements is present in our subset. 

Example 1:

Input: 
N = 4
A[] = {1, -1, 3, 4}
Output: 8
Explanation: 
We can choose 0th,2nd & 3rd index(0 based 
Index),so that it can satisfy the 
condition & can make maximum sum 8. 


"""


from typing import List

class Solution:
    def findMaxSubsetSum(self, N : int, A : List[int]) -> int:
        # code here
        
        
        dp = [0 for _ in range(N)]
        dp[0] = A[0]
        dp[1] = A[1] + max(0, A[0])
        
        for i in range(2, N):
            
            dp[i] = max(dp[i-1], dp[i-2]) + A[i]
            
        return max(dp[N-1], dp[N-2])

