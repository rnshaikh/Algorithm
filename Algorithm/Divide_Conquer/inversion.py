# calculate inversion count : inversion is when at i, j index in array i < j  if array[i]> array[j] then that is one inversion

"""
    use divide and conquer merge sort:
    at time of merge if element in left is greater that element in right copy that element in array update 
    inversion_count = count+ len(left[i:])
"""



class Inversion:

    def __init__(self):
        self.inverison_count = 0

    def divide(self, array):

        if len(array)>1:

            m  = len(array)//2
            left = array[:m]
            right = array[m:]

            self.divide(left)
            self.divide(right)
            count = self.merge_inversion(array, left,right)
            return count


    def merge_inversion(self, array, left, right):

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):

            if left[i]> right[j]:

                array[k] = right[j]
                k = k+1
                j = j+1
                self.inverison_count = self.inverison_count + len(left[i:])
            else:
                array[k] = left[i]
                i = i+1
                k = k+1

        while i < len(left):
            array[k] = left[i]
            i = i+1
            k = k+1

        while j < len(right):
            array[k] = right[j]
            j = j+1
            k = k+1

        return self.inverison_count


if __name__ == "__main__":

    inv = Inversion()

    li = [12,5,13,7,8,9,20,100]
    print(inv.divide(li))
