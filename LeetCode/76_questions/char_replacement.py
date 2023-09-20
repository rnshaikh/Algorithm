
"""
    You are given a string s and an integer k. 
    You can choose any character of the string and change it to any other uppercase English character. 
    You can perform this operation at most k times.

    Return the length of the longest substring containing the same letter you can get after performing the above operations.




"""

"""
    sliding window with coumt char in window map
    max_f_char = curr max freq. chars

    left = 0
    for right to last char :

        update count of curr char
        update max_f_char

        while window len - max_f_char > k:
            remove countMap left char
            update left by 1

        if window_len > max_legth:
            update max_length

    PAY ATTENTION: limited to chars A-Z; for each capital char, check if it could create the longest repeating substr, use sliding window to optimize; check if windowlen=1 works, if yes, increment len, if not, shift window right;

"""




class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        n = len(s)
        max_length= 0
        left= 0

        count_map = {}
        most_f_char = 0

        for right in range(n):

            count_map[s[right]] = 1 + count_map.get(s[right], 0)
            most_f_char = max(most_f_char, count_map[s[right]])

            while (right-left+1) - most_f_char > k:
                count_map[s[left]] -= 1
                left = left+1

            if right-left+1 > max_length:
                max_length = right-left+1

        return max_length

