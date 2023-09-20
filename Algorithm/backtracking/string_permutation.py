
import math


def permutation(st, left, right):

    if left == right :
        print(st)
    else:

        for i in range(left, right):
            st = swap(st, left, i)
            permutation(st, left+1, right)
            st = swap(st, left, i)


def swap(st, left, i):
    st = list(st)
    st[i], st[left] = st[left], st[i]
    st = "".join(st)
    return st


st = 'abcd'
left = 0
right = len(st)

permutation(st, left, right)

#print("st", st)



class Solution:
    
    def __init__(self):
        self.ans = set()
    
    def find_str(self, S, left, right):
        
        if left == right:
            self.ans.add(S)
        else:
            for i in range(left, right):
                S = self.swap(S, left, i)
                self.find_str(S, left+1, right)
                S = self.swap(S, left, i)
    
    def swap(self, S, left, right):
        
        s_list = list(S)
        s_list[left], s_list[right] = s_list[right], s_list[left]
        S = "".join(s_list)
        return S
        
    
    def find_permutation(self, S):
        # Code here
        
        self.find_str(S, 0, len(S))
        return sorted(self.ans)

