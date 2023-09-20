"""

Given an array nums[] of size n, where nums[i] denotes the number of characters in one word. 
Let K be the limit on the number of characters that can be put in one line (line width).
Put line breaks in the given sequence such that the lines are printed neatly.
Assume that the length of each word is smaller than the line width.
When line breaks are inserted there is a possibility that extra spaces are present in each line.
The extra spaces include spaces put at the end of every line except the last one.

You have to minimize the following total cost where total cost = Sum of cost of all lines, where cost of line is = (Number of extra spaces in the line)2.

"""


"""
Algorithm:

    it top down approach:

        initalized dp with n length of -1
        call solve with 0word , nums array, k, n

        solve func:

        if i == n last word:
            return 0

        if dp[i] != -1: if ith word is already calculatd
            return dp[i]

        intialize mn = 9999999999999, sum_a = 0, j=i

        traverse j from i to n

            if sum_a+nums[j]+(j-i) > k that mean current word length and space between word is greater than k:
                break
            if j == n-1: if it last line cost will be 0
                mn = 0

            sum_a = sum_a + nums[j]
                            calculate (k - current_sum - j - i)^2  + call j+1, nums, k, n
            mn = min(mn, ((k-sum_a-(j-i))) ** 2  +  self.solve(j+1, nums,k,n))


        dp[i] = mn
        return mn
"""



dp = []
class Solution:

    def solve(self,i, nums, k, n):

        global dp
        
        if i == n:
            return 0

        if dp[i] != -1:
            return dp[i]

        mn = 999999999999999
        sum_a = 0
        j = i
        for j in range(i, n):
            print("j ", j)
            if sum_a+nums[j]+(j-i)>k:
                break
            if j == n-1:
                mn = 0
            sum_a = sum_a+nums[j]
            mn = min(mn, ((k-sum_a-(j-i)) ** 2) + self.solve(j+1, nums, k, n))

        dp[i] = mn
        return dp[i]

    def solveWordWrap(self, nums, k):
        #Code here
        global dp
        n = len(nums)
        dp = [-1 for _ in range(n)]

        return self.solve(0, nums, k, n)




sol = Solution()
nums = [3,2,2,5]
k = 6
print("cost: ", sol.solveWordWrap(nums, k))
print("nums:", nums)
print("dp:", dp)
