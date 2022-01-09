"""
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""

"""
    in intially
    for 1 step we can go one way
    for 2 step we can go in 2 way

    so using dynamic programing
    initial = for i 0 1 = its 1
    substurctue is dp[i] = sum of last 2 solution




"""



class Solution:

    def stairs(self, n, step, count):

        if step == n:
            count = count+1
            return count

        if step > n :
            return 0


        return self.stairs(n, step+1, count) + self.stairs(n, step+2, count)


    def climbStairs(self, n: int) -> int:

        # recursive
        #return self.stairs(n, 0, 0)


        #memozation

#         num_1 = 1
#         num_2 = 1
#         ans = 1
#         for i in range(1, n):
#             ans = num_1 +num_2
#             num_1 = num_2
#             num_2 = ans

#         return ans

        #dynamic progamming

        dp = [0] * (n+1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):

            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]



