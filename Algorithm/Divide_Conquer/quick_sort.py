

"""
    1) first you choose pivot element first element
    2) then divide list into two part around pivot element
    3) recursively sort first part
    4) recursively sort second part

    running time : O(nlogn)
    no extra space is required arranged element in same array.

"""


"""
    partition function
    1) first choos first elemeent as pivot element
    2) i = pivot_index+1,
    3) traverse j through pivot_index+1 to end
    4) if array[j] < pivot_element
    5) than swap array[i] and array[j] and increment i = i+1
    6) after loop pivot element position will be at i-1 so swap array[pivot_index] with i-1
    7) return i-1 as correct index of pivot element

    Divide function
    start < end
    8) in divide function after getting pivot index divide array into arrar, start, pi left half recursively call divide function
    until start<end
    9) divide array into right half array, pi+1, end   ommiting pivot element as it is sorted already
    recursively call divide function until start<end


    if array is already sorted and we choose first or last element as pivot element
    it gives O(n2) running times

    so choosing random pivot or element which is median array gives O(n logn)

"""



A = [3,7,8,2,1,4,9]

class Quick:

    def __init__(self):
        pass


    def quick_sort(self, array, start, end):

        import pdb
        pdb.set_trace()

        # if len(array)<=1:
        #     return

        if start < end:
            pi = self.partition(array, start, end)
            self.quick_sort(array, start, pi)
            self.quick_sort(array, pi+1, end)

    def partition(self, array, start, end):

        pivot_index = start
        pivot_ele = array[pivot_index]
        i = pivot_index+1

        for j in range(pivot_index+1, end):

            if array[j] < pivot_ele:
                array[i], array[j] = array[j], array[i]
                i = i+1


        array[pivot_index] , array[i-1] = array[i-1], array[pivot_index]

        return i-1


if __name__ == "__main__":

    q = Quick()

    q.quick_sort(A, 0, len(A)-1)

    print("Sorted Array", A)















# # Python3 implementation of QuickSort

# # This Function handles sorting part of quick sort
# # start and end points to first and last element of
# # an array respectively
# def partition(start, end, array):

#     # Initializing pivot's index to start
#     pivot_index = start
#     pivot_ele = array[pivot_index]
#     i = pivot_index+1

#     for j in range(pivot_index+1, end):

#         if array[j] < pivot_ele:
#             array[i], array[j] = array[j], array[i]
#             i = i+1


#     array[pivot_index] , array[i-1] = array[i-1], array[pivot_index]

#     return i-1

# # The main function that implements QuickSort
# def quick_sort(start, end, array):

#     import pdb
#     pdb.set_trace()
#     if (start < end):

#         # p is partitioning index, array[p]
#         # is at right place
#         p = partition(start, end, array)

#         # Sort elements before partition
#         # and after partition
#         quick_sort(start, p - 1, array)
#         quick_sort(p + 1, end, array)

# # Driver code
# array = [3,7,8,2,1,4,9]
# quick_sort(0, len(array) - 1, array)

# print(f'Sorted array: {array}')


