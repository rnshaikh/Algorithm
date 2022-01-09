"""
    Given an unsorted array Arr of length N. Your task is to find the maximum difference between the successive elements in its sorted form.
    Return 0 if the array contains less than 2 elements.

    Expected Time Complexity: O(N)
"""

"""
    we can do this using sorting and then traversing arr and finding max diff
    but time complexity will be O(n log n)

    but there is pigeonhole sort which can do sorting in O(n + range) where range is size of pigeonhole
    this sorting only works when no of element is aproximately same to values in arr.

    in pigeon hole sorting is as follows

        1) find min and max of arr
        2) define range as max-min+1
        3) create pigeon arr with size as range
        3) travers through each element in arr:
            store element count at index pi[ele-min] = pi[ele-min] + 1

        i = 0
        4) traverse through range(pigeon_arr):
            while(count > 0):
                store element in arr[i] = count+min
                decrement count
                increment i


"""




class Solution:

    def find_min_max(self, arr):
        min_ele = 999999999999999
        max_ele = -999999999999999

        for ele in arr:
            if ele > max_ele:
                max_ele = ele

            if ele < min_ele:
                min_ele = ele

        return min_ele, max_ele



    def maxSortedAdjacentDiff(self,arr, n):
    # code here

        if n < 2:
            return 0

        min_ele, max_ele = self.find_min_max(arr)

        range_ele = (max_ele-min_ele) + 1

        pigeon_arr = [0] * range_ele

        for ele in arr:
            pigeon_arr[ele-min_ele] = pigeon_arr[ele-min_ele] + 1

        j = 0
        for i in range(range_ele):
            while(pigeon_arr[i] > 0):
                pigeon_arr[i] = pigeon_arr[i] - 1
                arr[j] = i + min_ele
                j = j + 1

        max_diff = 0

        for i in range(n):

            if i-1 < 0:
                if abs(arr[i]- arr[i+1]) > abs(max_diff):
                    max_diff = abs(arr[i] - arr[i+1])

            elif i+1 >= n:
                if abs(arr[i]-arr[i-1])> abs(max_diff):
                    max_diff =  abs(arr[i] - arr[i-1])

            else:

                if abs(arr[i]- arr[i+1]) > abs(max_diff):
                    max_diff = abs(arr[i] - arr[i+1])

                if abs(arr[i]-arr[i-1])> abs(max_diff):
                    max_diff =  abs(arr[i] - arr[i-1])

        return max_diff
