# Key Pair

"""
    Method : sort and two-pointer technique

    1) sort array . take point on initial number and last number
    2) if sum is greater than x then decrement last pointer if it is less increment first pointer.

"""


#User function Template for python3
class Solution:
    def hasArrayTwoCandidates(self,arr, n, x):
        # code here

        for i in range(0, n):
            for j in range(i, n):
                if i == j:
                    continue
                if arr[i]+arr[j] == x:
                    return True

        return False
