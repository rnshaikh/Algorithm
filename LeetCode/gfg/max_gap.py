"""
    Given an unsorted array Arr of length N. 
    Your task is to find the maximum difference between the successive elements in its sorted form.
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
        
    def find_max_min(self, arr, n):
        
        
        max_num = float('-inf')
        min_num = float('inf')
        
        
        for i in range(n):
            
            if arr[i] > max_num:
                max_num = arr[i]
            
            if arr[i] < min_num:
                min_num = arr[i]
                
        return max_num, min_num
    
    def maxSortedAdjacentDiff(self,arr, n):
    # code here

        if n <= 1:
            return 0


        max_num, min_num = self.find_max_min(arr, n)
        range_1 = (max_num - min_num) + 1
        
        
        hole_arr = [0] * range_1
        
        for i in range(n):
            hole_arr[arr[i]-min_num] = hole_arr[arr[i]-min_num] + 1
            
        
        j = 0
        
        for i in range(range_1):
            
            while hole_arr[i] > 0:
                hole_arr[i] -= 1
                arr[j] = i + min_num
                j = j+1

        max_diff = float('-inf')
        
        for i in range(n-1, -1, -1):
            
            if i-1 >= 0:
                max_diff = max(max_diff, abs(arr[i]-arr[i-1]))
                
                
        return max_diff
