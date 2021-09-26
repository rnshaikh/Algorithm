


class MaxHeap:

    def __init__(self):

        self.heap = []
        self.size = 0

    def get_parent(self, index):

        return int((index-1) / 2)

    def insert(self, value):
        self.heap.append(value)
        current = self.size
        while(self.heap[current]> self.heap[self.get_parent(current)]):
            self.heap[current], self.heap[self.get_parent(current)] = self.heap[self.get_parent(current)], self.heap[current]
            current = self.get_parent(current)

        self.size = self.size+1

        print("Heap:", self.heap)

    def heapify(self, n, index):

        import pdb
        pdb.set_trace()
        largest = index
        left = 2*index + 1
        right = 2*index + 2

        if left<n and self.heap[left] > self.heap[index]:
            largest = left

        elif right < n and self.heap[right] > self.heap[index]:
            largest = right

        if index != largest:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify(n, largest)

    def extract_max(self):
        max_ele = self.heap.pop(0)
        self.size = self.size - 1
        return max_ele
        self.heapify(self.size-1, 0)

    def decrease_key(self, index, value):

        self.heap[index] = value

        while(index != 0 and self.heap[self.get_parent(index)]< self.heap[index]):
            self.heap[self.get_parent(index)], self.heap[index] = self.heap[index], self.heap[self.get_parent(index)]
            index = self.get_parent(index)

    def delete(self, index):
        self.decrease_key(index, float('inf'))
        print(self.heap)
        self.extract_max()

if __name__ == "__main__":

    maxh = MaxHeap()

    ch = int(input("Enter A choice : \n 1) insert \n2)extract max  \n3) delete element at index \n4)Exit"))

    while(ch):

        if ch == 1:
            value = int(input("Enter a value:"))
            maxh.insert(value)

        if ch == 2:
            print(maxh.extract_max())

        if ch == 3:
            index = int(input("Enter element index to be deleted:"))
            maxh.delete(index)

        if ch == 4:
            break

        ch = int(input("Enter A choice : \n 1) insert \n2)extract max  \n3) delete element at index \n4)Exit"))





