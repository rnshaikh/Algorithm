
# Largest subarray with 0 sum

"""
    logic if curr_sum of array while traversing  comes previously then there is some subarray with sum 0

    if curr_sum is 0 then sub_array with all previous element is one of the sub_array with length of array until that element

    if curr_element is 0 and max_length is 0 then it can be one subarray with length 1


    algo:
        curr_sum = 0 , max_len=0 , hash_sum =0

        for i in range(n):

            curr_sum = curr_sum + arr[i]
            if curr_ele = 0 and max_len = 0:
                max_len = 1

            if curr_sum is 0 then
                max_len = i+1  that  mean len subarray with these ele

            if curr_sum in hash_sum:
                max_len is max(max_len, differen between current index and  previous index)

            else:
                store curr_sum and index in hash_map

        return max_len

"""


def maxLen(n, arr):
    #Code here

    hash_sum = {}

    max_len = 0

    curr_sum = 0

    for i in range(n):

        curr_sum = curr_sum + arr[i]


        if arr[i] == 0 and max_len == 0:
            max_len = 1

        if curr_sum == 0:
            max_len = i + 1


        if curr_sum in hash_sum:

            max_len = max(max_len, i-hash_sum[curr_sum])

        else:
            hash_sum[curr_sum] = i

    return max_len
