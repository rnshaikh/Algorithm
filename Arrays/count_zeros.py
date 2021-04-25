# Count the Zeros in array 0 followed by 1 [1,1,1,0,0]


"""
Method 1:
    1) initiate zero = 0
    2) traverse array from last to first
    3) check curr_ele != 1 increment zero else break;
    5) return zero


"""




class Solution:
    def countZeroes(self, arr, n):
        # code here

        m = n-1
        zero = 0
        for i in range(m, -1, -1):
            if arr[i] != 1:
                zero = zero+1
            else:
                break

        return zero
