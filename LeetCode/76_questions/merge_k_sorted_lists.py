from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, [lists[i].val, i])
        
        dummy = ListNode()
        head = dummy

        while len(heap):
            val, index = heappop(heap)
            nex = lists[index].next
            dummy.next = lists[index]
            dummy = dummy.next
            if nex:
                heappush(heap, [nex.val, index])
                lists[index] = nex
        return head.next

            

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        head1 = list1
        head2 = list2
        
        if not head1:
            return list2
        
        if not head2:
            return list1
        
        nhead = ListNode()
        temp = nhead
        while head1 and head2:
            if head1.val <= head2.val:                
                nex = head1.next
                temp.next = head1
                head1 = nex
                temp = temp.next
                
            else:
                nex = head2.next
                temp.next = head2
                head2 = nex
                temp = temp.next

        while head1:
            nex = head1.next
            temp.next = head1
            temp = temp.next
            head1 = nex

        while head2:
            nex = head2.next
            temp.next = head2
            temp = temp.next
            head2 = nex
        return nhead.next
        