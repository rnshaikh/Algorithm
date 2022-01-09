"""
    Given an integer array of N elements. You need to find the maximum sum of two elements such that sum is closest to zero.

"""


"""
    first sort array in ascending order using merge sort
    then take min_sum = LARGE_INT
    take two pointer i, j from first , last
    while i < j
        calculate sum
        if abs(sum) < abs(min_sum):
            min_sum = sum

        if sum -ve then increment i

        if sum +ve then decrement j

"""


class Solution:
    def divide(self, arr):

        if len(arr) > 1:

            mid = len(arr) // 2

            left = arr[:mid]
            right = arr[mid:]

            self.divide(left)
            self.divide(right)

            self.conquer(arr, left, right)


    def conquer(self, arr, left, right):

        i = 0
        j = 0
        k = 0

        while(i < len(left) and j < len(right)):

            if left[i] < right[j]:

                arr[k] = left[i]
                i = i+1
                k = k+1

            else:
                arr[k] = right[j]
                j = j+1
                k = k+1

        while(i < len(left)):

            arr[k] = left[i]
            i = i+1
            k = k+1

        while(j < len(right)):
            arr[k] = right[j]
            j = j+1
            k = k+1

    def closestToZero (self,arr, n):
        # your code here

        self.divide(arr)
        print(arr)

        min_sum = 9999999999999999

        i = 0
        j = n-1

        while(i < j):

            sum1 = arr[i] + arr[j]

            if abs(sum1) <= abs(min_sum):
                if abs(sum1) == abs(min_sum) and sum1 < min_sum:
                    i = i+1
                    continue

                min_sum = sum1

            if sum1 < 0 :
                i = i+1

            else:
                j = j-1

        return min_sum





sol = Solution()

sol.closestToZero([-8,-66,-60], 3)



