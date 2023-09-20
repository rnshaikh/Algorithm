"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


algorithm:

    lefmost element in preorder is root
    inorder that element divided list into left side left subtree, right side right subtree


    so call build tree
    if curent > inend : return None

    if current == end : return node

    create node wih current value
    increment preorder + 1

    find its index in inorder

    for node.left = call build tree with start,  index-1
    for node.right = call build tree with index+1, len(indorder)-1

"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def __init__(self):
        self.prefix = 0
    
    def build_tree(self, preorder, inorder, start, end):
        if self.prefix >= len(preorder):
            return 
        
        if preorder[self.prefix] not in inorder[start:end+1]:
            return

        val = preorder[self.prefix]
        node = TreeNode(val)
        self.prefix += 1
        in_index = inorder.index(node.val)
        
        node.left = self.build_tree(preorder, inorder, start, in_index)
        node.right = self.build_tree(preorder, inorder, in_index, end)
        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        n = len(inorder)-1
        node = self.build_tree(preorder, inorder, 0, n)
        return node
    
    