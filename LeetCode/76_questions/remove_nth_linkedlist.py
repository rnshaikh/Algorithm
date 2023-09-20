#Remove Nth Node From End of List



"""
    add dummy node
    left, right point should heave distence n
    until right is none update left and right
    then delet left.next node
    return dummy.next


"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


#         count = 0

#         temp = head
#         while(temp):
#             count = count+1
#             temp = temp.next



#         rem_node = (count-n)
#         #print("rem_node", rem_node)
#         cnt = 0
#         temp = head

#         if rem_node == 0:
#             head = head.next
#             return head

#         while temp:
#             cnt= cnt+1
#             if cnt == rem_node:
#                 #print("temp", temp.val)
#                 temp.next = temp.next.next
#                 break
#             temp = temp.next



#         return head


        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n >0 and right:
            right = right.next
            n = n-1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next

