"""
    Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.



"""



"""
    same as kadane alogrithm max sum sub array

    but heare we maintain curr_max and curr_min
    for num = 0 we start curr_max and curr_min as 1



"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)
        curr_max = 1
        curr_min = 1


        for i in nums:
            if i == 0:
                curr_max=1
                curr_min = 1
                continue

            temp = curr_max * i
            curr_max = max(i*curr_max, i*curr_min, i)
            curr_min = min(temp, i*curr_min, i)

            #print("curr_max, curr_min", curr_max, curr_min)
            res = max(curr_max, res)

        return res
