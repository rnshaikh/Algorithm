"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, 
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

"""



"""
    find pivoted element : element from which number get decreases
    then perform binary search on 0 pivot-1 and pivot+1 to last


"""




class Solution:
    
    
    
    def find(self, nums, start, end, n):
        
        
        if start > end:
            return -1
        
        if start == end:
            return start
        
        mid = (start+end) // 2
        
        if mid < n and nums[mid] > nums[mid+1]:
            return mid
        
        if mid>=0 and nums[mid] < nums[mid-1]:
            return mid-1
        
        if nums[mid] <= nums[start]:
            return self.find(nums, start, mid-1, n)
        
        return self.find(nums,mid, end, n)
    
    
    def bin_search(self, nums, start, end, target):
        
        while start <= end:
    
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                end = mid-1
            
            else:
                start = mid+1
        
        return -1
            
          
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        pivot = self.find(nums, 0, n-1, n)
        
        if pivot == -1:
            index = self.bin_search(nums, 0, n-1, target)
            return index
        
        if nums[pivot] == target:
            return pivot
        
        index = -1
        
        if nums[pivot] >= target and nums[0]<=target:
            index = self.bin_search(nums, 0, pivot, target)
            
        
        if index != None and index != -1:
            return index
        
        index = self.bin_search(nums, pivot+1, n-1, target)
        
        return index
            