"""
Given a singly linked list, the task is to rearrange it in a way that all odd position nodes are together and all even positions node are together.
Assume the first element to be at position 1 followed by second element at position 2 and so on.

"""

"""
    1,2,3,4,5

initialize = a=1, b=2, bhead=2

1 iter = a.next = b.next  ,  1,3,4,5  a=1,b=2,bhead=2
         a= a.next,  1,3,4,5   a=3, b=2, bhead=2
         b.next = a.next      1,3,4,5   2,4,5  a=3, b=2, bhead=2
         b = b.next           1,3,4,5   2,4,5  a=3  b=4  bhead=2

2 iter = a.next = b.next    1,3,5     2,4,5  a=3, b=4 bhead=2
         a= a.next          1,3,5     2,4,5   a=5, b=4 bhead=2
         b.next = a.next    1,3,5     2,4,None  a=5, b=4 bhead=2
         b = b.next         1,3,5,   2,4,None  a=5, b=None, bhead=2

    a.next = bhead     1,3,5,2,4,None


"""


class Solution:
    def rearrangeEvenOdd(self, head):
        #code here

        a=head
        b=head.next
        bhead = head.next

        while(a and b and a.next and b.next):
            a.next = b.next
            a = a.next
            b.next = a.next
            b = b.next


        if b:
            b.next = None
        a.next =bhead

        return head
