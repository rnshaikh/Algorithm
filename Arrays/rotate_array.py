
#Rotate array by  counter clock wise by D

#method 1:
# stored first d element in temporary array
# stored remaining element in new array
# append two temp to new array


class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self,A,D,N):
        #Your code here
        last_array = A[D:] + A[:D]
        A.clear()
        A.extend(last_array)
