
"""
Method 1 :
    if n=1 return 1

    traverse array from left to right
    find sum of left and right array if it equal just return position
    retrun -1

"""

class Solution:
    # Complete this function

    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here

        if N == 1:
            return 1

        for i in range(0, N):

            left_arr = A[i+1:]
            right_arr = A[:i]

            left_sum = sum(left_arr)
            right_sum = sum(right_arr)

            if left_sum == right_sum:
                return i+1

        return -1


"""

    method 2 efficient:

    right_sum = sum of all element:
    left_sum = 0

    traverse array from left to right

        subtract current ele from right sum

        check if right_sum == left_sum return i+!

        add current ele in left_sum


"""



class Solution:
    # Complete this function

    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here

        if N == 1:
            return 1

        right_sum = sum(A)
        left_sum = 0

        for i in range(0, N):

            right_sum = right_sum - A[i]

            if right_sum == left_sum:
                return i+1

            left_sum = left_sum + A[i]
