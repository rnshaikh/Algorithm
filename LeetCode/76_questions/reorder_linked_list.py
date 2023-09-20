"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

"""

"""
    1) find out second half of list using slow and fast pointer slow = head and fast=head.next in every iter slow by 1 fast by 2

    2) the reverse second half of list

    3) first = head second = prev then now reorder list until second is not none



"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """


        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        second = slow.next
        first = head
        slow.next = None


        nex = None
        curr = second
        prev = None

        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex


        first = head
        second = prev

        while second:

            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


        return head













class Solution:
    
    
    def find_mid(self, node):
        
        curr = node
        step = node
        
        while step and step.next:
            curr = curr.next
            step = step.next.next
            
            
        return curr
    
    
    def reverse(self, node):
        
        curr = node
        prev = None
        nex = None
        
        while curr:
            
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        
        return prev
            
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        
        curr1 = head
        curr2 = head
        
        mid = self.find_mid(curr2)
        curr2 = self.reverse(mid.next)
        mid.next = None
        
        
        flag = True
        
        
        while curr1 and curr2:
            
            if flag:
                temp = curr1.next
                curr1.next = curr2
                curr1 = temp
            else:
                temp = curr2.next
                curr2.next = curr1
                curr2 = temp
            
            flag = not flag
    
        return head
        
        
        
                
            
    
            
            
        
        
        
        
        
        
        
