from collections import defaultdict


class Graph:

    def __init__(self, v):

        self.v = v
        self.graph = defaultdict(list)


    def add_edge(self, u, v):

        self.graph[u].append(v)
        self.graph[v].append(u)


    def bfs(self, start_vertex, visited):

        queue = []
        component = []

        queue.append(start_vertex)
        component.append(start_vertex)
        visited[start_vertex] = True

        while(len(queue)):

            ver = queue.pop(0)
            for i in self.graph[ver]:
                if visited[i] == False:
                    queue.append(i)
                    component.append(i)
                    visited[i] = True
        return component

    def find_connected_component(self):

        visited = [False] * self.v
        component = []

        for i in range(self.v):
            if visited[i] == False:
                comp = self.bfs(i, visited)
                if comp:
                    component.append(comp)

        print("Connected component:", component)


if __name__ == "__main__":

    n = int(input("Enter no of vertex:"))
    gr = Graph(n)

    ch = int(input("Enter no of choice: \n 1.Add Edge \n 2.Find Connected component \n 3.Exit."))

    while(ch):

        if ch==1:
            ver_str = input("Enter vertices between edge (space separated):")
            u, v = ver_str.split(" ")
            u, v = int(u) , int(v)
            gr.add_edge(u, v)

        if ch==2:
            gr.find_connected_component()

        if ch==3:
            print("Good Bye !!")
            break

        ch = int(input("Enter no of choice: \n 1.Add Edge \n 2.Find Connected component \n 3.Exit."))







