
# Find peak element if elment neibour are less retrun that element index.

class Solution:
    def peakElement(self,arr, n):

        for i in range(0, n):

            if n == 1:
                return i

            if i == 0:
                if arr[i]> arr[i+1]:
                    return i

            elif i == n-1:
                if arr[i] > arr[i-1]:
                    return i

            elif arr[i]> arr[i+1] and arr[i]> arr[i-1]:
                return i
