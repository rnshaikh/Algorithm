"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""


"""
    divide and conquer:

    if x == 0: return 0
    if y == 0 : return 1

    result = pow(x, int(y/2))

    result = result*result

    if y is even:
        return result
    else:
        retrun x * result


    for e.x
    2^4 =    2^2 * 2^2
            x^y/2 * x^y/2
    2^5 =   2* 2^2 * 2^2
            x* x^y/2 * x^y/2

"""


class Solution:

    def findpow(self, x, y):
        if x == 0:
            return 0

        if y==0:
            return 1

        result = self.findpow(x, int(y/2))
        result = result * result

        if y%2 == 0:
            return result
        else:
            return x * result

    def myPow(self, x: float, n: int) -> float:


        result = self.findpow(x, n)

        if n < 0 :
            return 1/result
        return result

