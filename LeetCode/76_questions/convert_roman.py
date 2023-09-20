class Solution:
    def convertRoman(self, n):
        #Code here
        
        nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        romans = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        
        nums = nums[::-1]
        romans = romans[::-1]
    
        ans = ""
        
        for i in range(len(nums)):
            
            if n:
                while n >= nums[i]:
                    
                    qu = n // nums[i]
                    rem = n % nums[i]
                    ans = ans + romans[i] * qu
                    n = rem
        
        return ans

"""
693. Binary Number with Alternating Bits
"""

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:


        if n == 1:
            return True
        while n > 0:

            prev = n & 1
            n = n >> 1
            curr = n & 1

            if curr == prev:
                return False
        return True