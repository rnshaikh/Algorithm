"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""

"""
    array hashmap
    hashset to get unique values in array, to check for duplicates easily

"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hash_map = {}

        for i in range(len(nums)):

            if nums[i] not in hash_map:
                hash_map[nums[i]] = i
            else:
                return True

        return False
