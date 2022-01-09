"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

"""




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans= []
        cur_level = []
        nex_level = []
        ltr = True

        if not root:
            return []

        cur_level.append(root)
        level = []

        while(len(cur_level)>0):

            node = cur_level.pop(-1)
            level.append(node.val)

            if ltr:
                if node.left:
                    nex_level.append(node.left)
                if node.right:
                    nex_level.append(node.right)
            else:
                if node.right:
                    nex_level.append(node.right)
                if node.left:
                    nex_level.append(node.left)


            if len(cur_level) == 0:
                ans.append(level)
                level = []
                cur_level, nex_level = nex_level, cur_level
                ltr = not ltr

        ans = [x for x in ans if x != []]
        return ans
