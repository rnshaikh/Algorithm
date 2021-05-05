#Smallest subarray with sum greater than x

"""
    Given an array of integers (A[])  and a number x, find the smallest subarray with sum greater than the given value.
    Note: The answer always exists. It is guaranteed that x doesn't exceed the summation of a[i] (from 1 to N).
"""


"""
    method 1:

    1) intialize curr_sum = 0 and min_len = n+1 ; start= 0 , end=0

    2) while end is less than n

    3) add element in curr_sum and increment end by 1 until end less than n

    4) if current sum get greater than x then

    5) remove element from curr_sum and increment start by 1 and update min_len = end-start

    6) return min_len

"""


class Solution:
    def sb(self, arr, n, x):
        # Your code goes here

        # Initialize current sum and minimum length
        curr_sum = 0
        min_len = n + 1

        # Initialize starting and ending indexes
        start = 0
        end = 0
        while (end < n):

            # Keep adding array elements while current
            # sum is smaller than or equal to x
            while (curr_sum <= x and end < n):
                curr_sum += arr[end]
                end += 1

            # If current sum becomes greater than x.
            while (curr_sum > x and start < n):

                # Update minimum length if needed
                if (end - start < min_len):
                    min_len = end - start

                # remove starting elements
                curr_sum -= arr[start]
                start += 1

        return min_len

