"""

    zig zag traersal

    in bfs use queue and until its empty we print num one by one and append left child and right child

    here
    we two stack current_level, next level
    one ltr = False which false that we have push first right node and left node for next level

    while current level stack is empty
        pop nod
        append data in ans

        if ltr: thefirst left and right node push in next level
        else:  right and then left node push in next level

        if len(current_level) <= 0:
            then swap current_level, next_level = next_level, current_level
            invert ltr variable.



"""





#Function to return a list containing the level order traversal in spiral form.
def findSpiral(root):
    # Code here

    stq_l = []
    ans = []
    stq_l.append(root)
    stq = []
    ltr = False
    while(len(stq_l)):
        node = stq_l.pop(-1)

        if node and node.data != None:
            ans.append(node.data)

        if ltr:
            if node and node.left:
                stq.append(node.left)
            if node and node.right:
                stq.append(node.right)
        else:
            if node and node.right:
                stq.append(node.right)
            if node and node.left:
                stq.append(node.left)

        if len(stq_l) <= 0:
            stq, stq_l = stq_l, stq
            ltr = not ltr
    return ans
