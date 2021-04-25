# Find maximum possible stolen value from houses


"""
Create an extra space dp, DP array to store the sub-problems.
Tackle some basic cases, if the length of the array is 0, print 0, if the length of the array is 1, print the first element, if the length of the array is 2, print maximum of two elements.
Update dp[0] as array[0] and dp[1] as maximum of array[0] and array[1]
Traverse the array from the second element to the end of array.
For every index, update dp[i] as maximum of dp[i-2] + array[i] and dp[i-1], this step defines the two cases, if an element is selected then the previous element cannot be selected and if an element is not selected then the previous element can be selected.
Print the value dp[n-1]

"""


class Solution:

    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,hval, n):

        # code here

        if n == 0:
            return 0
        if n == 1:
            return hval[0]
        if n == 2:
            return max(hval[0], hval[1])

        # dp[i] represent the maximum value stolen so
        # for after reaching house i.
        dp = [0]*n

        # Initialize the dp[0] and dp[1]
        dp[0] = hval[0]
        dp[1] = max(hval[0], hval[1])

        # Fill remaining positions
        for i in range(2, n):
            dp[i] = max(hval[i]+dp[i-2], dp[i-1])

        return dp[-1]

