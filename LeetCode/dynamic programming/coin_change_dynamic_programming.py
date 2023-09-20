"""

You are given an integer array coins representing coins of different denominations and an integer 
amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

"""


"""

    in dp programming we are gonna take array[amount+1] with inital vvalue 99999

    we are going to use bottom-up approach start from 0 amount how many min coin required
    dp[0] = 0

    for i amount  how many min coin required

        for j in coins: take every coin

            if i-j >= 0
                dp[i] = min(dp[i], 1+dp[i-j])  current coin +  dp[amount-current_coin]
                i = 4 j = 3
                ex. 1 + dp[4-3]  = 1+dp[1]

    return dp[amount]
"""



class Solution:

    def recur(self, coins, curr_amount, amount, count, result):

        if curr_amount > amount:
            return

        if curr_amount == amount:
            if result[0] > count:
                result[0] = count
            return

        for i in coins:
            print("curr_amount, amount, count, coin", curr_amount, amount, count, i)
            self.recur(coins, curr_amount+i, amount, count+1, result)



    def coinChange(self, coins: List[int], amount: int) -> int:

#         result = [999999999]

#         if amount == 0:
#             return 0

#         for i in coins:
#             self.recur(coins, i, amount, 1, result)

#         if result[0] == 999999999:
#             return -1
#         return result[0]

        dp = [(amount+1) for _ in range(amount+1)]
        dp[0] = 0

        for i in range(1, amount+1):
            for j in coins:
                if i - j >= 0 :
                    dp[i] = min(dp[i], 1+dp[i-j])


        if dp[amount] != (amount)+1:
            return dp[amount]
        else:
            return -1


