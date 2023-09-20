"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
"""


"""
    lett and right point with 2 sum
    to remove duplicate sort and compare with last element

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        if n <= 0:
            return nums

        nums.sort()

        ans = []

        for i in range(0, n):
            if i> 0 and nums[i-1] == nums[i]:
                continue

            l = i+1
            r = n-1

            while l < r:

                three_sum = nums[i]+ nums[l]+nums[r]

                if three_sum > 0:
                    r = r-1

                elif three_sum < 0:
                    l = l+1

                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l = l+1
                    while l < r and nums[l] == nums[l-1]:
                        l = l+1
        return ans
