# Intersection of two sorted Linked lists

"""
    method1:
        1) intiates temp1 and temp2 and new linklist
        2) traverse until temp1 and temp2 is none
        3) if temp1.data is greater than move to next node of temp2
        4) if temp2.data is greater than move to next node of temp1
        6) else insert temp1.data and temp1=temp1.next and temp2 = temp2.next

"""

def findIntersection(head1,head2):
    #return head

    temp1= head1
    temp2 = head2
    link = linkedList()

    while(temp1 != None and temp2 != None):

        if(temp1.data> temp2.data):
            temp2 = temp2.next

        elif(temp2.data>temp1.data):
            temp1 = temp1.next
        else:
            link.insert(temp1.data)
            temp1 = temp1.next
            temp2 = temp2.next


    return link.head
