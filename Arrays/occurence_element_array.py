# count occurence of element from 1 to N

"""
method :
    intiate array from 0 to n-1 with 0

    traverse elment of array:
        update occurance of element at i  by 1    if i=0  4 is present then in has a[4-1] is increment by 1 beacause hase stored element 1 to 5


"""


class Solution:

    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencycount(self,A,N):
        # code here


        hash_mp = [0 for i in range(N)]

        # Traverse all array elements
        i = 0

        while (i < N):

            # Update the frequency of array[i]
            hash_mp[A[i] - 1] += 1

            # Increase the index
            i += 1

        A.clear()
        A.extend(hash_mp)
