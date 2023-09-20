"""
Given a positive integer N, count 
all possible distinct binary strings 
of length N such that there are no consecutive 1’s. 
Output your answer modulo 10^9 + 7.

"""

"""
    fibionacci series

"""








count = 0
class Solution:

    def recur(self, st, n):
        global count
        if n==0:
            count = count+1

            return
        else:

            if st[-1] == '1':
                self.recur(st+'0', n-1)
            else:
                self.recur(st+'0', n-1)
                self.recur(st+'1', n-1)


    def countStrings(self,n):
        # code here
    #   global count
    #   self.recur('0', n-1)
    #   self.recur('1', n-1)

    #   return count % ((10**9)+7)

        mod = ((10**9)+7)
        dp = [-1  for _ in range(n+1)]

        for i in range(0, n+1):
            if i == 0:
                dp[i] = 0
            elif i == 1:
                dp[i] = 2
            elif i == 2:
                dp[i] = 3
            else:
                dp[i] = (dp[i-1] + dp[i-2]) % mod

        return dp[n]
