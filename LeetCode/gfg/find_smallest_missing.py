"""
    Given a sorted array of n distinct integers where each integer is in the range from 0 to m-1 and m > n. Find the smallest number that is missing from the array.

    Input: {0, 1, 2, 6, 9}, n = 5, m = 10
    Output: 3

    Input: {4, 5, 10, 11}, n = 4, m = 12
    Output: 0

"""

"""
    using binary search we can solved it in O(log n) time

    if binary search
    if start > end: then missing element is end+1

    if a[start] != a[start]:
        return start

    mid = calculate mid

    if mid ele and index is equal:
        then search in right part
    else:
        search in left part


"""




def find_smallest_mission_element(array, start, end):

    if start > end:
        return end+1

    if array[start] != start:
        return start

    mid = (start+end) // 2


    if array[mid] == mid:
        return self.find_smallest_mission_element(array, mid, end)

    return self.find_smallest_mission_element(array, start, mid)



