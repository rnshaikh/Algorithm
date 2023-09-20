

"""
Reverse bits of a given 32 bits unsigned integer.

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)

"""

"""
    start 1 bit put that to 32 bit in res
    to take i bit from input we have shift input right by 1 and logical and with 1
    to store given bit in result from 31 to 0 we have to logical or res with bit left shift by 31-i

"""


class Solution:
    def reverseBits(self, n: int) -> int:

        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit <<(31-i))

        return res
