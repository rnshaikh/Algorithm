"""
You are given a string s and an integer k. You can choose any character of the string and change it to 
any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa. 


"""

"""
    sliding window technique with max_char_c 

    tak start, n, count {} 

    iterate thourgh s with end:
        update count of end char

        update max_char_c 

        while len of the curr_str - max_char_c > k:
            decrement start in count 
            increment start by 1

        if curr_len > max_len
            max_len = curr_len


"""





class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        n = len(s)
        start = 0
        max_len = 0
        max_char_c = 0
        
        count = {}
        
        
        for end in range(n):
            
            count[s[end]] = count.get(s[end], 0) + 1
            max_char_c = max(max_char_c, count[s[end]])
            
            
            while (end-start+1) - max_char_c  > k:
                count[s[start]] -= 1
                start = start+1
                
                
            if end-start+1 > max_len:
                max_len = end-start+1
                
        
        return end-start+1
