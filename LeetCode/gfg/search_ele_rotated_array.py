"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

"""



"""
    find pivoted element : element from which number get decreases
    then perform binary search on 0 pivot-1 and pivot+1 to last


"""




class Solution:

    def find_pivot(self, A, l, h, key):

        if l > h:
            return -1

        if l == h:
            return l

        mid = int((l + h) / 2)

        if(mid < h and A[mid] > A[mid+1]):
            return mid

        if(mid > l and A[mid] < A[mid-1]):
            return (mid-1)

        if A[l] >= A[mid]:
            return self.find_pivot(A, l, mid-1, key)

        else:
            return self.find_pivot(A,mid+1, h, key)


    def binary_search(self, A, l, h, key):


        if l > h:
            return -1

        mid = (l+h)//2

        if A[mid] == key:
            return mid

        elif A[mid] > key:
            return self.binary_search(A, l, mid-1, key)

        else:
            return self.binary_search(A, mid+1, h, key)


    def search(self, A : list, l : int, h : int, key : int):
        # Complete this function

        pivot = self.find_pivot(A, l, h, key)
        index = None
        if pivot == -1:
            index = self.binary_search(A, l, h, key)

        if A[pivot] == key:
            return pivot

        if A[0] > key:
            index = self.binary_search(A,pivot, h, key)

        if index == None:
            index = self.binary_search(A,l, pivot, key)

        return index

