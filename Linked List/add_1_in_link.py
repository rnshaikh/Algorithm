
#Add 1 to a number represented as linked list

"""
    Method 1 :
        1) start st ='' temp = head
        2) traverse linked list until temp not none append data in str
        3) add 1 in int(str)
        4) start temp = head, i=0, num = string(num)
        5) traverse until temp.next is not none
        6) update temp.data = num[i] and i = i+1
        7) last node update temp.data =num[i] and i=i+1
        8) if len(num) is >= i+1 then create new node update data = num[i] and i=i+1
        9) return head
"""


class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        st = ''
        temp = head
        while(temp != None):
            st = st + str(temp.data)
            temp = temp.next

        num = int(st) + 1
        temp = head
        num = str(num)
        i = 0
        while(temp.next is not None):
            temp.data = num[i]
            temp = temp.next
            i = i+1


        temp.data = num[i]
        i = i+1
        while len(num) >= i+1:
            new = Node(num[i])
            temp.next = new
            i = i+1

        return head
