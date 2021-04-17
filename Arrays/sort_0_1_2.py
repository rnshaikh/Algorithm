

"""
method 1:
    thre count 0 , 1, 2 increment if element 0, 1, 2

    push 0 into arr until 0 count is 0
    push 1 into arr uniil 1 count is 0
    push 2 into arr until 2 count is 0

"""


class Solution:
    def sort012(self,arr,n):
        # code here

        zero_arr = 0
        one_arr = 0
        two_arr = 0

        for i in range(0, n):
            if arr[i] == 0:
                zero_arr= zero_arr + 1
                continue
            if arr[i] == 1:
                one_arr = one_arr + 1
                continue
            if arr[i] == 2:
                two_arr = two_arr + 1
                continue

        i = 0

        while zero_arr>0:
            arr[i] = 0
            i = i+1
            zero_arr = zero_arr -1

        while one_arr > 0:
            arr[i] = 1
            i = i +1
            one_arr = one_arr - 1

        while two_arr > 0:
            arr[i] = 2
            i = i + 1
            two_arr = two_arr -1



"""
method 2:

    three variable lo, mid , hi, 0, 0, n-1

    repeat unitl mid <= hi
        if ar[mid] == 0
            swap with arr[lo], arr[mid] = arr[mid], arr[lo]
            increment mid by 1
            increment low by 1

        if arr[mid] == 1
            increment mid by 1

        if arr[mid] == 2:
            swap arr[mid] with arr[hi]
            decrement hi by 1

"""



class Solution:
    def sort012(self,arr,n):
        # code here
        lo = 0
        hi = n - 1
        mid = 0
        while mid <= hi:
            if arr[mid] == 0:
                arr[lo], arr[mid] = arr[mid], arr[lo]
                lo = lo + 1
                mid = mid + 1
            elif arr[mid] == 1:
                mid = mid + 1
            else:
                arr[mid], arr[hi] = arr[hi], arr[mid]
                hi = hi - 1
        return arr














