"""
    Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

"""

"""
    kadane algorithms:

        1) kadane algorithm traverse through array store 2 thing one sum of element traversed and max_sum so far
        if sum of element become less than 0 then its againe start with 0

        if sum_ofelement is greater than max_sum update max_sum

"""




class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here

        max_end_here = 0
        max_sum = arr[0]

        for i in range(N):

            max_end_here = max_end_here + arr[i]

            if max_end_here > max_sum:
                max_sum = max_end_here

            if max_end_here < 0:
                max_end_here = 0


        return max_sum
