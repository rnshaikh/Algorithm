# Sorted subsequence of size 3

# find 3 element in array such tha A[i] < A[j] < A[k]


"""
Method 1:

    1) Initiate min_num = A[0], max_num = 99999 , store_min=min
    2) traverse array and see if current element is min_num then continue, if current element < min_num update min_num continue,
    3) if current_element < max_num, update max_num = current_element, store_min = min_num
    4) el if current_elelemt > max_element then we found three num store_min < max_num < current_element


"""





class Solution:
    def find3number(self,A, n):
        # code here

        seq = 1
        min_num = A[0]

        max_num= 999999

        store_min = min_num

        for i in range(1, len(A)):

            if A[i] == min_num:

                continue

            elif A[i] < min_num:

                min_num = A[i]
                continue

            elif(A[i] < max_num):

                max_num = A[i]

                store_min = min_num

            elif(A[i]> max_num):

                seq = seq + 1

                return [store_min, max_num, A[i]]

                max_num = A[i]


        return []
