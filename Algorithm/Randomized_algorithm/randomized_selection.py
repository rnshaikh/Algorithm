

# problem : we have get ith samllest number from unsorted order

"""
        one solution is reduced selection to sorting sort using merge sort then give it smallest
        number
        but running time for this algorithm is O(n log n) we can do better than tha


        second solution : used quick sort but in quick choos random pivot element which divide array into 25:75 list
        after we place pivot its rightful position than
        check if i == j return reurn j th element
        if j > i then  ith index will be on left part so send 1st part ofy array, j-1, ith index
        if j <i then ith index will on right side so send 2nd part, n-j , i-jth index


        in deterministic solution:
                we just choose pivot element as medians of median
                we divide array into 5 array of 5 element
                find out median of each array
                then find out median of median array
                choose that as pivot element
"""


import random


class selQuick:

    def divide(self, array, start, end, ith):
            if (start < end):
                p = self.partition(array, start, end, ith)
                return p

    def partition(self, array, start, end, ith):

        pivot_index = random.randint(start, end-1)
        pivot = array[pivot_index]

        i = pivot_index+1
        for j in range(pivot_index+1, end):

            if array[j] < pivot:
                array[i], array[j] = array[j], array[i]

                i = i+1

        array[i-1], array[pivot_index] = array[pivot_index], array[i-1]
        correct_pivot_index = i-1

        if correct_pivot_index == ith:
            return array[correct_pivot_index]

        if correct_pivot_index < ith:
            return self.partition(array[correct_pivot_index:end],
                           correct_pivot_index,end, ith-correct_pivot_index)

        if correct_pivot_index > ith:
            return self.partition(array[start:correct_pivot_index],start, correct_pivot_index, ith)



A = [9, 10, 5, 3, 100, 1]


ddio = selQuick()
print(ddio.divide(A, 0, len(A), 4))


