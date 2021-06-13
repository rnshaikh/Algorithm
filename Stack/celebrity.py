# Find Celebrity problem:

"""
    1) take variable cel = False , ind=0, count=0
    2) traverse list
    3) check if all element is zero then cele=True, ind=i, count=+1
    4) if cele and count==1 return True else False
"""


"""
    1) take two pointer i = 0 , j=n-1
    2) if M[i][j] == 1 increase i else j-1 until (i<j)
    3) travese list againe check i is known by every one M[k][i] != 1 return -1
    4) return i

"""


class Solution:

    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here
        cele = False
        ind = 0
        count = 0
        for i in range(0,n):
            if not any(M[i]):
                cele =True
                ind = i
                count = count+1


        if cele and count==1:
            return ind
        else:
            return -1
