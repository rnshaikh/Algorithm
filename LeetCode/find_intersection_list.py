"""
    Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
"""


class Solution:


    def check_inter(self, small, large):

        temp_s = small
        temp_l = large
        li = set()
        while(temp_s != None):
            li.add(temp_s)
            temp_s = temp_s.next

        while(temp_l != None):
            if temp_l in li:
                return temp_l
            temp_l = temp_l.next
        return


    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        node = self.check_inter(headA, headB)

        if node :
            return node

        return None
