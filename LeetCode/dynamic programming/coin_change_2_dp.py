"""
    Given a value N, find the number of ways to make change for N cents, 
    if we have infinite supply of each of S = { S1, S2, .. , SM } valued coins.

    n = 4 , m = 3
    S[] = {1,2,3}
    Output: 4
        Explanation: Four Possible ways are:
        {1,1,1,1},{1,1,2},{2,2},{1,3}.
"""

"""
    Algorithm :

    in dp here we are going from bottom up from first coin and 1 amount to m coin and n amount

    take list to store no way to compute i amount size is amount+1

    dp[0] = 1 for base case

    outer loop changes from 0 to m coin:
        inner loop changes from 1 to amount+1 : amount

            if j-coint[i] >= 0  that mean coins value is greater than
                dp[j] = dp[j] + dp[j-coins[i]]
                dp[j] is store how many way current amount can be computed from previous coin
                d[j-coins[i]] is simply to say if get how many  way amount - coins can be computed

    dp[n]
"""







class Solution:
    def count(self, coin, m, n):
        # code here

        dp = [0 for _ in range(n+1)]

        dp[0] = 1

        for i in range(m):
            for j in range(1, n+1):
                if j - coin[i] >= 0:
                    dp[j] = dp[j] + dp[j-coin[i]]

        return dp[n]
