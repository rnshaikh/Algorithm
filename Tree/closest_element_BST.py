#Given a BST and an integer. Find the least absolute difference between any node value of the BST and the given integer.


"""
        1) list inorder traversal
        2) K is present in list return 0
        3) take min_diff = large num
        3) traverse through list
        4) check if data > K then update min_diff
        5) else update min_diff
        6) return min_diff
"""


class Solution:

    #Function to find the least absolute difference between any node
    #value of the BST and the given integer.

    def inorder(self, root, res):

        if not root:
            return

        self.inorder(root.left, res)
        res.append(root.data)
        self.inorder(root.right, res)
        return res


    def minDiff(self,root, K):
        # code here
        res = self.inorder(root, [])

        if K in res:
            return 0

        min_diff = 999999999

        for i in res:
            if i > K:
                min_diff = min(min_diff, abs(i-K))

            else:
                min_diff = min(min_diff, abs(i-K))
