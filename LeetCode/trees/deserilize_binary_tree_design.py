"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

"""




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def __init__(self, str_tr=""):
        self.str_tr = ""
        self.preindex = 0

    def pre_order(self, root):

        if not root:
            return

        self.str_tr = self.str_tr + str(root.val)+","
        self.pre_order(root.left)
        self.pre_order(root.right)

    def in_order(self, root):

        if not root:
            return

        self.in_order(root.left)
        self.str_tr = self.str_tr + str(root.val)+","
        self.in_order(root.right)


    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.pre_order(root)
        self.str_tr = self.str_tr + "None"
        self.in_order(root)
        return self.str_tr

#     def construct(self, pre_order, in_order, start, end):

#         if start > end:
#             return

#         print("preindex", self.preindex)
#         node = TreeNode(pre_order[self.preindex])
#         self.preindex = self.preindex + 1

#         if start == end:
#             return node

#         index_inorder = in_order.index(node.val)

#         node.left = self.construct(pre_order, in_order, start, index_inorder-1)
#         node.right = self.construct(pre_order, in_order, index_inorder+1, end)

#         return node

    def build(self, preorder, inorder, current, inend):

        if current>inend:
            return None

        node = TreeNode(preorder[self.preindex])
        self.preindex = self.preindex + 1

        if current == inend:
            return node

        index = inorder.index(node.val)

        print("inorder index", index)

        node.left = self.build(preorder, inorder, current, index-1)
        node.right = self.build(preorder, inorder, index+1, inend)

        return node


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tree_order_array = data.split("None")
        pre_order = tree_order_array[0].split(",")
        in_order = tree_order_array[1].split(",")

        for i in range(len(pre_order)):
            if pre_order[i] != '':
                pre_order[i] = int(pre_order[i])
            else:
                pre_order.pop(i)

        for j in range(len(in_order)):
            if in_order[j] != '':
                in_order[j] = int(in_order[j])

            else:
                in_order.pop(j)

        self.preindex = 0
        print("pre_order, in_order", pre_order, in_order)
        node = self.build(pre_order, in_order, 0, len(pre_order)-1)
        return node



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
