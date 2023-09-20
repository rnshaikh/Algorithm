
"""
    find sqrt of x
"""

"""
    binary search:

    left 1 to x

    if x < 2 : return x

    mid = left+right//2

    if mid * mid == x:
        return mid

    if mid squre is greater:
        right = mid

    if mid squre is less
        left = mid + 1


    we dont find any such number
    retrun left-1



"""



class Solution:
    def mySqrt(self, x: int) -> int:


        left = 1
        right = x

        if x < 2:
            return x

        while(left < right):

            mid = (left + right) // 2

            if (mid*mid) == x:
                return mid

            elif (mid*mid) > x:
                right = mid
            elif (mid*mid) < x:
                left = mid+1
        
        return left-1
