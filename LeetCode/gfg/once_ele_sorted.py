


"""

for loop increment by 2
and
    last element check give solution


Xor of arr can give solution


binary search
An Efficient Solution can find the required element in O(Log n) time. The idea is to use Binary Search. Below is an observation on the input array.
All elements before the required have the first occurrence at even index (0, 2, ..) and the next occurrence at odd index (1, 3, …). And all elements after the required elements have the first occurrence at an odd index and the next occurrence at an even index.
1) Find the middle index, say ‘mid’.
2) If ‘mid’ is even, then compare arr[mid] and arr[mid + 1]. If both are the same, then the required element after ‘mid’ and else before mid.
3) If ‘mid’ is odd, then compare arr[mid] and arr[mid – 1]. If both are the same, then the required element after ‘mid’ and else before mid.


"""



class Solution:

    def divide(self, arr, start, end):

        if start > end:
            return None

        if start == end:
            return arr[start]

        mid = start + (end-start) // 2

        if mid%2 == 0:
            if arr[mid+1] == arr[mid]:
                return self.divide(arr, mid+1, end)
            else:
                return self.divide(arr, start, mid)

        else:
            if arr[mid-1] == arr[mid]:
                return self.divide(arr, mid+1, end)
            else:
                return self.divide(arr, start, mid)



    def findOnce(self,arr : list, n : int):
        # Complete this function

        res = arr[0]
        return self.divide(arr, 0, len(arr)-1)
