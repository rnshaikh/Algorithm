# insert element in sorted circular linked list


"""
    Method:1 :

    1) initialize temp = head, prev= None
    2) travese throught linked list to get last node as prev
    3) initialize temp= head again
    4) if temp.data is greater than given data then prev.next = new and new.next = temp and head = temp return head
    5) else traverse through linked list until temp.next != head
    6) check if temp.data > given data if greater then prev.next = new and new.next = temp return head
    7) for last nod check if temp.data > given if yes prev.next= new and new.next=temp return head

"""



class Solution:
    def sortedInsert(self, head, data):

        temp = head
        prev = None
        new = Node(data)

        while(temp.next != head):
            temp = temp.next

        prev = temp
        temp = head

        if temp.data>data:
            prev.next = new
            new.next = temp
            head = new
            return head

        while(temp.next != head):
            if temp.data > data:
                prev.next = new
                new.next = temp
                return head

            prev = temp
            temp = temp.next

        if temp.data>data:
            prev.next = new
            new.next = temp

        return head
