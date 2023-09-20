"""

Given a string s, find the length of the longest substring without repeating characters.
"""



"""
    sliding window with charset for checking repeating char

    if char is repeated remove left from charset increment left

    else:
        add r in charset
        max_length update.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        left = 0

        max_length= 0
        charset = set()

        for right in range(n):

            while s[right] in charset:
                charset.remove(s[left])
                left = left+1

            charset.add(s[right])
            if right-left+1 > max_length:
                max_length= right-left+1

        return max_length






