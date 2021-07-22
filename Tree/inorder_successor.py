

"""

    find node
    if node present have right subtree find min node in right subtree
    if node dont have right subtree then find closes ancestor greater than node
        if start from root
        while ancestor != current:
            if ancestor.data > current:
                successor = ancestor
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right

"""




class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')

    def find_min(self, root):

        if not root:
            return None
        elif root.left == None:
            return root
        return self.find_min(root.left)

    def find(self, root, k):
        if not root:
            return None

        elif root.data == k:
            return root

        elif root.data > k :
            return self.find(root.left, k)

        elif root.data < k:
            return self.find(root.right, k)


    def inorderSuccessor(self, root, x):
        # Code here

        current = self.find(root, x.data)

        if not current:
            return None

        elif current.right:
            successor = self.find_min(current.right)
            return successor

        else:
            successor = None
            ancestor = root

            while(ancestor != current):

                if ancestor.data > current.data:
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
        return successor

