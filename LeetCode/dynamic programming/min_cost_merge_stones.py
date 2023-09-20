"""
There are n piles of stones arranged in a row. The ith pile has stones[i] stones.

A move consists of merging exactly k consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these k piles.

Return the minimum cost to merge all piles of stones into one pile. If it is impossible, return -1.

"""


"""
    this dp hard problem:
    here we are going go consider first 1 element in arr then 2 element and so on

    for all element less than k-1 dp[x][y] will be zero bc there is no sufficient element

    first we going find cumm sum of element
        sum_num [i+1] = sum[i] + stones[i]

        so then if we want sum of element from x to y we can get it by sum_num[y+!] - sum_num[x]


    so there are 3 loop
        first loop control then no element in sub problem we are starting from k-1 to n
            2n loop in x from 0 to n
                3rd loop is y = x+l to n:
                    if lenth is equal to k-1 then we just sum arr from x to y
                        dp[x][y] = sum(arr[x to y])
                    else:
                        we hae to divide arr in mid and mid is increment by k-1 from x to y
                        dp[x][y] = min(dp[x][y], dp[x][mid] + dp[mid+1][y])


                        here after merge there can k-1 element so we have to sum of that k-1 element also
                        if l % (k-1) == 0
                            dp[x][y] = dp[x][y]+sum(arr[xtoy])

    return dp[0][n-1]



"""


class Solution:

    def mergeStones(self, stones: List[int], k: int) -> int:

        n = len(stones)

        if (n-k) % (k-1) != 0:
            return -1
            
        sum_num = [0] * (n+1)

        for i in range(0, n):
            sum_num[i+1] = sum_num[i] + stones[i]

        #print("sum_num", sum_num)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for l in range(k-1, n):
            for x in range(0, n):
                for y in range(x+l, n):
                    if(l == k-1):
                        dp[x][y] = (sum_num[y+1] - sum_num[x])
                    else:
                        dp[x][y] = 9999999999999
                        for mid in range(x,y,k-1):
                            dp[x][y] = min(dp[x][y], (dp[x][mid] + dp[mid+1][y]))

                        #print("x, y, dp[x][y]", x,y,dp[x][y])
                        if l % (k-1) == 0:
                            #print("in addition x, y, dp[x][y]", x, y, dp[x][y])
                            dp[x][y] = dp[x][y] + (sum_num[y+1] - sum_num[x])

        #print("dp", dp)
        return dp[0][n-1]




