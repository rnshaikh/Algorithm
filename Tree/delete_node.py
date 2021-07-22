



def find_min(root):

    if not root:
        return
    elif root.left == None:
        return root
    return find_min(root.left)


def deleteNode(root, X):
    # code here.

    if not root:
        return root

    elif root.data > X:
        root.left = deleteNode(root.left, X)
    elif root.data < X:
        root.right = deleteNode(root.right, X)
    else:
        if root.right == None and root.left==None:
            del root
            root = None
        elif root.right == None:
            temp = root
            root = root.left
            del temp
        elif root.left == None:
            temp = root
            root = root.right
            del temp
        else:
            min_node = find_min(root.right)
            root.data = min_node.data
            root.right = deleteNode(root.right, min_node.data)

    return root
