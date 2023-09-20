"""
A top secret message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
You are an FBI agent. You have to determine the total number of ways that message can be decoded, as the answer can be large return the answer modulo 109 + 7.
Note: An empty digit sequence is considered to have one decoding. It may be assumed that the input contains valid digits from 0 to 9 and If there are leading 0’s, extra trailing 0’s and two or more consecutive 0’s then it is an invalid string.
"""


"""
    we can solve thi problem by dynamic programming

    take list dp[1] of n+1

    if str == '0' retrun 0

    if len(str) <= 1 return 1

    if prefix of str is 0 or there is 2 adjacent '00' in str:
        return 0


    travese from 2 char to last char:

        take last 2 char in str

        if d1 > 0 and d2>0 :
            id d1d2 < 27:
                dp[i] = dp[i-1] + dp[i-2]

            else:
                dp[i] =dp[i-1]
        else:
            one of d1 d2 is zero
            if d1==0:
                dp[i] = dp[i-1]
            else:
                id d1>2: then we cant encode:
                    return 0
                else:
                    dp[i] = dp[i-2]

    return dp[n] % 10^9+7


"""



class Solution:
    def CountWays(self, str):
        # Code here
        n = len(str)
        if str == '0':
            return 0

        if n <=1:
            return 1

        if str[0]=='0' or '00' in str:
            return 0

        dp = [1 for _ in range(n+1)]

        for i in range(2, n+1):

            d1, d2 = int(str[i-2]), int(str[i-1])

            if d1 > 0 and d2>0:

                if d1*10+d2 < 27:
                    dp[i] = dp[i-1] + dp[i-2]

                else:
                    dp[i] = dp[i-1]

            else:

                if d1==0:
                    dp[i] = dp[i-1]

                else:
                    if d1>2:
                        return 0
                    else:
                        dp[i] = dp[i-2]

        return dp[-1] % ((10**9)+7)
