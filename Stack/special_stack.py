# Your task is to complete all these function's
# function should append an element on to the stack
# find minimum element in stack





def push(arr, ele):
    # Code here
    arr.append(ele)



# Function should pop an element from stack
def pop(arr):
    # Code here

    if isEmpty(arr):
        return -1

    ele = arr.pop()
    return ele

# function should return 1/0 or True/False
def isFull(n, arr):
    # Code her

    if len(arr)>=n:
        return True
    else:
        return False

# function should return 1/0 or True/False
def isEmpty(arr):
    #Code here

    if len(arr)>=0:
        return True
    else:
        return False


# function should return minimum element from the stack
def getMin(n, arr):
    # Code here

    min_q = 999999999

    for a in arr:
        if a<min_q:
            min_q = a
    return min_q

