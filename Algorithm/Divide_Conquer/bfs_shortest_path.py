from collections import defaultdict


class Graph:

    def __init__(self, v):
        self.graph = defaultdict(list)
        self.V = v

    def add_edge(self, u, v):

        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs_shortes_path(self, start_ver):

        visited = [False] * self.V
        short_path = [float('inf')] * self.V
        queue = []

        queue.append(start_ver)
        visited[start_ver] = True
        short_path[start_ver] = 0

        while(len(queue)):

            vertex = queue.pop(0)
            for i in self.graph[vertex]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    short_path[i] = short_path[vertex] + 1
        print(short_path)


if __name__ == "__main__":

    n = int(input("Enter no of vertex:"))
    gr = Graph(n)

    ch = int(input("Enter no of choice: \n 1.Add Edge \n 2.Find Shortest Path \n 3.Exit."))

    while(ch):

        if ch==1:
            ver_str = input("Enter vertices between edge (space separated):")
            u, v = ver_str.split(" ")
            u, v = int(u) , int(v)
            gr.add_edge(u, v)

        if ch==2:
            ver = int(input("Enter a vertex from you find shortest path:"))
            print("Shortest path from given vertex:")
            gr.bfs_shortes_path(ver)

        if ch==3:
            print("Good Bye !!")
            break

        ch = int(input("Enter no of choice: \n 1.Add Edge \n 2.Find Shortest Path \n 3.Exit."))

