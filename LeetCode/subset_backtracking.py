"""
Given an integer array nums of unique elements, return all possible subsets (the power set).


"""

import math

class Solution:

    def check(self, nums, an):

        if set(nums) == set(an):
            return False
        else:
            return True


    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        queue = []
        queue.append([])

        len_in = len(nums)

        while(len(queue)):

            an = queue.pop(0)
            if len(ans) <=0:
                ans.append(an)
            else:
                flag = True
                for i in ans:
                    if set(i) == set(an):
                        flag = False
                        break
                if flag:
                    ans.append(an)

            if len(an) <= len_in-1:
                temp = an.copy()
                for i in nums:
                    temp.append(i)
                    queue.append(temp.copy())
                    temp.pop(-1)

        return ans






import math

class Solution:

    def check(self, nums, an):

        if set(nums) == set(an):
            return False
        else:
            return True


    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = {}
        queue = []
        queue.append([])

        len_in = len(nums)

        while(len(queue)):
            an = queue.pop(0)
            st = hash(tuple(set(an)))
            if len(ans) <=0:
                ans[st] = an
            elif st not in ans:
                ans[st] = an

            if len(an) <= len_in-1:
                temp = an.copy()
                for i in nums:
                    temp.append(i)
                    queue.append(temp.copy())
                    temp.pop(-1)

        return ans.values()
