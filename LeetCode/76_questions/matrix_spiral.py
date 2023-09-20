"""
Given an m x n matrix, return all elements of the matrix in spiral order.

"""

"""

keep track of visited cells through left, right, top, bottom boundry; keep track of boundaries, layer-by-layer;

"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        ans = []
        while left < right and top < bottom:

            for i in range(left, right):
                ans.append(matrix[top][i])

            top = top+1

            for i in range(top, bottom):
                ans.append(matrix[i][right-1])

            right = right-1

            if not (left<right and top<bottom):
                break

            for i in range(right-1, left-1, -1):
                ans.append(matrix[bottom-1][i])

            bottom = bottom-1

            for i in range(bottom-1, top-1, -1):
                ans.append(matrix[i][left])

            left = left+1

        return ans

