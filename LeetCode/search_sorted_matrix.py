"""
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

"""


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix)-1
        i = 0
        j = len(matrix[0])-1


        while i <= n and j >= 0:

            if matrix[i][j] == target:
                return True

            if matrix[i][j] < target:
                i = i+1

            else:
                j = j-1

        return False
