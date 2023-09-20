# lowest common ancestore of bst

"""
    three cases :

        if curr node val is greater than both data: look into right
        if curr node val is less than both data : look into left
        if if split happen that is common ancestor


"""



class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        curr = root

        while curr:

            if curr.val > p.val and curr.val > q.val:
                curr = curr.left

            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right

            else:
                return curr
