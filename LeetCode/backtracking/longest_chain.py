"""
You are given N pairs of numbers. 
In every pair, the first number is always smaller than the second number. 
A pair (c, d) can follow another pair (a, b) if b < c. Chain of pairs can be formed in this fashion. 
You have to find the longest chain which can be formed from the given set of pairs. 
 

it is similiar to longest increasing subsequence.
and greedy method sort arr using 2nd element check if first element of curr obj is greater the 2nd ele of prev obj 
"""
'''
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
'''

from functools import cmp_to_key

class Solution:
    
    def comparator(x, y):
        return x.b - y.b
    
    def maxChainLen(self,Parr, n):
        # Parr:  list of pair
        #code here
        
        # dp = [1 for _ in range(n)]
        # max_len = 0
        
        # for i in range(1, n):
        #     for j in range(0, i):
        #         if Parr[i].a > Parr[j].b and dp[i] < 1+dp[j]:
        #             dp[i] = 1+dp[j]
        # return max(dp)
        
        Parr = sorted(Parr, key=cmp_to_key(Solution.comparator))
        
        prev = float('-inf')
        cnt = 0
        
        for i in Parr:
            if prev < i.a:
                cnt += 1
                prev = i.b
        return cnt
            
 