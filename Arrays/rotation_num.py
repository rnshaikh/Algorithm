# Rotation

"""
    Given an ascending sorted rotated array Arr of distinct integers of size N. The array is right rotated K times. Find the value of K.

    Method:
        1) Find maximum num .
        2) find its index
        3) if index+1 == n then return 0 rotation
        4) else return index+1 rotation
"""


#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        # code here
        max_num=0

        for i in arr:
            if i > max_num :
                max_num = i


        index = arr.index(max_num)

        if index+1 == n:
            return 0
        else:
            return index+1

