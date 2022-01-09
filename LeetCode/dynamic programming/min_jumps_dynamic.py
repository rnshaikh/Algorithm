"""

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

"""




class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_reach = 0

        for i in range(len(nums)):

            if i <= max_reach:
                max_reach = max(i+nums[i], max_reach)

            else:
                return False
        return True




class Solution:

    def min_jumps(self, nums, l, h):
        if l == h:
            return 0

        if nums[l] == 0:
            return 999

        min = 999
        for i in range(l+1, h+1):
            if i < l+nums[l]+1:
                print("calculating jumps from i to h", i, h)
                jumps = self.min_jumps(nums, i, h)
                if jumps != 999 and jumps+1 < min:
                    min = jumps+1
                print("jumps from i h,cost, min ",i, h, jumps, min)

        return min

    def canJump(self, nums: List[int]) -> bool:
        min_st = self.min_jumps(nums, 0, len(nums)-1)
        if min_st != 999 or min_st!=0:
            return True
        else:
            return False



set B[i] to infinity for all i
B[1] = 0;                    <-- zero steps to reach B[1]
for i = 1 to n-1             <-- Each step updates possible jumps from A[i]
    for j = 1 to A[i]        <-- Possible jump sizes are 1, 2, ..., A[i]
        if i+j > n           <-- Array boundary check
            break
        if B[i+j] > B[i]+1   <-- If this path to B[i+j] was shorter than previous
            B[i+j] = B[i]+1  <-- Keep the shortest path value
            C[i+j] = i       <-- Keep the path itself
