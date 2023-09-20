"""
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.
 Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""



"""
Alogrithnms:
    1) recursively can b build by queue or stack
    2) queue build all solution at one time while stack dfs build one solution at time

    2) pass list of digits combination and len(digits)
    3) take queue append empty string
    4) while queue is not empty:
        pop string if len(s) == n append in ans
        else:
            take string from digits combination [len(s)]
            iterate over char append that char in current s push into queue

"""

class Solution:

    def gen_combination(self, possible_in, n):
        ans = []
        queue = []
        s = ""

        queue.append(s)

        while(len(queue)):

            s = queue.pop(0)

            if len(s) == n:
                ans.append(s)
            else:
                for i in possible_in[len(s)]:
                    queue.append(s+i)

        return ans

    def letterCombinations(self, digits: str) -> List[str]:
        num_comb = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }

        if len(digits) <= 0:
            return []

        if len(digits) == 1:
            chars = num_comb[digits]
            ans = [ch for ch in chars]
            return ans

        possible_comb = []
        for i in digits:
            possible_comb.append(num_comb[i])

        ans = self.gen_combination(possible_comb, len(digits))
        return ans
