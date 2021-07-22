


class Queue:

    def __init__(self, front=None, rear=None):

        self.q = []
        self.front = front
        self.rear = rear

    def isEmpty(self):

        if not len(self.q):
            return True
        return False

    def enqueue(self, data):

        if self.isEmpty():
            self.q.append(data)
            self.front = 0
            self.rear = 0
            return

        self.q.append(data)
        self.rear = self.rear + 1

    def dequeue(self):

        if self.isEmpty():
            return -1

        ele = self.q.pop(self.front)
        self.rear = self.rear-1

        return ele

    def get_fron(self):
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def get_rear(self):
        if self.isEmpty():
            return -1
        return self.q[self.rear]


if __name__ == '__main__':

    qu = Queue()

    n = int(input("Enter A no element to pushed into Queue:"))

    while(n>0):
        ele = int(input("Enter A element to pushed into Queue:"))
        qu.enqueue(ele)
        n = n-1

    y = int(input("front element(1/0):"))
    if y:
        print(qu.get_fron())


    y = int(input("rear element(1/0):"))
    if y:
        print(qu.get_rear())

    print("Is Empty:", qu.isEmpty())

    k = input("dequeue from queue (yes/Exit):")

    while k != 'Exit':
        print("dequeue eleement:", qu.dequeue())
        qu.get_rear()
        k = input(" dequeue from queue:")


