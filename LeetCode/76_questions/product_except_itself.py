"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

"""





class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod = 1
        zero_exist = False
        count = 0

        for i in nums:
            if i == 0:
                zero_exist = True
                count = count + 1

            else:
                prod = prod * i

        if count == len(nums):
            return nums

        if count > 1:
            prod = 0

        for i in range(len(nums)):

            if zero_exist and nums[i] != 0:
                nums[i] = 0
            elif zero_exist and nums[i] == 0:
                nums[i] = prod
            else:
                nums[i] = prod // nums[i]

        return nums
