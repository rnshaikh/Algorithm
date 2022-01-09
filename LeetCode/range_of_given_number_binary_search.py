"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""


def binary_search(self, nums, low, high, target, fr):

    if(high >= low):
        mid = low + (high - low) // 2
        mid = int(mid)
        if fr == "low":
            if (mid == 0 or target>nums[mid-1]) and nums[mid] == target:
                return mid

            if target > nums[mid]:
                return self.binary_search(nums, (mid+1), high, target, fr)
            else:
                return self.binary_search(nums, low, (mid-1), target, fr)

        if fr == "high":
            if (mid == (len(nums)-1) or target<nums[mid+1]) and nums[mid] == target:
                return mid

            if target < nums[mid]:
                return self.binary_search(nums, low, (mid-1), target, fr)

            else:
                return self.binary_search(nums, (mid+1), high, target, fr)

    else:
        return None


def searchRange(self, nums: List[int], target: int) -> List[int]:


    if len(nums) == 1 and nums[0] == target:
        return [0,0]

    low = self.binary_search(nums, 0, len(nums)-1, target, "low") #self.first(nums, 0, (len(nums)-1), target, len(nums))

    if low == None:
        return [-1, -1]

    high = self.binary_search(nums, 0, len(nums)-1, target, "high") #self.last(nums, 0, (len(nums)-1), target, len(nums))


    return [low, high]
