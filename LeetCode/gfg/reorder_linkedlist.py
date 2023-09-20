"""
Given a singly linked list: A0→A1→…→An-1→An, reorder it to: A0→An→A1→An-1→A2→An-2→…
For example: Given 1->2->3->4->5 its reorder is 1->5->2->4->3.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

"""

"""

    we can do this simply using array storing all nodes in it
    then taking to pointer create list
    but it will have space complexity O(n)

    other solution is
    divide then list in middle
    reverse the all elements after mid  in curr2

    i = True
    while(Curr2) is not none

        if i is true append element from curr1

        else:
            append element from curr2
"""




def get_mid(temp):

    curr = temp
    step = temp

    while(step and step.next != None):

        curr = curr.next
        step = step.next.next
    return curr

def reverse(temp):

    prev = None
    curr = temp
    nex  = None

    while(curr != None):

        nex = curr.next
        curr.next = prev
        prev = curr
        curr = nex

    return prev




def reorderList(self):

    if (self.head==None or self.head.next==None):
        return

    # li_node = []
    # temp = self.head
    # while(temp != None):
    #     li_node.append(temp)
    #     temp = temp.next

    # i = 1
    # k = 1
    # j = len(li_node) - 1
    # temp = self.head
    # while(i < j):
    #     if k % 2 == 0:
    #         temp.next = li_node[i]
    #         temp = temp.next
    #         i = i + 1
    #         k = k + 1
    #     else:
    #         temp.next = li_node[j]
    #         temp = temp.next
    #         j = j -1
    #         k = k + 1

    # if i == j:
    #     temp.next = li_node[i]
    #     temp = temp.next
    #     temp.next = None

    curr1 = self.head
    mid = get_mid(self.head)

    curr2 = mid.next
    curr2 = reverse(curr2)

    mid.next = None

    curr1 = self.head
    i = True
    while(curr2 != None):

        if i:
            temp= curr1.next
            curr1.next = curr2
            curr1 = temp
        else:
            temp = curr2.next
            curr2.next = curr1
            curr2 = temp

        i = not i





class Solution:
    
    def find_mid(self, node):
        
        curr = node
        step = node
        
        while step and step.next:
            
            curr = curr.next
            step = step.next.next
        
        return curr
        
        
    def reverse(self, node):
        
        prev = None
        curr = node
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
        mid = self.find_mid(curr1)
        
        curr2 = mid.next
        curr2 = self.reverse(curr2) 
        mid.next  = None
        
        
        i = True
        
        
        while curr1 and curr2:
            
            if i:
                temp = curr1.next
                curr1.next = curr2
                curr1 = temp
            else:
                temp = curr2.next
                curr2.next = curr1
                curr2 = temp
            
            i = not i
