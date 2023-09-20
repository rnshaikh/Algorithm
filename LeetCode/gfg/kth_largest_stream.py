"""
    Given an input stream arr[] of n integers. 
    Find the Kth largest element for each element in the stream and if the Kth element doesn't exist, 
    return -1.
"""

"""
    user min_heap of size k so that kth largest element will be pop in O(1) using heappop

    traverse element of arr
        push in min heap first
        check if i+1 < k :
            ans.append(-1)
        else:

            pop element from min_heap until len min_heap is k

            pop kth largest element from min_heap
            append in ans
            push back to min_heap

"""

import heapq

class Solution:

    def kthLargest(self, k, arr, n):
        # code here
        ans = []
        min_heap = []
        for i in range(n):
            heapq.heappush(min_heap, arr[i])
            if i+1 < k:
                ans.append(-1)
            else:
                while(len(min_heap)>k):
                    heapq.heappop(min_heap)

                kth = heapq.heappop(min_heap)
                ans.append(kth)
                heapq.heappush(min_heap, kth)

        return ans
