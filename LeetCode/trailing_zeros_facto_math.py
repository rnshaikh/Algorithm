




class Solution:

    def fac(self, n):
        if n==0:
            return 1

        return n * self.fac(n-1)

    def trailingZeroes(self, n: int) -> int:

        facto = self.fac(n)
        count = 0
        facto_str = str(facto)
        for i in range(len(facto_str)-1, 0, -1):
            if int(facto_str[i]) == 0:
                count = count+1

            else:
                break

        return count
