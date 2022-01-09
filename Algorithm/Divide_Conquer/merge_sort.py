


class MergeSort:


    def __init__(self):

        pass

    def divide(self, array):

        if len(array)>1:

            mid = len(array)//2

            left = array[:mid]
            right = array[mid:]

            # print("left", left)
            # print("right", right)
            self.divide(left)
            self.divide(right)
            self.conquer_merge(array, left, right)
            print("result", array]]])

    def conquer_merge(self, array, left, right):

        i = 0
        j = 0
        k = 0

        print("array, left, right", array, left, right)

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                array[k] = left[i]
                i = i+1
                k = k+1

            else:
                array[k] = right[j]
                j = j+1
                k = k+1

        while i < len(left):
            array[k] = left[i]
            i = i+1
            k = k+1

        while j < len(right):
            array[k] = right[j]
            j = j+1
            k = k+1


if __name__ == "__main__":

    sort = MergeSort()

    li = [12,5,6,7,8,9,1,100]
    sort.divide(li)
