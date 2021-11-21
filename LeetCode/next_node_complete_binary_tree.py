# Definition for a Node.

"""
you are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""



class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:


    def recur(self, node):

        if not node:
            return

        if node.left:
            if node.right:
                node.left.next = node.right

        if node.right:
            if node.next:
                node.right.next = node.next.left

        self.recur(node.left)
        self.recur(node.right)




    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return None

        #current_l = []
        #next_l = []

        #temp = root
        #current_l.append(temp)

        #while(len(current_l)):


            #node = current_l.pop(0)

            #if len(current_l):
                #node.next = current_l[0]

            #if node.left:
                #next_l.append(node.left)

            #if node.right:
                #next_l.append(node.right)

            #if len(current_l) == 0:
                #current_l, next_l = next_l, current_l
        #return root
        self.recur(root)

        return root
