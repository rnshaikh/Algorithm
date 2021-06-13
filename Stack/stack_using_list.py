



class Stack:

    def __init__(self):

        self.stack = []

    def push(self, element):

        self.stack.append(element)

    def pop(self):

        if len(self.stack)<=0:
            return -1

        return self.stack.pop()

    def isEmpty(self):

        if len(self.stack)<=0:
            return True
        return False

    def peek(self):

        if len(self.stack)<=0:
            return -1

        return self.stack[-1]


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
