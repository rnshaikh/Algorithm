"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

"""


class Solution:


    def check_balanced(self, parn):

        stack = []

        if len(parn) == 1:
            return True

        for i in parn:
            if i == "(":
                stack.append(i)
            elif i == ")" and len(stack):
                st = stack.pop(-1)
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False


    def recur(self, sti, ans, n):

        if len(sti)== n*2:
            if self.check_balanced(sti):
                return ans.append(sti)
                print("ans", ans)
            return ans

        self.recur(sti+"(", ans, n)
        self.recur(sti+")", ans, n)
        return ans

    def generateParenthesis(self, n: int) -> List[str]:

        st = ""
        ans = []
#         queue = []
#         queue.append(st)
#         ans = []
#         while(len(queue)):

#             sti = queue.pop(0)

#             if len(sti) == n*2:
#                 ch = self.check_balanced(sti)
#                 if ch:
#                     ans.append(sti)

#             else:
#                 queue.append(sti+"(")
#                 queue.append(sti+")")

        ans = self.recur(st, ans, n)

        return ans
