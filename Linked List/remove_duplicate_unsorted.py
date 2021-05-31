#Function to remove duplicates from unsorted linked list.

"""
    Method 1 :
        1) initalize prev = None curr=head, lis=[]
        2) traverse until curr is not none
        3) if curr.data in list the prev.next = curr.next and curr= curr.next
        4) insert data in list and prev = curr


"""


class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list

        prev = None
        curr = head
        lis = []
        #count = 0
        while(curr != None):
            if curr.data in lis:
                prev.next = curr.next
                curr = curr.next
                continue

            lis.append(curr.data)
            #count = count + 1
            prev = curr

        # if count == 1:
        #     head.next = None

        return head
