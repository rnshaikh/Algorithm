
#6->5->4->3->2->1->


class Node:

    def __init__(self, data, prev=None, next=None):

        self.data = data
        self.prev = prev
        self.next = next


class DLL:

    def __init__(self, head=None, mid=None, count=0):

        self.head = head
        self.mid = None
        self.count = count

    def push(self, data):

        node = Node(data)

        node.prev = None

        if self.head == None:
            self.head = node
            self.count = self.count+1
            self.mid = node
            return

        node.next = self.head
        self.head.prev = node
        self.count = self.count + 1

        if self.count == 1:
            self.mid = node
        else:

            if self.count % 2 != 0:
                self.mid = self.mid.prev
        self.head = node

    def pop(self):

        if self.count==0:
            return -1

        data = self.head.data
        newhead = self.head.next

        if not newhead:
            self.head = None
            self.count = self.count-1
            self.mid = None
            return data

        newhead.prev = None

        self.head = newhead
        self.count = self.count-1

        if self.count %2 == 0:
            self.mid = self.mid.next
        return data

    def findmid(self):
        if self.count == 0:
            return -1
        return self.mid.data

    def deletemid(self):

        if self.count == 0:
            return -1

        mid = self.mid

        mid_next = self.mid.next
        mid_prev = self.mid.prev

        mid_prev.next = mid_next
        mid_next.prev = mid_prev

        self.count = self.count-1

        if self.count % 2 == 0:
            self.mid = mid_next
        else:
            self.mid = mid_prev

        return mid.data


if __name__== '__main__':

    st = DLL()
    n = int(input("Enter A no element to pushed into stack:"))

    while(n>0):
        ele = int(input("Enter A element to pushed into stack:"))
        st.push(ele)
        n = n-1

    y = int(input("mid element(1/0):"))
    if y:
        print(st.findmid())

    y = int(input("delete mid element(1/0):"))
    if y:
        print(st.deletemid())

    k = input("pop from stack (yes/Exit):")
    while k != 'Exit':
        print("Pop eleement:", st.pop())
        print("mid:", st.findmid())
        k = input(" pop from stack:")







