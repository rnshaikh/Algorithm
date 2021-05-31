# Remove loop in linked list

"""
1) intialize set
2) temp = head , prev=None
3) traverse through list until temp is not None
3) if temp in set break
4) els add temp in set and prev=temp and temp.next
5) if temp==None no loop return head
5) prev.next = None return head
"""



class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes

        lis = set()
        temp = head
        prev = None
        while(temp != None):
            if temp in lis:
                break
            lis.add(temp)
            prev = temp
            temp = temp.next

        if temp == None:
            return head

        prev.next = None
        return head
