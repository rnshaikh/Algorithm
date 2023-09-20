
#Delete nodes having greater value on right

"""
Recusive:
    1) exit condtion if head.next == None
    2) goes to last two node ,  head , temp
    3) check if temp.data>head: retrun temp to its previous nod
    4) else link that node to head (previous node) head.next = temp
    5) return head to previous nod
    
    1) check if temp and temp.next is not None otherwise return head
    2) initate temp and prev
    3) traverse until temp.next is none
    4) check if temp.data<temp.next.data if yeas then check if prev is null if yes head = temp.next els prev.next = temp.next
    5) restart traverse from temp =head and prev=None
    6) prev= temp and temp=temp.next
"""




class Solution:
    def compute(self,head):
        #Your code here


        # if(head.next == None):
            #return head

        # temp = self.compute(head.next)
        # if temp.data> head.data:
        #     return temp
        # else:
        #     head.next = temp
        # return head

        temp = head
        prev = None

        if temp == None or temp.next == None:
            return head

        while(temp.next != None):

            if temp.data<temp.next.data:
                nex = temp.next
                if prev:
                    prev.next = nex

                else:
                    head = temp.next

                temp = head
                prev = None
                continue

            prev = temp
            temp = temp.next

        return head


