"""

A number n can be broken into three parts n/2, n/3 and n/4 (consider only integer part). 
Each number obtained in this process can be divided further recursively. 
Find the maximum sum that can be obtained by summing up the divided parts together.
Note: The maximum sum may be obtained without dividing n also.


"""

"""
    algorithm :

        if we use recuresive solution it will gow from n to 0 and find out first maximum sum of (0) then 1 then 2 and so on until n
        then check if sum is greater than n if yes return sum else return  n

        there is overlapping sub problem beacuse at some point n/2 or n/3 can same so maximum some of that num can be solved more than 1
        so we used dp with bottom up approach

        tak dp with n+1
        where each i store maxmium sum of (i/2 + i/3 + i/4 , i
        at 0 position maximum sum of (i/2, 0/3 0/4) will be store

        so if we get num like 24 then maxmim sum can be found by max(24, dp[24/2]+dp[24/3]+dp[24/4])
        beacuse we store maximum sum of 12, 8, 6 in our array so we dont calulate again and again in case of recusion

"""












class Solution:

    def recur(self, n):

        if n<=0:
            return 0

        sum_x = self.recur(int(n/2)) + self.recur(int(n/3)) + self.recur(int(n/4))

        if n <= sum_x:
            return sum_x
        else:
            return n

    def maxSum(self, n):
        # code here
        #return self.recur(n)

        dp = [0  for i in range(n+1)]
        print("before dp", dp)
        for i in range(1, n+1):

            dp[i] = max(i, dp[int(i/2)]+dp[int(i/3)]+dp[int(i/4)])

        print("dp", dp)
        return dp[n]
