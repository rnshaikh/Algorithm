


class Node:

    def __init__(self, data, next=None):

        self.data = data
        self.next = next


class Stack:

    def __init__(self, head=None):

        self.head = head

    def isEmpty(self):

        if not self.head :
            return True
        else:
            return False

    def push(self, data):

        node = Node(data)

        if not self.head:
            self.head = node
            return

        node.next = self.head
        self.head = node

    def pop(self):

        if (self.isEmpty()):
            return -1
        else:
            temp = self.head
            self.head = self.head.next
            return temp.data

    def peek(self):

        if(self.isEmpty()):
            return -1
        else:
            return self.head.data


if __name__== '__main__':

    st = Stack()
    n = int(input("Enter A no element to pushed into stack:"))

    while(n>0):
        ele = int(input("Enter A element to pushed into stack:"))
        st.push(ele)
        n = n-1

    y = int(input("peek element(1/0):"))
    if y:
        print(st.peek())

    print("Is Empty:", st.isEmpty())

    k = input("pop from stack (yes/Exit):")
    while k != 'Exit':
        print("Pop eleement:", st.pop())
        st.peek()
        k = input(" pop from stack:")
