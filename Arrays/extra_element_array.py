# find extra element in 1st array which not in 2nd sorted array's


"""
Method1
    find differen of two sets
    then find index of that element in first array
"""

"""
    method 2:
    binary search:

    logic all indices of element greater than or equal to index of missing element will have different element in both array

    index = len(2nd array)
    left =0
    right = len(2nd aaray-1)

    while left < = right:

        mide = left+right/2

        if a[mid] == b[mid]:
            left = mid +1

        else:
            index= mid
            right = mid-1

    return index

"""



class Solution:
    def findExtra(self,a,b,n):

        #add code here

        # ele_list = list(set(a) - set(b))

        # index = a.index(ele_list[0])

        # return index

        index= len(b)
        left = 0
        right = len(b) -1

        while left <= right:

            mid = (int)((left + right) / 2)

            if a[mid] == b[mid]:
                left = mid+1
            else:
                index = mid
                right = mid-1

        return index
