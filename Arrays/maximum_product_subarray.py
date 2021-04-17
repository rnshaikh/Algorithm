# maximum product of sub array

"""
    metod: kandane's algorithm + max_mum product can be obatined by minimum product of previous elements multiplied by current element

    initalize max_ending_here, min_ending_here =1, flag=0, max_so_far=0

    traverse every element of array:

        if element > 0:
            max_ending_here = max_ending_here * element
            min_ending_here = min(min_ending_here*element, 1)
            flag=1

        elif element == 0
            max_ending_here , min_ending_here =1

        else:
            temp = max_ending_here
            max_ending_here = max(min_ending_here*element, 1)
            min_ending_here = temp* element

        max_so_far < max_ending_here:
            max_so_far = max_ending_here


    if max_so_far== 0 and flag==0:
            return max_so_far
    retrun max_so_far


ex.

max_ending_here = 1
min_ending_here = 1


max_so_far = 0
flag = 0

{12, 2, -3, -5, -6, -2}



i= 0 arr[i] = 12

12>0:
    max_ending_here = max_ending_here * 12  = 12
    min_ending_here = min(12,1) 1
    flag = 1

    max_so_far = 12

i=1  arr[i] = 2 max_ending_here=12, min_ending_here=1, max_so_far = 12

  2>0:
    max_ending_here = max_ending_here*2 = 24
    min_ending_here = min(24,1) = 1
    flag=1

    max_so_far =24



i=2  arr[i] = -3  max_ending_here=24, min_ending_here=1, max_so_far = 24

    -3<0:
        temp = 24
        max_ending_here  = max(1*-3, 1) = 1
        min_ending_here = 24* -3 = -72

    max_so_far = 24

i=3  arr[i] = -5  max_ending_here=1, min_ending_here=-72, max_so_far = 24

    -5<0:
        temp = 1
        max_ending_here = max(-72*-5, 1) = 360
        min_ending_here = 1*-5 = -5

    max_so_far = 360

i=4  arr[i] = -6  max_ending_here=360, min_ending_here=-5, max_so_far = 360

    -6 < 0:
        temp = 360
        max_ending_here = max(-5*-6, 1) = 30
        min_ending_here = 360*-6 = -2160

    max_so_far = 360

i=5  arr[i] = -2  max_ending_here=30, min_ending_here=-2160, max_so_far = 360


    -2 < 0:
        temp = 30
        max_ending_here = max(-2160*-2, 1) = 4320
        min_ending_here = 30* -2 = -60

    max_so_far = 4320





"""




#User function Template for python3
class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self,arr, n):
        # code here

        max_ending_here = 1
        min_ending_here = 1

        max_so_far = 0
        flag= 0

        for i in range(0, n):

            if arr[i]>0:

                max_ending_here = max_ending_here * arr[i]
                min_ending_here = min(min_ending_here*arr[i], 1)
                flag=1

            elif arr[i] == 0:
                max_ending_here = 1
                min_ending_here = 1

            else:
                temp = max_ending_here
                max_ending_here = max(min_ending_here*arr[i], 1)
                min_ending_here = temp * arr[i]


            if max_so_far < max_ending_here:
                max_so_far = max_ending_here


        if flag==0 and max_so_far == 0:
            return max_so_far

        return max_so_far
