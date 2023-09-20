"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

"""
"""
    # bucket sort but reverse. count is index and numbers in list so 2times occur num's will be in 2nd index list O(n) time instead of heap which O(nlogn)


    hashmap count occurance of each element in list

    then take bucket to store element its countwise index for element with 1 occurance will at 1 index

    iterate through hashmap store element in buckets with its counter as index

    the traverse from last to 0:
        append element in ans incremen count if if k return ans

"""



class Solution:

    def topKFrequent(self, num: List[int], k: int) -> List[int]:


        hashmap = {}
        buckets = [[] for _ in range(len(num)+1)]

        for i in num:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        for key, value in hashmap.items():
            buckets[value].append(key)

        count = 0
        ans = []
        for i in range(len(num), -1, -1):
            for nu in buckets[i]:
                ans.append(nu)
                count += 1
                if count >= k:
                    return ans



from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ans = []
        hash_map = {}
        for i in range(len(nums)):    
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
            
            else:
                hash_map[nums[i]] += 1
        
        
        min_heap = []
        for key, value in hash_map.items():
            heappush(min_heap, (-value, key))
            
        
        while len(min_heap):
            count, value = heappop(min_heap)
            count = count * -1
            if k>0:
                ans.append(value)
                k = k-1
            else:
                break
        
        return ans