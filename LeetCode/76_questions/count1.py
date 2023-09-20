
"""

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.


"""

"""
modulo, and dividing n; mod and div are expensive, to divide use bit shift, instead of mod to get 1's place use bitwise & 1;
"""



class Solution:
    def hammingWeight(self, n: int) -> int:
        
        res = 0

        while n:
            res= res + (n%2)
            n = n // 2
            
        return res


class Solution:
    def hammingWeight(self, n: int) -> int:
        
        res = 0

        while n:
            res= res + (n & 1)
            n = n >> 1
            
        return res



class Solution:
    def hammingWeight(self, n: int) -> int:

        res = 0

        while n:
            n = n & (n-1)
            res = res+1

        return res
