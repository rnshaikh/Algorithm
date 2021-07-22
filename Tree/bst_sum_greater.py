# Given a BST, transform it into greater sum tree where each node contains sum of all nodes greater than that node.

"""
    1) call recursive function with [0],root
    2) exit condition if root==None return
    3) traverse to root.right first
    4) temp = root.data update root.data = res[0] and then res[0] = res[0]+temp
    5) then traverse root.left

"""



class Solution:

    def transform(self, root, res):

        if root == None:
            return
        self.transform(root.right, res)
        temp = root.data
        print("root data", temp)
        print("res", res[0])
        root.data = res[0]

        res[0] = res[0]+temp
        self.transform(root.left, res)

    def transformTree(self, root):
        #code here
        self.transform(root, [0])

