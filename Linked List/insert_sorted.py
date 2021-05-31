# insert in sorted linked list


"""
    1) intialize temp=head, prev = None
    3) if head is none new is head
    3) traverse through list until temp.data>key if yes prev.next = new and new.next=temp return head1
    4) if not in list that mean it is last element so prev.next = new return head1
"""

class Solution:
    def sortedInsert(self, head1,key):
        # code here
        # return head of edited linked list

        prev = None
        temp = head1
        new = Node(key)

        if temp==None:
            head1 = new
            return head

        while(temp != None):
            if temp.data>key:
                if prev == None:
                    new.next = temp
                    head1=new
                    return new

                prev.next = new
                new.next = temp
                return head1
            prev = temp
            temp = temp.next

        prev.next = new

        return head1
