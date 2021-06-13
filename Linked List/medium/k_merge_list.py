#Function to merge K sorted linked list.

"""
    1) take list
    2) traverse each list store node in list
    3) sort list
    4) add each element in list in linkedlist
    5) return head
"""


class Solution:
    #Function to merge K sorted linked list.
    def mergeKLists(self,arr,K):
        # code here
        # return head of merged list

        array = list()
        link = LinkedList()

        for i in range(len(arr)):

            temp = arr[i]

            while(temp != None):
                array.append(temp.data)
                temp = temp.next

        array.sort()
        for i in array:
            link.add(i)

        return link.head




