"""

Array hashmap
use hash map to instantly check for difference value, map will add index of last occurrence of a num, don’t use same element twice;
"""


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}

        for i in range(len(nums)):
            hash_map[nums[i]] = i


        for i in range(len(nums)):

            diff = target-nums[i]
            if diff in hash_map and hash_map[diff] != i:
                index_1 = hash_map[diff]
                index_2 = i
                return [index_2, index_1]


        return -1
