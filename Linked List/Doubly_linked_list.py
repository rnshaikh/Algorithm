


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

            if temp.data == ele:
                next_ele = temp.next
                node.prev = temp
                node.next = next_ele
                next_ele.prev= node
                temp.next = node
                return

            temp = temp.next

        print("Not Found:")

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
