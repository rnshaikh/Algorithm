# Merge two sorted list in 3rd

"""
    1) intialize temp1=head1 and temp2=head2 and link =LinkedList()
    2) traverse through both list until one of them is None
    3) if temp1.data > temp2.data insert in new list and temp2=temp2.next
    4) if temp2.data> temp1.data insert temp1 and temp1=temp1.next
    6) els insert both and increment both
    7) check if temp2 is not none then insert his element in new list
    8) check if temp2 is not none then insert his element in new list
"""



def sortedMerge(head1, head2):
    # code here

    temp1 = head1
    temp2 = head2

    link = LinkedList()

    while(temp1!=None and temp2 != None):

        if temp1.data>temp2.data:
            link.append(temp2.data)
            temp2=temp2.next
        elif temp2.data>temp1.data:
            link.append(temp1.data)
            temp1 = temp1.next
        else:
            link.append(temp1.data)
            link.append(temp2.data)
            temp1=temp1.next
            temp2=temp2.next

    if temp1!=None:
        while(temp1!=None):
            link.append(temp1.data)
            temp1=temp1.next

    if temp2!=None:
        while(temp2!=None):
            link.append(temp2.data)
            temp2 = temp2.next

    return link.head
