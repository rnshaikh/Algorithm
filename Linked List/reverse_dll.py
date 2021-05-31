# reverse dll


"""
    1) intialize curr=head, prev = head.prev , nex=None
    2)  traerse until curr is not None
    3) nex = curr.next, prev = curr.prev
    4) curr.next = prev, curr.prev=nex
    5) prev = curr and curr = next

"""

def reverseDLL(head):
    #return head after reversing

    curr = head
    prev = None
    nex = None

    while(curr != None):
        nex = curr.next
        prev = curr.prev

        curr.next = prev
        curr.prev = nex

        prev = curr
        curr=nex

    head=prev
    return head
