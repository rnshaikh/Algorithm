# heap sort:

"""
    1) build max heap for building max heap start from bottom to top which n//2 to 0
    2) after building max heap we swap n-1 element with 0 after swaping we need to heapify(i,0) beacuse max heap get disturbed.
    3) after building max heap we start from n-1 until 1 element swap with 0th element and heapify(arr, i, 0) 0th element
    4) heapify sort already sorted array it check left and right child is greater or not if greater then swap with that child call heapify again

"""



class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here

        largest = i
        left = 2*i + 1
        right = 2*i + 2

        if left<n and arr[left]> arr[largest]:
            largest = left

        if right<n and arr[right] > arr[largest]:
            largest = right


        if largest != i:
            arr[largest], arr[i] = arr[i] , arr[largest]
            self.heapify(arr,n, largest)

    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n//2 - 1, -1, -1):
            self.heapify(arr, n, i)


    #Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        #code here

        self.buildHeap(arr, n)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
        return arr
