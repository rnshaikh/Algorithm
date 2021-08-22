

class Graph:

    def __init__(self, v):
        self.gr = [[0]*v for _ in range(v)]

    def insert(self, src, dest):
        self.gr[src][dest] = 1
        self.gr[dest][src] = 1

    def display(self):

        print(self.gr)
        for i in range(len(self.gr)):
            print("Adjacent vertices of %s vertex :" %(i))
            for j in range(len(self.gr[i])):
                if self.gr[i][j] == 1:
                    print("vertex: %s" %(j))


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
            graph.insert(a,b)

        if k == 2:
            graph.display()

        if k == 3:
            print("Good Bye!!!")
            break;


        k = int(input("""Enter one of the below option :
                    1) Insert
                    2) Print
                    3)Exit"""))
