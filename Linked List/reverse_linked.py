

"""
    method 1: iterative:

    1) initialize current= head, prev, nex = None
    2) iterate until current != None:
    3)  set = next =current.next, current.next =prev, prev = current, current=nex
    4) update head = prev
    5) return head

"""


class Solution:
    #Function to reverse a linked list.

    def reverseList(self, head):
        # Code here

        current = head
        prev = None
        nex = None

        while(current != None):
            nex = current.next
            current.next = prev
            prev = current
            current = nex

        head = prev
        return head


"""
    method = recursive
    1) define recur func wuth p, head
    3) exit counditon if p.next == None then update head = p
    3) call recur function with p.next, head
    5) set q = p.next
    6) q.next = p
    7) p.next = None

"""

class Solution:
    #Function to reverse a linked list.
       def recur(self, head):
        
        if not head or not head.next:  # for 0 and 1 node linkelist
            return head
        
        new_head = self.recur(head.next)
        p = head.next  #for 2 node linked list
        p.next = head
        head.next = None
        return new_head
        
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        head = self.recur(head)
        return head
