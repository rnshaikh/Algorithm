"""

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).


"""

"""

    Algorithm:
        i iterate over string and j iterate over pattern

        exit cases:
            i becomes greater than string and j becomes greater than pattern
            return 1 success

            if j gets exahusted return 0 failure

            matach =  i > len(string) and string[i] == pattern[j] or string[i] == "."
            this is checking if current char matches or current character matches with .

            if pattern[j+1] next character is * then
                check with empty char as * or check with preceding element as star
                back(i, j+2) or back(i+1, j)

            if match (current chars):
                back(i+1, j+1)

            else:
                return 0


"""


class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:

        cache = {}
        def backtracking(i, j):

                if (i,j) in cache:
                    return cache[(i,j)]

                if i >= len(string) and j >= len(pattern):
                    return 1

                if j >= len(pattern):
                    return 0


                match = (i < len(string) and ( string[i] == pattern[j] or pattern[j] == "."))

                if j+1 < len(pattern) and pattern[j+1] == "*":

                    cache[(i,j)] = (backtracking(i, j+2) or
                                    (match and backtracking(i+1, j)))
                    return cache[(i,j)]

                if match:
                    cache[(i, j)] = backtracking(i+1, j+1)
                    return cache[(i,j)]

                else:
                    cache[(i,j)] = 0
                    return cache[(i,j)]

        return backtracking(0, 0)







class Solution:
    def wildCard(self,pattern, string):
        # Code here

        cache = {}
        def backtracking(i, j):

            if (i,j) in cache:
                return cache[(i,j)]

            if i >= len(string) and j >= len(pattern):
                return 1

            if j >= len(pattern):
                return 0

            match = (i < len(string) and (string[i] == pattern[j] or pattern[j] == "?"))

            if pattern[j] == "*":

                cache[(i,j)] = (backtracking(i, j+1) or
                                (i < len(string) and backtracking(i+1, j)))
                return cache[(i,j)]

            if match:
                cache[(i,j)] = backtracking(i+1, j+1)
                return cache[(i,j)]
            else:
                cache[(i,j)] = 0
                return cache[(i,j)]

        return backtracking(0, 0)

