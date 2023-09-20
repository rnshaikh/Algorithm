"""
You are given N identical eggs and you have access to a K-floored building from 1 to K.

There exists a floor f where 0 <= f <= K such that any egg dropped at a floor higher than f will break, 
and any egg dropped at or below floor f will not break. 
There are few rules given below.

An egg that survives a fall can be used again.
A broken egg must be discarded.
The effect of a fall is the same for all eggs.
If the egg doesn't break at a certain floor, it will not break at any floor below.
If the eggs breaks at a certain floor, it will break at any floor above.
Return the minimum number of moves that you need to determine with certainty what the value of f is.

For more description on this problem see


"""

"""
    algorithm:

    in recurisve solution there 3 cases

    for 1 egg k floor there will be  k trial
    for n egg 0 floor 0 trial and for n egg 1 floor 1 trial

    for any x floor there are 2 case if egg break or not
        if egg break than floor above x egg will break for them
        so condition will be n-1, x-1 floor will remain

        if egg does not broke then condition will be m, k-x floor will remain


    so we can solved this using dp

    tak dp with col as floor k+1 row as egg n+1

    for 0 egg all column will be 0
    for 1 egg columns value will be its number i

    for 0 or 1 column for all row value will be 0 or 1

    traverse through n+1 egg
        traverse through k+1 floor:

            max_moves = max_number
            for x in 1, j+1 floor
                                egg break     egg does not break
                res = 1 + max(dp[i-1][x-1], dp[i][j-x])
                if res < max_moves:
                    max_moves = res

            dp[i][j] = max_moves



"""




class Solution:

    #Function to find minimum number of attempts needed in
    #order to find the critical floor.

    # def recur(self, n, k):

    #     if n == 1 :
    #         return k

    #     if k==0 or k==1:
    #         return k



    #     moves = 99999999999
    #     res = 0

    #     for i in range(1, k+1):

    #         res = max(self.recur(n-1, i-1), self.recur(n,k-i))

    #         if res < moves:
    #             moves = res

    #     return moves+1


    def eggDrop(self,n, k):
        # code here

        # moves = self.recur(n, k)

        # return moves


        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

        for i in range(k+1):
            dp[1][i] = i

        #print("dp for 1 egg k floor", dp)
        for i in range(n+1):

            dp[i][0] = 0
            dp[i][1] = 1

        #print("dp for n egg and 0 and 1 floor", dp)

        for i in range(2, n+1):
            for j in range(2, k+1):
                min_moves = 99999999999999999
                for x in range(1, j+1):
                              #egg is broken,  egg is not broken
                    res = 1 + max(dp[i-1][x-1], dp[i][j-x])
                    if res < min_moves:
                        min_moves = res

                dp[i][j] = min_moves


        #print("dp", dp)
        return dp[n][k]
