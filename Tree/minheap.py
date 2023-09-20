
from heapq import heapify, heappush, heappop



class MinHeap:

    def __init__(self):
        self.heap = []


    def parent(self, index):
        return (index-1)//2

    def insert(self,value):
        heappush(self.heap, value)
        print(self.heap)

    def getmin(self):

        return self.heap[0]

    def extractMin(self):
        num = heappop(self.heap)
        print("extrct func",self.heap)
        return num

    def decreaseKey(self, index, value):

        self.heap[index] = value

        while(index != 0 and self.heap[self.parent(index)] > self.heap[index]):
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]


    def delete(self, index):

        self.decreaseKey(index, float("-inf"))
        print("del function", self.heap)
        self.extractMin()





heap = MinHeap()
heap.insert(3)
heap.insert(2)
heap.insert(15)
heap.insert(5)
heap.insert(4)
heap.insert(45)
heap.delete(1)
print("After delete index 1", heap.heap)

print("Extract Min", heap.extractMin())
#print("Get Min :", heap.getmin())
# heap.decreaseKey(2, 1)
# print("After decreaseKey at 2 to 1" , heap.getmin())

