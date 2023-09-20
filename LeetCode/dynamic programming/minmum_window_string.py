"""
Given two strings S and P. Find the smallest window in the string S 
consisting of all the characters(including duplicates) of the string P.
Return "-1" in case there is no such window present. 
In case there are multiple such windows of same length, return the one with the least starting index.

"""

"""
    this is solved by sliding window technique.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        n = len(s)
        m = len(t)


        count_t = [0] * 256
        count_s = [0] * 256

        result_window = n+2
        result_start = 0
        
        count = 0
        start = 0
    
        for i in t:
            count_t[ord(i)] += 1

        for end in range(n):
            count_s[ord(s[end])] += 1

            if count_s[ord(s[end])] <= count_t[ord(s[end])]:
                count = count+1

            if count == m:

                while count_s[ord(s[start])] >  count_t[ord(s[start])] or count_t[ord(s[start])] == 0:
                    if count_s[ord(s[start])] > count_t[ord(s[start])]:
                        count_s[ord(s[start])] -=1
                    start = start+1

                if (end-start+1) <= result_window:
                    result_window = (end-start+1)
                    result_start = start
        
        if result_window == n+2:
            return ""
        return s[result_start:result_start+result_window]



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        n = len(s)
        m = len(t)

        pattern = {}
        string = {}

        for i in t:
            pattern[i] = pattern.get(i, 0)+1
        
        have = 0
        need = len(pattern)

        result_start = n+2
        result = n+2
        start = 0

        for end in range(n):
            
            string[s[end]] = string.get(s[end], 0) + 1
            
            if s[end] in pattern and string[s[end]] == pattern[s[end]]:
                have = have+1

            print("have", have, need) 
            while have == need:

                if end-start+1 < result:
                    result = end-start+1
                    result_start = start

                string[s[start]] -= 1
                
                if s[start] in pattern and string[s[start]] < pattern[s[start]]:
                    have = have-1
                start = start+1

        if result == n+2:
            return ""
        return s[result_start: result_start+result]
