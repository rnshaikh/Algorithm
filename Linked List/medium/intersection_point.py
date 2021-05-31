#Intersection Point in Y Shapped Linked Lists

"""
    Method:
        1) intitialize set, temp1=head1 and temp2=head2
        2) traverse through 1st list and store in set
        3) then traverse through 2nd list and check if node is present in set if yeas return data
        4) return -1

"""


def intersetPoint(head1,head2):
    #code here

    lis = set()
    temp1 = head1
    while(temp1!=None):
        lis.add(temp1)
        temp1 = temp1.next

    temp2 = head2
    while(temp2!=None):
        if temp2 in lis:
            return temp2.data
        temp2=temp2.next

    return -1
