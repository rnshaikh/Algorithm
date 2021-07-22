
# find median

"""

    1) first get inorder traversal
    2) list check if odd then median is len / 2 return number
    3) else take len/2 and previous number and sum of that/2 if it is int convert and return else return
"""





from decimal import Decimal

def inorder(root, res):

    if not root:
        return

    inorder(root.left, res)

    res.append(root.data)

    inorder(root.right, res)

    return res


def findMedian(root):
    # code here
    # return the median


    res = inorder(root, [])

    if int(len(res) %2) == 0:

        mid = int(len(res) / 2)
        mid0 = mid-1
        result = (res[mid] + res[mid0])/2
        if Decimal(result)%1 == 0:
            return int(result)
        return result

    mid = int(len(res)/2)
    return res[mid]

