"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.
"""

"""
    so in brute force with nested loop we can find count of subarry with exaclty k distinct numbers
    in O(n2) times

    in sliding window technique we can find it in O(n) times:
        here
        we going to find count of sub array with atmost k distinct element
        we going to find count of sub array with atmost k-1 distinct element

        then we are going to subtract 1 from 2 which will give us count of subarray with exactly k distinct element


        take hashmap with all numbers in array as key and value 0 initial it will count no element that show till now
        take diff for storing how many distinct element we find till now
        j = 0 left pointer
        total = 0 for storing total no of subarrya

        traverse each element in array
            if it value in hash  map is 0:
                increment diff
                increment hashmap value
            else:
                incrment hasmap value

            if diff <=k :
                total = total + (i-j+1) not of subarray

            else:
                diff is greater than k than we have to move left array till diff <= k
                while loop till j < n and j <= i and diff>k:
                    decrment hashmap value by 1
                    if hashmap value == 0:
                        decrement diff by 1
                    increment j by 1

                total = total + (i-j+1) here we are cacluating total no of subarray with new distinct element

        return total


"""


class Solution:


    def count_subarray(self, nums, k):

        if k == 0:
            return 0

        hashmap = {}
        for i in nums:
            hashmap[i] = 0

        total = 0
        j = 0
        diff = 0
        n = len(nums)-1

        for i in range(len(nums)):
            if hashmap[nums[i]]==0:
                diff = diff+1
                hashmap[nums[i]] = hashmap[nums[i]] + 1

            else:
                hashmap[nums[i]] = hashmap[nums[i]] + 1

            if diff <= k:
                total = total + (i-j+1)
            else:
                while(j < n and j <= i and diff > k):
                    hashmap[nums[j]] = hashmap[nums[j]] - 1
                    if hashmap[nums[j]] == 0:
                        diff = diff-1

                    j = j+1

                total = total+(i-j+1)
        return total


    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

#         j = 0
#         ans_lis = []
#         count = 0

#         for i in range(len(nums)):
#             diff = 1
#             ans = []
#             ans.append(nums[i])
#             if diff == k:
#                 count = count+1
#                 ans_lis.append(ans.copy())

#             for j in range(i+1, len(nums)):
#                 if diff > k:
#                     break

#                 else:
#                     if nums[j] in ans and diff<=k:
#                         ans.append(nums[j])
#                         ans_lis.append(ans.copy())
#                         if diff == k:
#                             count = count+1

#                     elif diff<k:
#                         ans.append(nums[j])
#                         diff = diff+1
#                         ans_lis.append(ans.copy())
#                         if diff == k :
#                             count = count+1

#                     else:
#                         break

#         print(ans_lis)
#         return count

        return self.count_subarray(nums,k) - self.count_subarray(nums, k-1)
