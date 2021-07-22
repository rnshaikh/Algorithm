


class Queue:

    def __init__(self):

        self.s1 = []
        self.s2 = []

    def isEmpty(self):
        if not len(self.s1):
            return True
        return False

    def enqueue(self, data):

        if not self.isEmpty():
            while(len(self.s1)>0):
                self.s2.append(self.s1[-1])
                self.s1.pop()

            self.s1.append(data)

            while(len(self.s2)>0):
                self.s1.append(self.s2[-1])
                self.s2.pop()
            return
        else:
            self.s1.append(data)

    def dequeue(self):

        if self.isEmpty():
            return -1

        data = self.s1.pop()
        return data


if __name__ == '__main__':

    qu = Queue()

    n = int(input("Enter A no element to pushed into Queue:"))

    while(n>0):
        ele = int(input("Enter A element to pushed into Queue:"))
        qu.enqueue(ele)
        n = n-1

    print("Is Empty:", qu.isEmpty())

    k = input("dequeue from queue (yes/Exit):")

    while k != 'Exit':
        print("dequeue eleement:", qu.dequeue())
        k = input(" dequeue from queue:")
