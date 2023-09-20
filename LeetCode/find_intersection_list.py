"""
    Given the heads of two singly linked-lists headA and headB, 
    return the node at which the two lists intersect. 
    If the two linked lists have no intersection at all, return null.
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




class Solution:
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        
        point1 = headA
        point2 = headB
        
        while point1 != point2:
            
            point1 = point1.next
            point2 = point2.next
        
            if point1 == point2:
                return point1
            
            if not point1:
                point1 = headB
            
            if not point2:
                point2 = headA
        
        return point1
    