"""

Given an integer N denoting the Length of a line segment. 
You need to cut the line segment in such a way that the cut length of a line segment each time is 
either x , y or z. Here x, y, and z are integers.
After performing all the cut operations, your total number of cut segments must be maximum.


"""

""""
    same as coin change problem istead of finding minimum here we find maximum
"""






class Solution:

    #Function to find the maximum number of cuts.
    def recur(self, n, x, y, z):


        if n<=0:
            return 0
        a1, a2, a3 = float('-inf'), float('-inf'), float('-inf')
        if n >= x:
            a1 = self.recur(n-x, x, y, z)

        if n >= y:
            a2 = self.recur(n-y, x, y, z)

        if n >= z:
            a3 = self.recur(n-z, x, y, z)


        #print("a1, a2, a3", a1, a2, a3)
        return 1 + max(a1, a2, a3)

        #return max(x_cut, y_cut, z_cut)

        # return max(self.recur(n-x, cut+1, x, y, z),
        #           self.recur(n-y, cut+1, x, y, z), self.recur(n-z,cut+1, x, y, z))


    def maximizeTheCuts(self,n,x,y,z):
        #code here

        dp = [float('-inf') for _ in range(n+1)]
        dp[0] = 0

        cuts = [x,y,z]

        for i in range(1, n+1):

            for j in cuts:
                if i-j>=0:
                    dp[i] = max(dp[i], 1+dp[i-j])


        if dp[n] <= 0:
            return 0
        return dp[n]
