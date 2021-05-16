

class Node:

    def __init__(self, data, nex=None):

        self.data = data
        self.next = nex


class CLL:

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):

        node = Node(data)

        if self.head == None:

            self.head = node
            self.head.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = node
        node.next = self.head
        return

    def push(self, data):

        node = Node(data)
        temp = self.head

        while(temp.next != self.head):
            temp = temp.next

        node.next = self.head
        self.head = node
        temp.next = self.head

    def insert_before(self, data, ele):

        node = Node(data)
        temp = self.head

        if temp.data == ele:
            self.push(data)
            return

        while(temp.next != self.head):
            if temp.data == ele:
                break

            prev = temp
            temp = temp.next

        if temp == None:
            return

        if temp.data == ele:
            prev.next = node
            node.next = temp
            return
        prev.next = node
        node.next = temp
        return

    def display(self):

        temp = self.head

        print(temp.data)
        temp = temp.next

        while temp != self.head:
            print(temp.data)
            temp = temp.next

    def delete(self, data):

        temp = self.head

        if temp.data == data:
            last = temp.next
            while last.next != self.head:
                last = last.next

            self.head = temp.next
            last.next = self.head
            return

        while temp.next != self.head:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        if temp.data == data:
            prev.next = temp.next

        prev.next = temp.next

    def length(self):

        count = 0
        temp =self.head
        while temp.next != self.head:
            count = count+1
            temp = temp.next

        count = count+1
        print("Length: ", count)


if __name__ == '__main__':

    cll = CLL()
    n = int(input("Enter no of nodes:"))

    while n > 0:

        x = int(input("Enter a data:"))
        cll.insert(x)
        n = n-1

    cll.display()

    x = int(input("Enter data to be deleted:"))

    cll.delete(x)
    cll.display()

    cll.length()

    x = int(input("Enter data to be pushed:"))
    cll.push(x)
    cll.display()


    x = int(input("Enter data to be insert:"))
    y = int(input("Enter element to insert before:"))
    cll.insert_before(x, y)
    cll.display()



