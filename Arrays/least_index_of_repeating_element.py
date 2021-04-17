#Function to return the position of the first repeating element.


"""
    Method 1:
        1) initiate hash and least_index with {}, 9999
        2) if element present in hash and its index less than least index update least_index
        3) else add element and its index+1 in hash
        4) if least_index is not equal to 999 then return least_index else -1
"""

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):

        #arr : given array
        #n : size of the array

        hash_arr = {}
        least_index = 999

        for i in range(n):

            if arr[i] in hash_arr and least_index>hash_arr[arr[i]]:
                least_index = hash_arr[arr[i]]


            hash_arr[arr[i]] = i+1

        if least_index != 999:
            return least_index

        return -1
