"""
    Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

"""

"""
    in dynamic progamming

        dp [i] = 1 + dp[i-offset]  where offset is highest of 2 which == i

        offset = 1

        for i = 2
        2*offset == i
        then offset = i



If we observe bits from rightmost side at distance i than bits get inverted after 2^i position in vertical sequence.
for example n = 5;
0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
Observe the right most bit (i = 0) the bits get flipped after (2^0 = 1)
Observe the 3rd rightmost bit (i = 2) the bits get flipped after (2^2 = 4)
So, We can count bits in vertical fashion such that at i’th right most position bits will be get flipped after 2^i iteration;

"""


class Solution:
    def countBits(self, n: int) -> List[int]:

#         ans = [0]

#         for i in range(1, n+1):
#             result = 0
#             while i :
#                 result = result + (i & 1)
#                 i = i >> 1

#             ans.append(result)

#         return ans


        dp = [0 for _ in range(n+1)]
        offset = 1

        for i in range(1, n+1):

            if 2*offset == i:
                offset = i

            dp[i] = 1 + dp[i-offset]

        return dp
