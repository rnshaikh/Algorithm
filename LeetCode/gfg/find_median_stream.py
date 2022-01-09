"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

"""

"""
    for finding median in stream in O(1) time and iserting element in o(logn) we can use two heap max heap and min heap

    maxheap store 1st half element  min heap store 2nd half element

    differen between two heap should not be greater than 1

    and all element in maxheap should be less than all element in minheap

    if maxheap is greate then median is retrun largest element in maxheap

    if minheap is greater then median is retrun smallest element in minheap

    if both are equal then median is addition largest(maxhaeap) + smallest(minheap) / 2

"""





import heapq

class MedianFinder:

    def __init__(self):

        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:

        heapq.heappush(self.small, num*-1)

        if self.small and self.large and (self.small[0]*-1) > self.large[0]:
            num = heapq.heappop(self.small)
            heapq.heappush(self.large, num*-1)

        if len(self.small) > len(self.large)+1:
            num = heapq.heappop(self.small)
            heapq.heappush(self.large, num*-1)

        if len(self.large) > len(self.small) + 1:
            num = heapq.heappop(self.large)
            heapq.heappush(self.small, num*-1)



    def findMedian(self) -> float:

        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return ((self.small[0]*-1) + self.large[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
