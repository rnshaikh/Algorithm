# find mid element

"""
    1) initalize count = 0
    2) traerse list until node is none and increment count by 1
    3) divide count by 2 in n
    4) traverse list from start and decrement n by 1 until it is greater than 0
    5) return temp.data
"""

# function should return index to the any valid peak element
def findMid(head):
    # Code here
    # return the value stored in the middle node

    count = 0
    temp = head

    while(temp != None):
        count = count + 1
        temp = temp.next

    n = int(count/2)
    temp = head
    while n > 0:
        temp = temp.next
        n = n-1
    return temp.data
