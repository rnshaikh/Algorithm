# Given a BST, modify it so that all greater values in the given BST are added to every node.



"""
    same as bst_sum_greater only diff current node value is added in sum of all nodes greater than current node
"""

def transform(root, res):

    if not root:
        return

    transform(root.right, res)
    temp = root.data
    root.data = res[0]+root.data
    res[0] = res[0] + temp

    transform(root.left, res)


def modify(root):
    #code here

    transform(root, [0])
    return root
