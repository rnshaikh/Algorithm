# detect loop in linkedlist
"""
    1) start slow and fast with head
    loop till slow and fast and fast.next is not null
    2) slow = slow.next and fast = fast.next.next
    3) if both points to same return True
    4) return False
"""

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here

        slow = head
        fast = head

        while(slow != None and fast != None and fast.next != None):

            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False
