"""

Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == " ":
            return 1

        if len(s) == 1:
            return 1

        ans = ""
        last_st = ""
        word = []

        for i in s:
            if i in word:
                if len(last_st) < len(ans):
                    last_st = ans
                    ans = "" + i
            else:
                ans = ans + i
                word.append(i)

        if len(ans)> len(last_st):
            last_st = ans

        if last_st == "":
            return len(ans)

        return len(last_st)
