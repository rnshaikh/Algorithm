
#Function to check whether the list is palindrome.

"""
    method :
    1) create stack and all data into stack from head
    2) while stack is not empty. pop element from stack and check if its same as with list
    3) if not return 0 else increment temp = temp.next continue
    4) whole stack get empty return 1
"""

"""
    without stack
    1) reverse linked list intialize new head fast
    2) traverse linked list from start checked data with reverse linked list if its requal continue else return 0
    3) if whole list is traverse return 1
"""




from collections import deque


class Solution:
    def isPalindrome(self, head):
        #code here

        temp = head
        stack = deque()

        while temp != None:

            stack.append(temp.data)
            temp = temp.next

        temp = head
        while stack:
            da = stack.pop()
            if temp.data == da:
                temp = temp.next
                continue
            else:
                return 0

        return 1
