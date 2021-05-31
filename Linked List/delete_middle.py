delete middle element in linkedlist


"""
1) if head is null or head.next is null return None
2) calculate length of link list
3) node = divide by // 2
4) while node > 0 traverse list
5) prev.next = temp.next
6) return head
"""


def length(head):
    count=0
    temp=head

    while(temp!= None):
        count = count+1
        temp = temp.next
    return count


def deleteMid(head):
    '''
    head:  head of given linkedList
    return: head of resultant llist
    '''

    if head==None or head.next==None:
        return None

    leng = length(head)
    node = leng//2
    prev = None
    temp = head
    while(node>0):
        prev = temp
        temp=temp.next
        node = node-1
    prev.next = temp.next

    return head
