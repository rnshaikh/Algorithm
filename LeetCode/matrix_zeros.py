"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col_zero = []
        row_zero = []
        for li in matrix:
            for j in range(0, len(li)):
                if li[j] == 0:
                    col_zero.append(j)
                    row_zero.append(matrix.index(li))


        for row_col in row_zero:
            j = 0
            while j < len(matrix[0]) and row_col < len(matrix):
                matrix[row_col][j] = 0
                j = j+1

        for row_col in col_zero:
            j = 0
            while j <len(matrix) and row_col < len(matrix[0]):
                matrix[j][row_col] = 0
                j = j+1

        return matrix
