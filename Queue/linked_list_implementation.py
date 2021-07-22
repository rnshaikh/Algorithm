

class Node:

    def __init__(self, data=None):

        self.data = data
        self.next = None



class Queue:

    def __init__(self, head=None):

        self.front = None
        self.rear = None


    def isEmpty(self):

        if self.front is None:
            return True
        return False

    def enqueue(self, data):

        node = Node(data)

        if self.isEmpty():
            self.front = node
            self.rear = node
            return

        self.rear.next = node
        self.rear = node

    def dequeue(self):

        if self.isEmpty():
            return -1

        node = self.front

        if self.front==self.rear:
            self.front = None
            self.rear = None
            return node.data

        self.front = self.front.next

        return node.data

    def get_front(self):

        if self.isEmpty():
            return -1

        return self.front.data

    def get_rear(self):

        if self.isEmpty():
            return -1

        return self.rear.data


if __name__ == '__main__':

    qu = Queue()

    n = int(input("Enter A no element to pushed into Queue:"))

    while(n>0):
        ele = int(input("Enter A element to pushed into Queue:"))
        qu.enqueue(ele)
        n = n-1

    y = int(input("front element(1/0):"))
    if y:
        print(qu.get_front())


    y = int(input("rear element(1/0):"))
    if y:
        print(qu.get_rear())

    print("Is Empty:", qu.isEmpty())

    k = input("dequeue from queue (yes/Exit):")

    while k != 'Exit':
        print("dequeue eleement:", qu.dequeue())
        qu.get_rear()
        k = input(" dequeue from queue:")
