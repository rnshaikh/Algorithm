# equilibrium point find index where left half element sum == right half element sum

"""
    METHDO 1 :

        1) find out all sum of all element in list as right_sum
        2) intialize left_sum = 0
        3) traverse element of array
        4) remove current element from right_sum
        5) if right_sum == left_sum return index
        6) add current_element in left_sum


"""

# Your task is to ocomplete this function
# Function should return an integer

def findEquilibrium(a,n):
    # Code here


    right_sum = 0

    for i in range(n):

        right_sum = right_sum + a[i]


    left_sum = 0

    for i in range(n):

        right_sum = right_sum-a[i]

        if(right_sum == left_sum):
            return i

        left_sum = left_sum + a[i]


    return -1
