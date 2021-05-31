# #Function to rotate a linked list.

"""
Method1:
    1) intialize count=k, temp=head, list=[]
    2) traverse list until k>0  and add node in list
    3) check if temp == None return head
    4) set new head head=temp newtemp = head
    5) traverse untile newtemp.next is none for getting last node
    6) traverse throug list and update node.next=None, newtemp.next=node, newtemp=node
    7) return head
"""



class Solution:

    #Function to rotate a linked list.
    def rotate_counter(self,head):

        temp = head
        head = temp.next
        temp.next = None
        new = head
        while(new.next != None):
            new = new.next
        new.next = temp
        return head

    def rotate(self, head, k):
        # code here
        # while k>0:
        #     head=self.rotate_counter(head)
        #     k = k-1
        # return head
        count = k
        temp = head
        lis = []
        while(count>0):
            lis.append(temp)
            temp = temp.next
            count = count-1


        if temp == None:
            return head

        head = temp
        newtemp = head
        while(newtemp.next!=None):
            newtemp = newtemp.next

        for node in lis:
            node.next=None
            newtemp.next = node
            newtemp = node

        return head
