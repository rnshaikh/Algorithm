

# merge K sorted array

"""
    1) take heap and res list
    2) for i in range(k): heappush(1stvalue, arrayno, index)
    3) repeat heap is not empty
    4) heap pop value , arrayNo, index
    5) append value in res
    6) if index+1<K then heappush(nextvalue, arrayNo, index+!)

"""






from heapq import heapify, heappush,heappop

class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        # code here
        # return merged list

        res = []
        heap = []

        for i in range(K):
            heappush(heap, (arr[i][0], i, 0))

        while len(heap):

            value, arrayNo, index = heappop(heap)

            res.append(value)

            if index+1 < K:
                heappush(heap, (arr[arrayNo][index+1], arrayNo, index+1))

        return res
