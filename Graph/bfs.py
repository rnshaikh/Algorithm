
from collections import defaultdict


"""
    1) take 1 node from graph as start node
    2) take queue and visited array for tracking visited node
    3) append 1st node in queue and marked vistied[node] = true
    4) traverse until queue is not empty
    5) dequeu node from queue print it traverse its adjacent node check if it is already visited if not then append in queue and marked visited=True
"""



class Graph:

    def __init__(self):
        self.graph = defaultdict(list)


    def add_edge(self, u, v):

        self.graph[u].append(v)
        self.graph[v].append(u)

        print(graph)

    def BFS(self):

        visited = [False] * (max(self.graph) + 1)

        queue = []

        for i in self.graph:
            start = i
            break

        queue.append(start)
        visited[i] = True
        while(len(queue)):

            ver = queue.pop(0)
            print(ver)

            for i in self.graph[ver]:

                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


if __name__ == '__main__':

    graph = Graph()

    k = int(input("""Enter one of the below option :
                    1) Insert
                    2) BFS
                    3)Exit"""))

    while(True):

        if k == 1:
            a,b = input("Enter edge between 2 vertices:").split(" ")
            a = int(a)
            b = int(b)
            graph.add_edge(a,b)

        if k == 2:
            graph.BFS()

        if k == 3:
            print("Good Bye!!!")
            break;

        k = int(input("""Enter one of the below option :
                    1) Insert
                    2) BFS
                    3)Exit"""))

