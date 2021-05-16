#Function to remove duplicates from sorted linked list.

"""
    method:
        1) initialize prev = head and temp=head.next
        2) traverse until temp is not None
        3) temp.data == prev.data then update prev.next = temp.next , temp=prev.next countinue
        4) else prev= temp, temp = temp.next
"""


def removeDuplicates(head):
    #code here

    temp = head.next
    prev = head

    while (temp != None):
        if temp.data == prev.data:
            prev.next = temp.next
            temp = prev.next
            continue
        prev = temp
        temp = temp.next
