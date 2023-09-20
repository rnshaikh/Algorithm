"""

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""

"""
shrinking window, left/right initially at endpoints, shift the pointer with min height;

"""


class Solution:
    def maxArea(self, height: List[int]) -> int:


        max_w = -1

        l = 0
        r = len(height)-1

        while l < r:


            x = r-l
            min_l_r = min(height[l], height[r])
            water = x*min_l_r

            if water> max_w:
                max_w = water

            if height[l] < height[r]:
                l =l+1
            elif height[l] > height[r]:
                r = r-1
            else:
                l = l+1


        return max_w


