"""
Given an array arr[] of n integers,
construct a Product Array prod[] (of same size) such that prod[i] is equal to the product of all the elements of arr[] except arr[i].
Solve it without division operator in O(n) time.
"""


"""
    algorithm:
    take suffix array which store product of all number suffix to current number in [n-1] = 1
    take prefix array which store product of all number prefix to current number in [0] = 1
    take prod_ans array for storing product except himself

    traverse array for 1 to n
        find prefix of current number
        prefix[i] = prefix[i-1] * arr[i-1]

    traverse array from n-2 to 0
        find suffix product of current number
        suffix[i] = suffix[i+1] * arr[i+1]

    traverse from 0 to n
        caluclate prod
        prod[i] = prefix[i] * suffix[i]

"""

class Solution:
    def productExceptSelf(self, nums, n):
        #code here

        prefix = [1 for _ in range(n)]
        suffix = [1 for _ in range(n)]
        prod_ans=[1 for _ in range(n)]

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        for j in range(n-2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j+1]

        for i in range(n):
            prod_ans[i] = prefix[i]*suffix[i]

        return prod_ans


def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = [[1,1] for _ in range(len(nums))]

        for i in range(1, len(nums)):
            
            prod[i][0] = nums[i-1] * prod[i-1][0]
            
        
        for j in range(len(nums)-2, -1, -1):
            
            prod[j][1] = nums[j+1] * prod[j+1][1]
        
        
        for i in range(len(nums)):
            prod[i] = prod[i][0] * prod[i][1]
        
        
        return prod






/// o(1) space 
        ans = [1  for _ in range(n)]
        pref = 1
        suff = 1

        for i in range(n):

            ans[i] = ans[i] * pref
            pref = pref*nums[i]
            
            ans[n-i-1] = ans[n-i-1] * suff
            suff = suff * nums[n-i-1]
        
        return ans