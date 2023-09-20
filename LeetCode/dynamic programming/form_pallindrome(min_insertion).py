"""
Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
For Example:
ab: Number of insertions required is 1. bab or aba
aa: Number of insertions required is 0. aa
abcd: Number of insertions required is 3. dcbabcd


"""


"""
    Let the input string be str[l……h]. The problem can be broken down into three parts:

        Find the minimum number of insertions in the substring str[l+1,…….h].
        Find the minimum number of insertions in the substring str[l…….h-1].
        Find the minimum number of insertions in the substring str[l+1……h-1].
        Recursive Approach: The minimum number of insertions in the string str[l…..h] can be given as:

            minInsertions(str[l+1…..h-1]) if str[l] is equal to str[h]
            min(minInsertions(str[l…..h-1]), minInsertions(str[l+1…..h])) + 1 otherwise


here memorization technique is used to avoid similar subproblem recalls. 
We can create a table to store the results of subproblems so that 
they can be used directly if the same subproblem is encountered again.

The table should be filled in a diagonal fashion. For the string abcde, 0….4, 
the following should be ordered in which the table is filled:
"""



class Solution:

    def recur(self, s, l, h):

        if l == h:
            return 0

        if l > h:
            return 99999999

        if l == h-1:
            if l == h:
                return 0
            else:
                return 1

        if s[l] == s[h]:
            return self.recur(s, l+1, h-1)

        else:
            return min(1+self.recur(s, l+1, h), 1+self.recur(s, l, h-1))

    def findMinInsertions(self, S):
        # code here

        # return self.recur(S, 0, len(S)-1)

        n = len(S)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        gap = 0

        for gap in range(1, n):
            l = 0
            for h in range(gap, n):

                if S[l] == S[h]:
                    dp[l][h] = dp[l+1][h-1]

                else:
                    dp[l][h] = min(dp[l+1][h], dp[l][h-1]) + 1

                l = l+1

        return dp[0][n-1]
