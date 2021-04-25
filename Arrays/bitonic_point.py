
# bitonic point == element increasing and then decresing then maximum element


"""

    binary search

    left = 0 and right=h-2

    if (l<=right)
    if mid element greater then previous and next then return mid
    if mid element less than next element then l=mid+1, h=h
    else l=l, h=mid-1

    return -1
"""


#User function Template for python3
class Solution:


    def binarySearch(self, arr, left, right):

        if (left <= right):

            mid = (left + right) // 2;

            # base condition to check if
            # arr[mid] is bitonic point
            # or not
            if (arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]):
                return mid;

            # We assume that sequence
            # is bitonic. We go to right
            # subarray if middle point
            # is part of increasing
            # subsequence. Else we go
            # to left subarray.
            if (arr[mid] < arr[mid + 1]):
                return self.binarySearch(arr, mid + 1,right);
            else:
                return self.binarySearch(arr, left, mid - 1);

        return -1;


    def findMaximum(self,arr, n):
        # code here

        l =0
        h = n-1
        index = self.binarySearch(arr, 0, n-2)
        if index != -1:
            return arr[index]

        return arr[-1]
