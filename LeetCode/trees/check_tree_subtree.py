"""
    Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

    A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

"""

"""

    first travers throught tree using bfs
    in that check if node.val == s.val and flag == False:
        call is_identical function which set flag

    push node.left in queue
    and node.right in queue


    in is_identical function

        check if T == None and S==None return True

        check if T == None and S != None or S==None and T!=None return False

        check if T.val is not equal to S.val return False


        if(recursively T.right and S.right and T.left and S.left) return True

        else:
            return False


"""


class Solution:

    def is_identical(self, T, S):

        if(T == None and S == None):
            return True
        if(T == None or S == None):
            return False
        return T.data == S.data and self.is_identical(T.left,S.left) and self.is_identical(T.right,S.right)

    def isSubTree(self, T, S):
        # Code here

        if(T != None):
            return self.is_identical(T,S) or self.isSubTree(T.left,S) or self.isSubTree(T.right,S)
        return False






class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        flag = False
        if root == None and subRoot == None:
            return True

        flag = self.handler(root, subRoot, flag)
        return flag

    def is_identical(self, T, S):

        if T == None and S == None:
            return True

        if (T != None and S == None) or (T == None and S!= None):
            return False

        if T.val != S.val :
            return False

        if (self.is_identical(T.right, S.right) and self.is_identical(T.left, S.left)):
            return True

        else:
            return False

    def handler(self, T, S, flag):

        temp = T
        queue = []
        queue.append(temp)

        while len(queue):
            node = queue.pop(0)
            if node and node.val == S.val and not flag:
                flag = self.is_identical(node, S)

            if node and node.left:
                queue.append(node.left)

            if node and node.right:
                queue.append(node.right)

        return flag
