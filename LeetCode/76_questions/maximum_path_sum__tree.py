"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""

"""
    1) there are two case at every node at current node we have calculate sum with splitting branch including left and right childern  and root node value and update res if max
    2) at current node we have to retrun sum without splitting branch  take max of left or right child with current node value

"""




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_sum = [root.val]

        def dfs(root):

            if not root:
                return 0

            max_left = dfs(root.left)
            max_right = dfs(root.right)

            max_left = max(max_left, 0)
            max_right = max(max_right, 0)
            # without split
            res = root.val + max_left + max_right
            max_sum[0] = max(max_sum[0], res)

            return root.val + max(max_left, max_right)


        dfs(root)

        return max_sum[0]
