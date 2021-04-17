
# method :
"""
    sort array
    num = 1
    traverse array
        if arr[i] != num
            return num
        num = num +1
    return no_of_ele
"""


def MissingNumber(array,n):
    # code here
    num = 1
    array.sort()
    for i in range(0,len(array)):

        if array[i] != num :
            return num
        num = num + 1

    return n
