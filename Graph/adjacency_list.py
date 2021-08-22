



class Node:

    def __init__(self, data, next=None):

        self.data = data
        self.next = next



class Graph:

    def __init__(self, v):

        self.V = v
        self.graph = [0]*v

    def add_edge(self, src, dest):

        root = self.graph[src]

        node = Node(dest)
        if not root:
            self.graph[src] = node
        else:
            while root.next != None:
                root = root.next
            root.next = node

        root_des = self.graph[dest]
        node = Node(src)
        if not root_des:
            self.graph[dest] = node
        else:
            while root_des.next != None:
                root_des = root_des.next

            root_des.next = node

    def print_graph(self):

        for i in range(len(self.graph)):

            print("Vertices of %s as follows:" %(i))

            temp = self.graph[i]
            while(temp!=None):
                print("vertex: ", temp.data)
                temp=temp.next


if __name__ == '__main__':

    n  = int(input("Enter no of vetices:"))
    graph = Graph(n)

    k = int(input("""Enter one of the below option :
                    1) Insert
                    2) Print
                    3)Exit"""))

    while(True):

        if k == 1:
            a,b = input("Enter edge between 2 vertices:").split(" ")
            a = int(a)
            b = int(b)
            graph.add_edge(a,b)

        if k == 2:
            graph.print_graph()

        if k == 3:
            print("Good Bye!!!")
            break;


        k = int(input("""Enter one of the below option :
                    1) Insert
                    2) Print
                    3)Exit"""))

