# Max sum path in two arrays

"""
Given two sorted arrays A and B of size M and N respectively. Each array contains only distinct elements but may have some elements in common with the other array. Find the maximum sum of a path from the beginning of any array to the end of any of the two arrays. We can switch from one array to another array only at the common elements.
Note: Only one repeated value is considered in the valid path sum.


"""


"""
Method :

    1) Initiate variable max_sum = 0, sum_a =0, sum_b = 0

    2) travers first array check if it comman in 2nd if common then add sum_a with sum of ele in 2nd array from common

    3) else add element in sum_a check if its max_sum and update max_sum

    4) traverse 2nd array check if is common in 1st array if common then add sum_b with sum of ele in 1st array from common

    5) else add eleemen in sum_b check if its max_sum and update max_sum

    6) return max_sum




"""




#Your task is to complete this function
#Function should return an integer denoting the required answer

class Solution:
    def maxSumPath(self, ar1, ar2, m, n):
        #code here

        result_arr = []
        sum_a = 0
        max_sum = 0

        for i in range(m):
            if arr1[i] in arr2:
                index = arr2.index(arr1[i])
                sum_arr = sum(arr2[index:])
                new_sum = sum_a+sum_arr
                # result_arr.append(new_sum)
                if new_sum > max_sum :
                    max_sum = new_sum


            sum_a = sum_a + arr1[i]

        # result_arr.append(sum_a)
        if sum_a > max_sum:
            max_sum = sum_a


        sum_b = 0
        for j in range(n):
            if arr2[j] in arr1:
                index = arr1.index(arr2[j])
                sum_arr2 = sum(arr1[index:])
                new_sum = sum_b + sum_arr2
                # result_arr.append(new_sum)
                if new_sum > max_sum:
                    max_sum = new_sum


            sum_b = sum_b + arr2[j]

        #result_arr.append(sum_b)
        if sum_b > max_sum:
            max_sum = sum_b

        # result_arr.sort()
        return max_sum
