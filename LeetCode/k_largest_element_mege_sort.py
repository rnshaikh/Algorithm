"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""


class Solution:

    def divide(self, nums):

        if len(nums)>1:

            mid = len(nums) // 2

            left = nums[:mid]
            right = nums[mid:]

            self.divide(left)
            self.divide(right)

            self.merge(nums, left, right)


    def merge(self, nums, left, right):

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):


            if left[i] < right[j]:
                nums[k] = left[i]
                i = i+1
                k = k+1
            else:
                nums[k] = right[j]
                j = j+1
                k = k+1

        while i < len(left):
            nums[k] = left[i]
            i = i+1
            k = k+1

        while j < len(right):
            nums[k] = right[j]
            j = j + 1
            k = k + 1

    def findKthLargest(self, nums: List[int], k: int) -> int:

        self.divide(nums)
        ans= []
        while(k>0):
            ans.append(nums.pop(-1))
            k = k-1
        return ans[-1]




from heapq import heappush, heappop

class Solution:
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap_a = []
        
        for i in range(k):
            heappush(heap_a, nums[i])
            
        
        for i in range(k, len(nums)):
            
            if nums[i] > heap_a[0]:
                heappop(heap_a)
                heappush(heap_a, nums[i])
                
        
        return heap_a[0]