"""
Swapping pairs make sum equal

Given two arrays of integers A[] and B[] of size N and M, the task is to check if a pair of values (one value from each array) exists such that swapping the elements of the pair will make the sum of two arrays equal.
"""

"""
    method : 1

    1) sort array a,b
    2) calculate sum of a and b in sum_b and sum_b
    3) initialize i=0, j=0 , min_sum=-999999
    4) iterate i through n j through m
    5) calculate temp1 by subtracting current elemetn from a and adding current element from b
    6) calculate temp2 by subtracting current element from b and adding current element from a
    7) check if temp1 == temp2 return 1
    8) if (temp1-temp2) is greater than min_sum then update min_sum = temp1-temp2 and increment j by 1
    9) else min_sum = -999999 and increment by i by 1 and j=0
    10) if not retrun -1

"""




class Solution:

    def findSwapValues(self,a, n, b, m):
        # Your code goes here

        a.sort()
        b.sort()

        sum_a = sum(a)
        sum_b = sum(b)

        i = 0
        j = 0
        min_sum = -9999999


        while(i < n and j < m):

            temp1 = sum_a - a[i] + b[j]
            temp2 = sum_b - b[j] + a[i]

            if temp1 == temp2:
                return 1

            if temp1-temp2> min_sum:
                min_sum = temp1-temp2
                j = j+1
            else:
                min_sum = -999999
                i = i+1
                j=0
        return -1
