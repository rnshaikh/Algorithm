





class Solution:
    #Function to convert a binary tree into its mirror tree.

    def pre_order(self, root):

        if not root:
            return

        self.pre_order(root.left)
        self.pre_order(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp



    def mirror(self,root):
        # Code here

        self.pre_order(root)
        return root
