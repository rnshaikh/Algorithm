"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""





from heapq import heapify, heappush, heappop

class Solution:


    def __init__(self):
        self.heap = []
        heapify(self.heap)

    def heap_insert(self, ele):
        heappush(self.heap, ele)

    def extract_max(self):
        num = heappop(self.heap)
        return num

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ans = []
        count_dict = {}

        for i in nums:

            if str(i) not in count_dict:
                count_dict[str(i)] = 1

            else:
                count_dict[str(i)] = count_dict[str(i)]+1

        for key, value in count_dict.items():
            self.heap_insert(value*-1)

        largest = heapq.nsmallest(k, self.heap)
        keys = list(count_dict.keys())
        values = list(count_dict.values())

        while(len(largest)):
            count = largest.pop(0)
            count = count*-1
            index = values.index(count)
            values.pop(index)
            ele = int(keys.pop(index))
            ans.append(ele)

        return ans

