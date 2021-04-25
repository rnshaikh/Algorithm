# Product array puzzle


#find product except current element

"""
    1) remove all zero from list and calculate prod of new least
    2) calculate no of zero in list
    3) calculate total product of list without zero
    4) traers list if zero is more than 1 than all prod is 0
    5) if zero == 1 and i != 0 then product =0
    6) if zero == 1 and i==0 then product = prod of all
    7) else product = product/i

"""



#User function Template for python3
from operator import mul
from functools import reduce

def productExceptSelf(arr, n):
    #code here
    arr_2 = [i for i in arr if i != 0]

    zero = 0

    zero = len(arr) - len(arr_2)
    mul_a = reduce(mul, arr_2, 1)
    result = []

    for i in arr:

        if zero>1:
            result.append(0)
        elif zero==1 and i != 0:
            result.append(0)
        elif zero==1 and i==0:
            result.append(mul_a)
        else:
            result.append(int(mul_a/i))

    return result
