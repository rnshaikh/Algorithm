


# return the Kth largest element in the given BST rooted at 'root'

"""
    1) list order traversal
    2) reverse list
    3) return k-1 element
"""

class Solution:

    def inorder(self, root, res):

        if not root:
            return

        self.inorder(root.left,res)
        res.append(root.data)
        self.inorder(root.right, res)
        return res


    def kthLargest(self,root, k):

        res = self.inorder(root,[])

        return res[::-1][k-1]
