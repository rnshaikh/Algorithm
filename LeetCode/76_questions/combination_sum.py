"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations 
of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations 
that sum up to target is less than 150 combinations for the given input.

"""


"""
    dfs with backtracking

    here two decision to make
    add i element in sum and result call with i itself

    undo pop curr element from result and sum if it unsuccess result is not added to ans if it is success result is added to ans

    call with i+1 element sum and result

    success
    if target == sum:
        add res into ans
        return

"""



class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:


        ans = []

        def dfs(curr, total, target, i):

            if total == target:
                ans.append(curr.copy())
                return

            if i >= len(candidates) or target < total:
                return


            curr.append(candidates[i])
            dfs(curr, total+candidates[i], target, i)
            curr.pop()
            dfs(curr, total, target, i+1)

        dfs([], 0, target, 0)

        return ans
