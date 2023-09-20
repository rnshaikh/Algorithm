"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

"""


"""
    prefix sum hash_map:
    each time add current element in sum and then check if sum_a -k in hash_map if its add in count
    else add current sum in prefix_sum hash_map
"""

class Solution:


    def subarraySum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        prefix_sum = {0:1}
        start = 0
        sum_a = 0
        res = 0
        
        for end in range(n):
            
            sum_a += nums[end]
            
            if sum_a -k in prefix_sum:
                res += prefix_sum[sum_a-k]
            
            prefix_sum[sum_a] = prefix_sum.get(sum_a, 0)+1
            
            
        return res
            


#         get all subarrays with sum k (without negative value) sliding window technique
#         n = len(nums)
#         sum_a = 0
#         ans = []
#         count = 0
        
#         start = 0
        
#         for end in range(0, n):            
#             sum_a += nums[end]

#             while abs(sum_a) > k and start < end:
#                 sum_a -= nums[start]
#                 start = start+1

#             if sum_a == k:
#                 ans.append(nums[start:end+1])
#                 count = count+1
#                 continue
        
#         return count