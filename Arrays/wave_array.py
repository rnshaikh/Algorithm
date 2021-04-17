# Convert Sorted Array in to wave like array lexigographical order



"""
    method 1:
        travers array if array element is not last then
            index is even:
                then check if element is greater than next if not :
                    swap current, next element


"""




class Solution:
    #Complete this function
    #Function to sort the array into a wave-like array.
    def convertToWave(self,A,N):
        #Your code here

        for i in range(0,len(A)):

            if i%2 == 0:
                if i != N-1:
                    if A[i]< A[i+1]:
                        A[i], A[i+1] = A[i+1], A[i]
                        continue
