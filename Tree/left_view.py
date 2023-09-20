Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument.
Left view of following tree is 1 2 4 8.



def pre_order(root,ans, level):

    if not root:
        return

    if len(ans) == level:
        ans.append(root.data)

    pre_order(root.left,ans, level+1)
    pre_order(root.right, ans, level+1)



def LeftView(root):

    # code here

    ans = []
    pre_order(root, ans,0)

    return ans
