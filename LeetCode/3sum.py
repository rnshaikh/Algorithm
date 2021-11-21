"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) <= 0:
            return nums

        if len(nums) <= 2:
            return []

        ans = []

        for i in range(0, len(nums)-1):

            s = set()
            for j in range(i+1, len(nums)):
                x= -(nums[i]+nums[j])
                if x in s:
                    dup = False
                    for li in ans:
                        if set(li) == set([x, nums[i], nums[j]]):
                            dup = True
                    if not dup:
                        ans.append([x, nums[i], nums[j]])
                else:
                    s.add(nums[j])
        return ans
