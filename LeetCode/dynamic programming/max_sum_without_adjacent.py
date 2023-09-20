"""
Given an array Arr of size N containing positive integers. 
Find the maximum sum of a subsequence such that no two numbers in the 
sequence should be adjacent in the array.

"""

"""
    for 1 element max sum is that element

    for 2 element max sum max of them

    for 3 element maxof(last_ans, current_elem + curr-2)


    so there 2 case:
        arr[i] = max(arr[i-1], arr[i]+arr[i-2])

"""


class Solution:

    def findMaxSum(self,arr, n):
        # code here


        for i in range(1, n):

            if i-2 >= 0:
                curr = arr[i] + arr[i-2]
            else:
                curr = arr[i]

            arr[i] = max(arr[i-1], curr)

        return arr[n-1]
