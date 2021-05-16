
class Node:

    def __init__(self, data=None, prev=None, nex=None):


        self.data = data
        self.prev = prev
        self.next = nex


class DLL():

    def __init__(self, head=None):

        self.head = head

    def append(self, data):

        node = Node(data)
        if self.head == None:
            self.head = node
            return

        temp = self.head
        while temp.next != None:

            temp = temp.next

        temp.next = node
        node.prev = temp

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_after(self, data, ele):

        node = Node(data)
        temp = self.head

        while(temp != None):

            if temp.data == ele and temp.next != None:
                next_ele = temp.next
                node.prev = temp
                node.next = next_ele
                next_ele.prev= node
                temp.next = node
                return

            if temp.data == ele and temp.next == None:
                temp.next = node
                node.prev = temp
                return
            temp = temp.next

        print("Not Found:")

    def insert_before(self, data, ele):

        node = Node(data)
        temp = self.head

        if self.head.data == ele:
            temp.prev = node
            node.next = temp
            self.head = node
            return

        while temp != None:

            if temp.data == ele:
                prev_node = temp.prev
                node.next = temp
                temp.prev = node
                node.prev = prev_node
                prev_node.next = node
                return

            temp = temp.next

    def delete(self, ele):

        temp = self.head

        if self.head.data == ele:
            node = self.head.next
            node.prev = None
            self.head = node
            return

        while temp != None:

            if temp.data == ele:
                break
            temp = temp.next

        if temp == None:
            print("Not Found")
            return

        if temp.next != None:
            next_node = temp.next
            prev_node = temp.prev

            prev_node.next = next_node
            next_node.prev = prev_node
            return
        prev_node = temp.prev
        prev_node.next = None
        return

    def display(self):

        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next

    def display_reverse(self):

        temp = self.head
        while(temp.next != None):
            temp = temp.next

        while temp != None:
            print(temp.data)
            temp = temp.prev

    def length(self):

        temp = self.head
        count = 0
        while temp != None:
            count = count +1
            temp = temp.next

        print("Length:", count)
        return


if __name__ == '__main__':

    n = int(input("Enter No Of node : "))
    dll = DLL()

    while n > 0:
        d = int(input("Enter a data: "))
        dll.append(d)
        n = n - 1

    dll.display()

    print("Print in Reverse:")
    dll.display_reverse()

    d = int(input("Push element :"))
    dll.push(d)
    dll.display()

    x = int(input("Element to be insert: "))
    y = int(input("Element insert after :"))
    dll.insert_after(x,y)
    dll.display()
    print("Print in Reverse:")
    dll.display_reverse()

    x = int(input("Element to be insert: "))
    y = int(input("Element insert before :"))
    dll.insert_before(x,y)
    dll.display()
    print("Print in Reverse:")
    dll.display_reverse()

    dll.length()

    x = int(input("Element to be deleted: "))
    dll.delete(x)
    dll.display()
    print("Print in Reverse:")
    dll.display_reverse()


    x = int(input("Element to be deleted: "))
    dll.delete(x)
    dll.display()
    print("Print in Reverse:")
    dll.display_reverse()

    x = int(input("Element to be deleted: "))
    dll.delete(x)
    dll.display()
    print("Print in Reverse:")
    dll.display_reverse()

