"""
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

"""

"""

    1) first take dic for window and pattern to count no of chars

    2) res, res_len

    3) have = 0 and need = len(pattern) this much we want

    4) iterate throufgh string with i = 0
        increment count in window and check if itscount == patter count if yes incrment have by 1

        if have == neee:
            tak len if less res_len update res and res_len
            then decrmeent count from window for i chars
            if it is in pattern then decrement have by 1

        increment i by 1

"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        window = {}
        pattern = {}

        res = ""
        res_len = float('inf')

        for i in t:
            if i not in pattern:
                pattern[i] = 1
            else:
                pattern[i] += 1

        have = 0
        need = len(pattern)

        i = 0

        for j in range(len(s)):

            window[s[j]] = window.get(s[j], 0) + 1

            if s[j] in pattern and window[s[j]] == pattern[s[j]]:
                have = have+1

            while have == need:
                if res_len > (j-i+1):
                    res = s[i:j+1]
                    res_len = (j-i+1)

                window[s[i]] = window[s[i]] - 1

                if s[i] in pattern and window[s[i]] < pattern[s[i]]:
                    have = have-1

                i = i+1

            #print("res", res, res_len, j, i, (j-i+1))

        return res




class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        n = len(s)
        m = len(t)
        
        count_s = [0] * 256
        count_t = [0] * 256
        
        for i in t:
            count_t[ord(i)] += 1
        
        count = 0
        
        result_window = n+2
        result_start = 0
        
        start = 0
        for end in range(n):
            count_s[ord(s[end])]+=1
            
            if count_s[ord(s[end])] <= count_t[ord(s[end])]:
                count = count+1
                
            if count == m:
                while(count_s[ord(s[start])]) > count_t[ord(s[start])] or count_t[ord(s[start])] == 0:
                    if count_s[ord(s[start])]>count_t[ord(s[start])]:
                        count_s[ord(s[start])] -=1
                    start = start+1
                
                if (end-start+1) < result_window:
                    result_window = end-start+1
                    result_start = start
        
        if result_window == n+2:
            return ""
        
        return s[result_start: result_window+result_start]