




class Node:

    def __init__(self, data, node):

        self.data = data
        self.next = node


class Linked_list():

    def __init__(self, head=None):

        self.head = head


    def push(self, x):

        node = Node(x, None)
        node.next = self.head
        self.head = node
        return


    def insert_after(self, x, ele):

        node = Node(x, None)

        temp = self.head

        while(temp != None):

            if temp.data == ele:
                break
            temp = temp.next

        if temp != None:
            node.next = temp.next
            temp.next = node
            return
        print("Not Found...")


    def insert(self, data):

        node = Node(data, None)

        if not self.head:
            self.head = node
            return

        temp = self.head

        while temp.next != None:
            temp = temp.next

        temp.next = node

    def display(self):

        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next

    def search(self, x):

        temp = self.head

        while temp != None:

            if temp.data == x:
                print(temp.data)
                return

            temp = temp.next

        print(-1)

    def delete(self, x):

        temp = self.head

        if temp.data == x:
            self.head = temp.next
            return

        while temp != None:
            if temp.data == x:
                break
            previous = temp
            temp = temp.next

        if temp == None:
            return

        previous.next = temp.next

    def length(self):

        node = self.head
        count = 0

        while(node != None):
            count = count + 1
            node = node.next

        print("Length of Linked list is :", count)

    def length_rec(self, node, count):

        if node == None:
            return count
        else:
            count = count + 1
            return self.length_rec(node.next, count)


if __name__=='__main__':

    no_of_node = int(input("Enter No of node:"))

    linked_list = Linked_list()

    while no_of_node > 0:

        data = int(input("Enter Data:"))

        linked_list.insert(data)

        no_of_node = no_of_node - 1

    linked_list.display()

    x = int(raw_input("Enter element to be searched:"))

    linked_list.search(x)

    x = int(raw_input("Enter element to be delete:"))

    linked_list.delete(x)
    linked_list.display()


    x = int(input("Element to be pushed :" ))

    linked_list.push(x)
    linked_list.display()


    x = int(input("Element to be inserted :" ))
    y = int(input("Element inserted after :"))

    linked_list.insert_after(x,y)
    linked_list.display()

    linked_list.length()
    count = linked_list.length_rec(linked_list.head, 0)
    print("Length of linked list recursive:", count)


