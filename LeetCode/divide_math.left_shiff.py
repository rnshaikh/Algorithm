"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
"""


"""

    alogrithm left shift
    dividend = 10  divisor = 3

    subtracting divisor by dividend and incrment count by 1 until dividend is >= 0

    same thing is done by left shift operator count is increment by 1 << count



"""




class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        sign = True

        if (dividend >= 0) == (divisor >= 0):
            sign = True
        else:
            sign = False


        result = 0;

        dividend = abs(dividend)
        divisor = abs(divisor)
        while(dividend - divisor) >= 0 :
            count = 0
            while(dividend - (divisor << 1 << count) >= 0):
                count = count + 1

            result = result + (1 << count)
            dividend = dividend - (divisor << count)

        if sign:
            return result
        else:
            return result * -1

