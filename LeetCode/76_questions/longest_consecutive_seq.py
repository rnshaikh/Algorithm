"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""


"""

    idea:
        find starting element of seq
        which is element whose dont have prev element in set

        after finding starting element
        tak local_len = 1
        temp = ele
        iterate add 1 in ele and len until element not found

        if local_len greater then max_len then update max_len.


"""



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        num_set = set()

        for i in nums:
            num_set.add(i)

        max_len = 0

        for i in range(len(nums)):

            if nums[i]-1 not in num_set:
                local_len = 1
                temp = nums[i]+1
                while temp in num_set:
                    local_len +=1
                    temp += 1

                if local_len > max_len:
                    max_len = local_len

        return max_len
