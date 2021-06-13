'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# Return a list containing the Preoorder traversal of the given tree, (root,left,right)

"""
    1) take stack and list
    2) push root into stack
    3) traverse until stack is empty
    3) pop element from stack. push its data into ans
    4) check if element have right node push into stack
    5) check if element have left node push into stack
    6) return ans list

"""



def preOrder(root):
    # code here

    ans = []
    stack = []

    stack.append(root)

    while len(stack):
        s = stack.pop()
        ans.append(s.data)

        if s.right:
            stack.append(s.right)

        if s.left:
            stack.append(s.left)

    return ans
