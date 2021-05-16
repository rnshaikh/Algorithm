#Function to add two numbers represented by linked list. create linked list of sum


"""
    Method :
        1) intialize sum1 and sum2 string
        2) traverse fist linked list stored data into sum1
        3) traverse second list stored data into sum2
        4) convert sum1 and sum2 into int and add it into sum_l convert sum_l to string
        5) traverse char into sum_l convert to into create linked_list
        6) return head of new linked_list

"""


class Solution:

    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        first_sum = ''
        secon_sum = ''
        temp1 = first
        temp2 = second

        while(temp1 != None):
            first_sum = first_sum + str(temp1.data)
            temp1 = temp1.next

        while(temp2 != None):
            secon_sum = secon_sum + str(temp2.data)
            temp2 = temp2.next

        first_sum = int(first_sum)
        secon_sum = int(secon_sum)

        sum_l = first_sum + secon_sum
        sum_l = str(sum_l)

        LL2 = LinkedList()
        for i in sum_l:
            i = int(i)
            LL2.insert(i)
        return LL2.head
