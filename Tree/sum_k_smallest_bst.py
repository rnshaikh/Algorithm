

# sum of k smallest element in bst

"""
        1) do inorder traversal in list
        3) traverse list for k ele and sum them
        3) return sum

"""




def inorder(root,res):

    if not root:
        return
    inorder(root.left, res)
    res.append(root.key)
    inorder(root.right, res)
    return res


def sum(root, k):
    # code here

    res = inorder(root, [])
    res_1 = 0
    for i in range(k):
        res_1 = res_1+res[i]

    return res_1
