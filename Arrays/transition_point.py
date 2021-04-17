

# find tranistion point : return index when 1 started retrun -1 if no 1 return 0 if no 0 in array of 0,1



def transitionPoint(arr, n):
    zero = 0
    for i in range(0, n):
        if arr[i] == 1:
            return i
        if arr[i] == 0:
            zero = zero + 1
            continue

    if zero== 0:
        return 0

    return -1
