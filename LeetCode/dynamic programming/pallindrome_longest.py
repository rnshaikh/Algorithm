"""
Given a string S consisting of opening and closing parenthesis '(' and ')'. Find length of the longest valid parenthesis substring.

A parenthesis string is valid if:

For every opening parenthesis, there is a closing parenthesis.
Opening parenthesis must be closed in the correct order.

"""

"""
Input: str = "(()()"

Initialize result as 0 and stack with one item -1.

For i = 0, str[0] = '(', we push 0 in stack

For i = 1, str[1] = '(', we push 1 in stack

For i = 2, str[2] = ')', currently stack has 
[-1, 0, 1], we pop from the stack and the stack
now is [-1, 0] and length of current valid substring 
becomes 2 (we get this 2 by subtracting stack top from 
current index).

Since the current length is more than the current result, 
we update the result.

"""

class Solution:
    
    def is_valid(self, S):
        
        stack = []
        
        for i in S:
            
            if i == "(":
                stack.append(i)
            else:
                if not stack:
                    return False
                ch = stack.pop(-1)
        if len(stack):
            return False
        return True
            
    
    def maxLength(self, S):
        # code here
        
        n = len(S)
        max_length = 0
        
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if i == j:
        #             continue
                
        #         flag = self.is_valid(S[i:j+1])
        #         if flag and max_length < (j-i+1):
        #             max_length = j-i+1
                    
        # return max_length
        
        stack = []
        stack.append(-1)
        
        for i in range(n):
            
            if S[i] == "(":
                stack.append(i)
                
            else:
                stack.pop()
                if not len(stack):
                    stack.append(i)
                else:
                    max_ = i-stack[-1]
                    if max_ > max_length:
                        max_length = max_
                        
        return max_length
                    
        
        # dp = [0 for _ in range(n)]
        
        
        # for i in range(1, n):
        #     if ((S[i] == ')' and i - dp[i - 1] - 1 >= 0 and S[i - dp[i - 1] - 1] == '(')):
        #         dp[i] = dp[i - 1] + 2
        #         if (i - dp[i - 1] - 2 >= 0):
        #             dp[i] += (dp[i -dp[i - 1] - 2])
        #         else:
        #             dp[i] += 0
        #         max_length = max(dp[i], max_length)
        # return max_length