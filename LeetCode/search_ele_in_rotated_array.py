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

    def find_pivot(self, nums, low, high, n):

        if high < low:
            return -1

        #print("pivot, high, low", high, low)
        if high == low:
            #print("pivot return2")
            return low

        mid = (high+low) // 2
        #print("pivot mid", mid)
        if ( mid < high and nums[mid] > nums[mid+1]):
            print("pivot return1")
            return mid

        if(mid > low and nums[mid] < nums[mid-1]):
            return (mid-1)

        if nums[mid] <= nums[low]:
            return self.find_pivot(nums, low, mid-1, n)
        else:
            return self.find_pivot(nums, mid+1, high, n)


    def binary_search(self, nums, low, high, n, target):

        print("low high", low, high)
        if low > high:
            return -1

        mid = (low+high) // 2
        print("mid", mid)
        if nums[mid] == target:
            print("goot ans")
            return mid

        if nums[mid] > target:
            return self.binary_search(nums, low, mid-1, n, target)

        else:
            return self.binary_search(nums, mid+1, high, n, target)



    def search(self, nums: List[int], target: int) -> int:

#         for i in nums:
#             if i == target:
#                 return nums.index(i)

#         return -1

        pivot = self.find_pivot(nums, 0, len(nums)-1, len(nums))
        print("pivot", pivot)
        if pivot == -1:
            return self.binary_search(nums, 0, len(nums)-1, len(nums), target)

        if nums[pivot] == target:
            return pivot

        if nums[0] <= nums[pivot]:
            index = self.binary_search(nums, 0, pivot-1, len(nums), target)

        if index!=None and index != -1:
            return index

        index = self.binary_search(nums, pivot+1, len(nums)-1, len(nums), target)
        return index
