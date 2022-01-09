

"""
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

"""

"""
conversion is similiar to decimal but here unit is 26

A = 1
Z = 26

AB =   1*26 + 2*1 = 28

ZY =  26* 26 + 25* 1 = 701

CDA = 3*(26*26) + 4 * (26) + 1 * (1) = 2133

"""





class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        col_dict = {}
        cnt = 1
        for i in range(65, 91):
            col_dict[chr(i)] = cnt
            cnt = cnt+1

        if len(columnTitle) > 1:
            result = 0
            cnt = 1
            for i in range(len(columnTitle)-2, -1, -1):
                num_mul = 26 ** cnt
                result = result + (col_dict[columnTitle[i]] * num_mul)
                cnt = cnt + 1

            result = result + col_dict[columnTitle[-1]]

            return result

        return col_dict[columnTitle]
