
from collections import defaultdict


class Graph:

    def __init__(self, V):

        self.graph = defaultdict(list)
        self.V = V


    def insert(self, u, v):

        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self):

        queue = []
        visited = [False]*self.V

        start = 0
        visited[0] = True
        queue.append(start)

        while len(queue):

            node = queue.pop(0)
            print(node)
            for i in self.graph[node]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


    def dfs_util(self, node, visited):

        visited[node] = True
        print(node)
        for i in self.graph[node]:
            if visited[i] == False:
                self.dfs_util(i, visited)


    def dfs(self):

        visited = [False] * self.V

        start = 0

        self.dfs_util(start, visited)



if __name__ =="__main__":


    n = int(input("Enter number of Vertex:"))

    gr = Graph(n)

    ch = int(input("Enter you choice:\n 1) Insert edge \n 2)BFS \n 3)DFS \n 4) Exit"))

    while(ch):

        if ch == 1:
            n = input("Enter Edge between 2 vertex space seprated:")
            n, m = n.split(" ")
            n, m = int(n), int(m)
            gr.insert(n, m)

        if ch == 2:
            print("BFS of graph as follows:")
            gr.bfs()

        if ch == 3:
            print("DFS of graph as follows:")
            gr.dfs()

        if ch == 4:
            print("good bye!!!")
            break

        ch = int(input("Enter you choice:\n 1) Insert edge \n 2)BFS \n 3)DFS \n 4) Exit"))

