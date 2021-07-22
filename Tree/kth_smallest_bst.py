
class Solution:
    # Return the Kth smallest element in the given BST


    def inorder(self, root, res):

        if not root:
            return

        self.inorder(root.left, res)
        res.append(root.data)
        self.inorder(root.right, res)

        return res

    def KthSmallestElement(self, root, K):
        #code here.

        res = self.inorder(root, [])

        if K-1 >= len(res):
            return -1

        return res[K-1]
