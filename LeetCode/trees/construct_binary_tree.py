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
        self.preindex = 0

    def build(self, preorder, inorder, current, inend):

        if current>inend:
            return None

        node = TreeNode(preorder[self.preindex])
        self.preindex = self.preindex + 1

        if current == inend:
            return node

        index = inorder.index(node.val)


        node.left = self.build(preorder, inorder, current, index-1)
        node.right = self.build(preorder, inorder, index+1, inend)

        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if len(preorder) <= 1:
           return TreeNode(-1)


        head = self.build(preorder, inorder, 0, len(inorder)-1)

        if head:
            return head



