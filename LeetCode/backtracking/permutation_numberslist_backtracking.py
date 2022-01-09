"""
    Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        queue = []
        queue.append([])

        while(len(queue)):

            l1 = queue.pop(0)
            if len(l1) == len(nums):
                ans.append(l1)

            else:
                temp = l1.copy()
                for i in nums:

                    if i not in temp:
                        temp.append(i)
                        queue.append(temp.copy())
                        temp.pop(-1)

        return ans
