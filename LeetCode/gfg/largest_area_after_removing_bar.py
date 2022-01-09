#  Largest area possible after removal of a series of horizontal & vertical bars

"""
Given a grid consisting of horizontal & vertical bars of size (N + 2) x (M + 2) and two arrays H[]
and V[] denoting the number of horizontal & vertical bars required to be removed, the task is to find the largest area when a series of vertical and horizontal bars are removed.

Input: N = 3, M = 3, H[] = {2}, V[] = {2}
Output: 4
Explanation:
There are 3 bars in horizontal as well as vertical direction.

"""


"""
    algorithm
    intialize two sets horizontal bar and vertical_bar with from 1 to n+1 and from 1 to m+1 element

    then iterate through h array:
        remove given bar in h from horizontal bars set

    iterate throguh v array:
        remove given bar in v from vertiacal bars set


    convert horizontal bar set into list
    convert veritical basr set into list

    then find max_horizontal_diff  from horizontal_bar
    find max_vertical_diff from vertical_bar

    return product of max_horizontal_diff * max_vertical_diff


it smiliar cutting cak in horizontally and vertically and finding largest area of cut

"""

