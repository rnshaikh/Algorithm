"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

"""
 

class Solution:
    
    def inorder(self, root, p):
        
        if not root:
            return
        
        val = self.inorder(root.left, p)
        
        if val != None:
            return val
        
        if p[0] == 1:
            return root.val
        
        p[0] = p[0]-1
        return self.inorder(root.right, p)
    

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        
        p = [k]
        ele = self.inorder(root, p)
        
        return ele
        