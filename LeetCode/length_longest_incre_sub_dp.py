
"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
"""



"""
    dynamic progaming:

    initailly LIS at every index is 1
    take max_length = -inf

    start from last element to 0:

        for j fron i+1, last:
            if i < j
                stored it in max varaible =  1+LIS(j)  if 1+LIS(j) > max_1

        do this for element comes after i

        dp[i] = max(i. max_1)
        if max_length < dp[i]:
            update max-lenth = dp[i]



    for ex.
    [1, 2, 4, 3]

    start from last index
    LIS[3] = max(1, 1+LIS[4]) as 4 doesnot exist LIS[3]=1
    LIS[2] = max(1, 1+LIS[3]) only if [3] > [2] as 3 is not greater than 4 LIS[2] = 1
    LIS[1] = max(1, 1+LIS[2], 1+LIS[3])  = max(1, 2, 2) = 2
    LIST[0] = max(1, 1+LIST[1], 1+LIS[2], 1+LIS[3])  = max(1, 3, 2, 2) = 3

    result will be 3


"""







class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1 for _ in range(len(nums))]

        max_length = float("-inf")


        for i in range(len(nums)-1, -1, -1):
            if i < len(nums)-1:
                max_1 = -1
                for j in range(i+1, len(nums)):
                    if nums[j] > nums[i]:
                        if max_1 < 1+dp[j]:
                            max_1 = 1+dp[j]
                dp[i] = max(1, max_1)
                if max_length < dp[i]:
                    max_length = dp[i]

        if max_length > -1:
            return max_length
        return 1
