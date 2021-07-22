"""
There are given N ropes of different lengths, we need to connect these ropes into one rope.
The cost to connect two ropes is equal to sum of their lengths. The task is to connect the ropes with minimum cost.
"""


"""
    1) convert list to heap so that it will be sorted
    2) until k >1 , remove first 2 element add in m and then c=c+m
    3) push m to heap again
    4) return c
"""



import heapq

class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :

        # code here


        heapq.heapify(arr)
        c, m=0,0
        while n>1:
            a = heapq.heappop(arr)
            b = heapq.heappop(arr)

            m = a+b
            c = c+m
            heapq.heappush(arr, m)
            n = n-1
        return c
