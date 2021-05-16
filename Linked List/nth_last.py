#Function to find the data of nth node from the end of a linked list


"""
    method :
        count length of list
        then if n is greater than count return -1
        calculate diff = count - n
        traverse linked list from head and decrement diff by 1 until it is greater than 0
        return temp.data
"""



def getNthFromLast(head,n):
    #code here

    count = 0
    temp = head
    while(temp != None):
        count = count + 1
        temp = temp.next

    if n>count:
        return -1

    diff = count - n
    temp = head
    while diff>0:
        temp = temp.next
        diff = diff -1

    return temp.data
