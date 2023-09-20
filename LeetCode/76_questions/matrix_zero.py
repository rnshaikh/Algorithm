




class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_col = False
        zero_row = False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] == 0:
                    if i==0 and j == 0:
                        zero_col = True
                        zero_row = True

                    else:
                        if i == 0:
                            zero_row = True
                        matrix[i][0] = 0
                        if j == 0:
                            zero_col = True

                        matrix[0][j] = 0

        for i in range(1, len(matrix)):
            j = 1
            if matrix[i][0] == 0:
                while j < len(matrix[0]):
                    matrix[i][j] = 0
                    j = j+1

        for j in range(len(matrix[0])):
            i = 0
            if matrix[0][j] == 0:
                if j == 0 and not zero_col:
                    continue
                while i < len(matrix):
                    matrix[i][j] = 0
                    i = i+1

        if zero_row:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
