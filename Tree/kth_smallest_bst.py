
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
