# Given a Binary Search Tree and a target sum. Check whether there's a pair of Nodes in the BST with value summing up to the target sum.


"""
        1) list inorder traversal
        2) tak i=0 and j = len(res)-1
        3) traver until i<j
        4) add res[i] and res[j] if  = target return 1 if < target i=i+1 else j= j-1
        5) return 0

"""


class Solution:
    # root : the root Node of the given BST
    # target : the target sum


    def inorder(self, root, res):

        if not root:
            return

        self.inorder(root.left, res)
        res.append(root.data)
        self.inorder(root.right, res)
        return res



    def isPairPresent(self,root, target):
        # code here.
        sum_a = 0
        res = self.inorder(root,[])
        i = 0
        j = len(res) - 1

        while(i < j):

            sum_b = res[i]+res[j]
            if sum_b == target:
                return 1
            elif sum_b > target:
                j = j-1

            elif sum_b < target:
                i = i+1

        return 0
