
"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        num_1 = ""
        num_2 = ""

        temp1 = l1
        while(temp1 != None):
            num_1 = num_1 + str(temp1.val)
            temp1 = temp1.next

        temp2 = l2
        while(temp2 != None):
            num_2 = num_2 + str(temp2.val)
            temp2 = temp2.next

        num1_reverse = ""
        len_1 = len(num_1)-1
        while(len_1>=0):
            num1_reverse = num1_reverse + num_1[len_1]
            len_1 = len_1 -1

        num2_reverse = ""
        len_2 = len(num_2) - 1
        while(len_2 >= 0):
            num2_reverse = num2_reverse + num_2[len_2]
            len_2 = len_2 - 1

        ans = int(num1_reverse) + int(num2_reverse)
        ans = str(ans)
        ans_l = len(ans)-1
        ans_rev = ""
        while ans_l>=0 :
            ans_rev = ans_rev + ans[ans_l]
            ans_l = ans_l - 1

        prev_node = None
        head = None
        for i in ans_rev:
            node = ListNode(i, None)
            if prev_node:
                prev_node.next = node
                prev_node = node
            else:
                prev_node = node
                head = node

        return head
