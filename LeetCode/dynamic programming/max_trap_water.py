"""
Given an array arr[] of N non-negative integers representing the height of blocks. If width of each block is 1, 
compute how much water can be trapped between the blocks during the rainy season.

"""

"""
    algorithm:

        heere at current block how much water we can save is determined by  min(max height on left and max height on right) - current block height

        we have to calculate max_left on each position, max_right on each position , min_l_r at each position

        trap_water is calculated by current min_l_r - current height



"""







class Solution:
    def trappingWater(self, arr,n):
        #Code here

        max_left = [0 for _ in range(n)]
        max_right = [0 for _ in range(n)]
        min_l_r = [0 for _ in range(n)]

        max_left[0] = arr[0]
        max_right[-1] = arr[-1]

        min_l_r[0] = min(max_left[0], max_right[0])

        for i in range(1, n):

            if max_left[i-1] < arr[i]:
               max_left[i] = arr[i]
            else:
                max_left[i] = max_left[i-1]

        for j in range(n-2, -1, -1):
            if max_right[j+1] < arr[j]:
                max_right[j] = arr[j]
            else:
                max_right[j] = max_right[j+1]

        for i in range(n):
            min_l_r[i] = min(max_left[i], max_right[i])
        
        #print("max", max_left, max_right, min_l_r)
        trap_water = 0
        for i in range(n):

            water = min_l_r[i] - arr[i]

            if water>0:
                trap_water = trap_water + water

        return trap_water



"""
    we can solved this using 2 pointer
    take max_l , max_r, trap_water
    i = 0  j = n-1

    traverse until i<=j

    if max_l < = max_r:
        water = max_l - arr[i]
        add it in trap_water if non negative
        update max_l if less than curre
        i = i+1
    else:
        similiar for right
        j = j+1


"""




class Solution:
    def trappingWater(self, arr,n):
        #Code here



        max_l = arr[0]
        max_r = arr[-1]

        trap_water = 0

        i = 0
        j = n-1
        while(i <= j):

            if max_l <= max_r:
                water = max_l - arr[i]
                if water > 0:
                    trap_water = trap_water + water

                if max_l < arr[i]:
                    max_l = arr[i]
                i = i+1
            else:

                water = max_r - arr[j]

                if water > 0:
                    trap_water = trap_water + water

                if max_r < arr[j]:
                    max_r = arr[j]
                j = j-1

        return trap_water


class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height)-1
        res = 0
        
        while left < right:
            
            curr_level = min(height[left], height[right]) * (right-left)
            res = max(res, curr_level)
            
            if height[left] > height[right]:
                right = right-1
            
            else:
                left= left+1
        
        
        return res
            