"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

"""



class Solution:


    def divide(self, nums, low, high, n):

        mid = (low + high) / 2
        mid = int(mid)

        if low < 0 or high < 0:
            return
        if low > (n-1) or high > (n-1):
            return

        if mid == 0 and nums[mid] > nums[mid+1]:
            return mid

        elif mid == n-1 and nums[mid] > nums[mid-1]:
            return mid

        elif nums[mid] > nums[mid-1] and nums[mid]>nums[mid+1]:
            return mid

        if nums[mid] < nums[mid-1]:
            return self.divide(nums, low, mid-1, n)
        else:
            return self.divide(nums,mid+1, high, n)



    def findPeakElement(self, nums: List[int]) -> int:

#         if len(nums)<=1:
#             return 0

#         for i in range(1, len(nums)-1):

#             if nums[i]> nums[i-1] and nums[i] > nums[i+1]:
#                 return i


#         if nums[-1] > nums[-2]:
#             return len(nums)-1

#         return 0

        if len(nums)<=1:
             return 0

        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        return self.divide(nums, 0, len(nums)-1, len(nums))
