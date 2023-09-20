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

    new = ListNode()
    nhead = new
    
    while list1 and list2:
        
        if list1.val <= list2.val:
            nex1 = list1.next
            
            nhead.next = list1
            nhead = nhead.next
            nhead.next = None
            list1 = nex1
            
            
        else:
            nex2 = list2.next
            
            nhead.next = list2
            nhead = nhead.next
            nhead.next = None
            
            list2 = nex2
            
            
    while list1:
        nex1 = list1.next
            
        nhead.next = list1
        nhead = nhead.next
        nhead.next = None
            
        list1 = nex1
    
    
    while list2:
        
        nex2 = list2.next

        nhead.next = list2
        nhead = nhead.next
        nhead.next = None

        list2 = nex2
        
    return new.next
