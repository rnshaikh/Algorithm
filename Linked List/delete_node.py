#Function to delete a node without any reference to head pointer.

"""
    method :
        1) first traverse list update node.data with next node.data unitl node.next is not null
        2) then update address of current with next node until temp.next.next is not null
        3) at last node  update temp.next = None

"""


class Solution:
    def deleteNode(self,curr_node):
        #code here

        temp = curr_node
        while(temp.next != None):
            temp.data = temp.next.data
            temp = temp.next
        temp = curr_node
        while temp.next.next != None:
            temp = temp.next

        temp.next = None
