"""

You are given an integer array nums. You are initially positioned at the array's first index, and 
each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

"""


"""
dp
minJumps(start, end) = Min ( minJumps(k, end) ) for all k reachable from start

Algorithm:

    Create a dp[] array of size N, where N is the size of the given array.
    Initialise all the elements of the array to INT_MAX.
    Initialise dp[0] = 0, since, we are standing at the first index and we need no jumps to reach the last element.
    The recursive structure would be:
    dp[i] = 1 + min(dp[i], 1 + min( dp[i+1], dp[i+2],. . . dp[i + dp[i] + 1]))
    Iterate a loop from 0 till N – 1. Run a nested loop from i + 1 till min(i + arr[i] + 1, n) and find the minimum of jumps[i] and i + jumps[i].
    After iterations, return the value of dp[N – 1]



    int dp[n] = {INT_MAX}
    dp[0] = 0
    for(i = 0 to i < n){
        for(j = i+1 to j < min(i+num[i]+1, n)) {
            dp[j] = min(dp[j], 1 + dp[i])
        }
    }
    return dp[n-1]
"""




#greedy:
"""
    start from 2nd last check if we reach to end_pos if yes then update end_pos = i

    if end_pos = 0: return True else false
"""

def canJump(self, nums: List[int]) -> bool:
        end_pos = len(nums)-1

        for i in range(len(nums)-2, -1, -1):

            if i+nums[i] >= end_pos:
                end_pos = i

        if end_pos==0:
            return True
        else:
            return False



class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_reach = 0

        for i in range(len(nums)):

            if i <= max_reach:
                max_reach = max(i+nums[i], max_reach)

            else:
                return False
        return True




# to calculate min number of jumps that we can tak to reach last index

"""
    we can do this usin bfs.

    for first will check what is fathest we can go that will be our level
    so start from l=0 r =0 res = 0 at level 0

    we will traverse until r < len(nums)-1
        farthest = 0 for updating r of next level
        loop througn l to r+1
            farthest = max(farthest, i+nums[l])


        l = r+1
        r = farthest
        res = res+1

    return res

"""





class Solution:
    def jump(self, nums: List[int]) -> int:

        l = 0
        r = 0
        res = 0


        while r < len(nums)-1:

            farthest = 0

            for i in range(l, r+1):
                farthest = max(farthest, i+nums[i])


            if farthest == 0:
                return -1
                
            l = r+1
            r = farthest
            res = res+1

        return res












