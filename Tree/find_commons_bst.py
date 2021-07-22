



"""
 1) list out inorder traversal of first bst.
 2) traverse list and data in 2nd tree.
 3) append into res
 4) return res
"""




class Solution:

    #Function to find the nodes that are common in both BST.

    def inorder(self, root, res):

        if not root:
            return

        self.inorder(root.left, res)
        res.append(root.data)
        self.inorder(root.right, res)

        return res

    def find(self, root, x):

        if not root:
            return False

        elif root.data > x:
            return self.find(root.left, x)

        elif root.data < x:
            return self.find(root.right, x)

        elif root.data == x:
            return root.data

    def findCommon(self, root1, root2):
        # code here

        res = self.inorder(root1, [])

        res_1 = []
        for i in res:
            fin_res = self.find(root2, i)
            if fin_res:
                res_1.append(fin_res)

        return res_1
