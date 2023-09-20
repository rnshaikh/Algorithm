"""
Given a string s containing 0's and 1's. You have to return a smallest positive integer C, 
such that the binary string can be cut into C pieces and each piece should be of the power of 5  
with no leading zeros.

"""

"""
        same as longest increasing subsequence.

"""


def ispower(self, n):
        if (n < 125):
            return (n == 1 or n == 5 or n == 25)
        if (n % 125 != 0):
            return 0
        else:
            return self.ispower(n // 125)


    # Function to return the decimal
    # value of binary equivalent
    def number(self, s, i, j):
        ans = 0
        for x in range( i, j) :
            ans = ans * 2 + (ord(s[x]) - ord('0'))
        return ans

    # Function to return the minimum cuts required
    def cuts(self, s):
        n = len(s)
        # Allocating memory for dp[] array
        dp=[n+1 for i in range(n+1)]
        dp[0] = 0;

        # From length 1 to n
        for i in range(1, n+1) :

            # If previous character is '0' then ignore
            # to avoid number with leading 0s.
            if (s[i - 1] == '0'):
                continue
            for j in range(i) :

                # Ignore s[j] = '0' starting numbers
                if (s[j] == '0'):
                    continue

                # Number formed from s[j....i]
                num =self.number(s, j, i)
                print("num", num)
                # Check for power of 5
                if (not self.ispower(num)):
                    continue
                print("power true", num)
                # Assigning min value to get min cut possible
                dp[i] = min(dp[i], dp[j] + 1)

        # (n + 1) to check if all the strings are traversed
        # and no divisible by 5 is obtained like 000000
        if dp[n] < n + 1:
            return dp[n]
        else:
            return  -1
