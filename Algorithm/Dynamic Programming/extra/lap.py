"""
Given an array called A[] of sorted integers having no duplicates, 
find the length of the Longest Arithmetic Progression (LLAP) in it.


# Idea here is to use Dynamic programming to avoid extra searches.
# To be an arithmetic sequence the numbers have to have the same difference. So we can use
# this difference as a key to our dictionary to store the sequence length so for.
# [3,6,9,12]
# 1st iter: 3 : [{0:1}] [diff: seq_length]
# 2nd iter: 6 : [6-3: 2]
# 3rd iter: 9 : [9-3: 2, 9-6: 2+1] because 9-6==3 also exists in the dict of 6
# so on ...
"""



class Solution:
    
    def lengthOfLongestAP(self, A, n):
        # code here
        
        
        arr = A
        dp = {}
        max_length = 0
        dp[0] = {}
        
        for i in range(1, n):
            dp[i] = {}
            for j in range(0, i):
                diff = arr[i] - arr[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff]+1
                else:
                    dp[i][diff] = 2
                    
            
                max_length = max(max_length, dp[i][diff])
                
        return max_length
        