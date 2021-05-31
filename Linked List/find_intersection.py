# find intersection of two list


"""
Method:1
    1) create new linke list and set
    2) traerse 2nd list sotre in set
    3) traverse 1st list check if data in set if yes insert into new linked list
    4) return head of new linked list

"""




class Solution:
    def findIntersection(self, head1, head2):
        # code here
        # return head of intersection list

        link = linkedList()
        temp2 = head2
        lis = set()
        while(temp2 != None):
            lis.add(temp2.data)
            temp2=temp2.next

        temp1 = head1
        while(temp1 != None):
            if temp1.data in lis:
                link.insert(temp1.data)
            temp1=temp1.next
        return link.head
