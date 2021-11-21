# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorder(self, node):
        global k;

        if not node:
            return None

        val = self.inorder(node.left, k)
        if val != None:
            return val

        if k == 1:
            return node.val
        k = k-1
        return self.inorder(node.right, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        k = k
        val = self.inorder(root)
        return val
