"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

"""


"""

    rotate from bottom r to top r , bottom l to bottom r, top r to bottom l , top l to top r


    rotate layer-by-layer, use that it's a square as advantage, 
    rotate positions in reverse order, store a in temp, a = b, b = c, c = d, d = temp;



"""




class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        l = 0
        r = len(matrix)-1

        while(l < r):
            for i in range(r-l):

                top = l
                bottom = r

                top_left = matrix[top][l+i]

                matrix[top][l+i] = matrix[bottom-i][l]
                matrix[bottom-i][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = top_left

            l = l+1
            r = r-1
