#User function Template for python3

#Function to return the count of the number of elements in
#the intersection of two arrays.


"""
method:
    1) intiate count=0 , duplicate_element=0
    3) traverse array which is less in length
    4) check if current ele is in another array and it is not already in duplicate_element
    5) if yes then increment count
    6) return count

"""


class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        #return: expected length of the intersection array.

        #code here

        count = 0
        duplicate_element = []
        if n<m:

            for i in range(n):
                if a[i] in b and a[i] not in duplicate_element:
                    count = count + 1
                    duplicate_element.append(a[i])

        else:

            for j in range(m):
                if b[j] in a and b[j] not in duplicate_element:
                    count = count + 1
                    duplicate_element.append(b[j])

        return count
