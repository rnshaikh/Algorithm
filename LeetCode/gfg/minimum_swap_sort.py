


"""
    sort array using merge sort in O(n log n)
    time.
    then store in hashmap with value as key and index value

    iterate over nums
    check if element is correct index in hashmap if not then swap until its correct increment.

"""




class Solution:

    #Function to find the minimum number of swaps required to sort the array.

    def divide(self, nums):

        if len(nums)>1:
            mid = len(nums)//2
            left = nums[:mid]
            right = nums[mid:]
            self.divide(left)
            self.divide(right)
            self.conquer(nums, left, right)


    def conquer(self, nums, left, right):
        i = 0
        j = 0
        k = 0

        while(i<len(left) and j < len(right)):

            if left[i] > right[j]:
                nums[k] = right[j]
                k = k + 1
                j = j + 1

            else:
                nums[k] = left[i]
                i = i + 1
                k = k + 1

        while(i < len(left)):
            nums[k] = left[i]
            i = i + 1
            k = k+1

        while(j < len(right)):
            nums[k] = right[j]
            k = k+1
            j = j+1

    def minSwaps(self, nums):
        #Code here

        swap = 0
        sort_nums = nums.copy()
        self.divide(sort_nums)
        nums_map = {}
        for i in range(len(sort_nums)):
            nums_map[sort_nums[i]] = i

        # print("nums map", nums_map)
        # print("nums, sort_nums", nums, sort_nums)
        for i in range(len(nums)):
            while nums[i] != sort_nums[i]:
                index = nums_map[nums[i]]
                nums[i], nums[index] = nums[index], nums[i]
                swap = swap + 1
        return swap
