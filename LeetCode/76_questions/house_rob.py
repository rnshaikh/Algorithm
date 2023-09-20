"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

"""

"""
    dynamic progrming
    initialize dp[0] = with nums[0]

    traverse from 1 to last
        i-2 > =0
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        else:
            dp[i]  = max(dp[i-1], mums[i])

    return dp[n-1]


"""


class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [0 for _ in range(len(nums))]

        dp[0] = nums[0]


        for i in range(1, len(nums)):

            if i-2>=0:
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])

            else:
                dp[i] = max(dp[i-1], nums[i])

        #print("dp", dp)
        return dp[len(nums)-1]





"""
    Houser robber 2 with circular

    use 1 for 1 to last element
    use 1 for 0 to 2nd last element

    return max(1stele, 1, 2)

"""

class Solution:

    def helper(self, nums):


        n = len(nums)

        if n <=0:
            return 0

        dp = [0 for _ in range(n)]
        dp[0] = nums[0]

        for i in range(1, n):
            if i-2 >= 0:
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            else:
                dp[i] = max(dp[i-1], nums[i])

        return dp[n-1]




    def rob(self, nums: List[int]) -> int:

        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
