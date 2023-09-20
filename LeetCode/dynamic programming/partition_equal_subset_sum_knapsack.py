"""
Given a non-empty array nums containing only positive integers, 
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

"""


"""
    "Algortihm":

        first calculate total sum of list
        if sum is not divisible by 2 or odd then there is no subset with equal sum so return false
        else:
            half_sum = sum // 2

            not you have list of value and half_sum (capacity) to calculate which value equal to half_sum
            so this is knapsack problem.

            take dp with no_row equal to no_element+1 and col equal to hal_sum or capacity + 1

            traverse from 1 element to last_element:
                taverse from 0 to half_sum capacity:
                    two case if element present or not
                    element_not_present = values will be last value dp[i-1][w]
                    element_present = 0
                    if w-nums[i-1] >= 0 if current capacity constraint >=  current_element_capacity:
                        element_present = nums[i-1] + dp[i-1][w-nums[i-1]]

                    dp[i][w] = max(element_present, element_not_present)

        answer will stored in last value
        that dp[n][half_sum]

"""


class Solution:

    def knapsack(self, nums, n, half_sum):


        dp = [ [0  for _ in range(half_sum+1)] for _ in range(n+1)]


        for i in range(1, n+1):
            for w in range(0, half_sum+1):

                ele_not_present = dp[i-1][w]
                ele_present = 0

                if w - nums[i-1] >= 0:
                    ele_present = nums[i-1] + dp[i-1][w-nums[i-1]]

                dp[i][w] = max(ele_present, ele_not_present)


        return dp




    def canPartition(self, nums: List[int]) -> bool:

        total_sum = 0

        for i in nums:
            total_sum = total_sum + i

        if total_sum % 2 != 0:
            return False


        half_sum = total_sum // 2
        n = len(nums)
        dp = self.knapsack(nums, len(nums), half_sum)

        if dp[n][half_sum] == half_sum :
            return True
        else:
            return False
