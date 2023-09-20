"""
NumPy is one of the most popular, easy-to-use, versatile, open-source, 
python-based, general-purpose package that is used for processing arrays. 
NumPy is short for NUMerical PYthon. This is very famous for its highly optimized tools that
 result in high performance and powerful N-Dimensional array processing feature that is 
 designed explicitly to work on complex arrays. 

"""

import time
import numpy as np

"""
Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )


"""

"""
to delete 1st column 
"""
import numpy as np
#inputs
inputArray = np.array([[35,53,63],[72,12,22],[43,84,56]])
new_col = np.array([[20,30,40]])
# delete 2nd column
arr = np.delete(inputArray , 1, axis = 1)
#insert new_col to array
arr = np.insert(arr , 1, new_col, axis = 1)
print (arr)



arr = [i for i in range(1, 10)]

arr1 = np.array(arr)

print("data type of numpy array", type(arr1))
print("length of array", len(arr1))
print("data type of element", arr1.dtype)

int_arr = np.array([1,2,3,4,5], dtype='i8')
print("Data type of integer array", int_arr.dtype)

print("\n\n\n")

print("""
  slicing 
return subarray with start:end:step
negative index allow

""")

print("slice 1 : 4: 2", arr1, arr1[:4:2])

print("\n\n\n")

print("""
 copy vs view

 copy is deep copy and view is shallow copy
""")

ex_arr = np.array([1,2,3,4,5])
copy_arr = ex_arr.copy()
view_arr = ex_arr.view()

copy_arr[0]=10
print("copy array after update", copy_arr)
print("original arr after update", ex_arr)

view_arr[0]=10
print("original array after update", ex_arr)
print("view array after update", view_arr)

print("\n\n\n")

print("""
shape is number of element in each dimensions

""")
arr_d = np.array([1,2,3,4], ndmin=3)
print("3d array", arr_d, arr_d.shape)

print("\n\n\n")


print("""
reshaping means adding, removing dimensions or chaning number of element in each dimensions.
reshaping return view
""")

arr_d = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("reshape 2d array", arr_d.reshape(4,3))
print("reshape 3d array",arr_d.reshape(2,3,2))
print("check reshap is view or copy", arr_d.reshape(2, 6).base)


print("\n\n\n")

print(
"""
    joining  
    conactenate array default axis=0 merging axis=1 concatenating by rows

    stack is similiar to concatenate but uses new axis to stack element on one another

"""
)

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print("concatenate1 on axis =0", np.concatenate((arr1, arr2)))


arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])
print("concatenate1 on axis =1", np.concatenate((arr1, arr2), axis=1))

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])

print("stack axis=0", np.stack((arr1, arr2)))
print("stack axis=1", np.stack((arr1, arr2), axis=1))
print("stack on rows", np.hstack((arr1, arr2)))
print("stack on col", np.vstack((arr1, arr2)))
print("stack on depth", np.dstack((arr1, arr2)))


print("\n\n\n")

print("""
splitting : splits array into given parts

""")

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print("split into 4 parts", newarr)


arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print("split 2d array into 3 parts", newarr)



arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print("split 2d array into 3 parts on col", newarr)


print("\n\n\n")

print("""
searching : return array indexes where value is present

""")

arr = np.array([1, 2, 3, 4, 5])
x = np.where(arr == 4)
print("index array where 4 is present", x)



arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print("find indexes where values are even", x)


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 1)
print("find indexes where values are odd", x)

"""
There is a method called searchsorted() which performs a binary search in the array, 
and returns the index where the specified value would be inserted to maintain the search order.

The searchsorted() method is assumed to be used on sorted arrays.

"""
arr = np.array([6, 8, 9, 7])
x = np.searchsorted(arr, 7)
print("index of 7 in sorted array", x)



print(""" sorting : np.sort()  return new array""")
arr = np.array([[3, 2, 4], [5, 0, 1]])
print("sorted array", np.sort(arr))
print("sorted by col", arr.view('i4,i4,i4').sort(order=['f0'], axis=0), arr)


x = np.random.randint(100)
print("randonm int from 0 to 100", x)

x = np.random.rand()
print("random float from 0 to 1", x)


from numpy import random

x=random.randint(100, size=(5))
print("random 1d array within 100 number with size 5", x)



from numpy import random
x = random.randint(100, size=(3, 5))
print("random 2d array within 100 number with row 3 and col 5", x)



"""

ufuncs stands for "Universal Functions" and they are NumPy functions that operate on the ndarray object.

"""

import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)



def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print("UFUNCY", myadd([1, 2, 3, 4], [5, 6, 7, 8]))


