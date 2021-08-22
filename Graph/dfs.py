from collections import defaultdict



class Graph:

    def __init__(self):

        self.graph = defaultdict(list)
        self.v = 0

    def add_edge(self, u, v):

        self.graph[u].append(v)
        #self.graph[v].append(u)

    def dfs_util(self, i, visited):

        visited[i] = True
        for adj in self.graph[i]:
            if visited[adj] == False:
                self.dfs_util(adj, visited)

    def dfs(self):
        visited = [False] * (max(self.graph)+1)
        for i in self.graph:
            start = 2
            break

        self.dfs_util(start, visited)

    def find_mother(self):

        visited = [False] * (self.v)
        v = 0
        for i in range(self.v):
            if visited[i] == False:
                self.dfs_util(i, visited)
                v = i

        visited = [False] * (self.v)
        self.dfs_util(v, visited)
        if any(i==False for i in visited):
            return -1
        else:
            return v


if __name__ == '__main__':

    graph = Graph()

    v = int(input("""Enter no of vertex: """))
    graph.v = v
    k = int(input("""Enter one of the below option :
                    1) Insert
                    2) DFS
                    3) Find Mother Vertex
                    4)Exit"""))

    while(True):

        if k == 1:
            a,b = input("Enter edge between 2 vertices:").split(" ")
            a = int(a)
            b = int(b)
            graph.add_edge(a,b)

        if k == 2:
            graph.dfs()

        if k == 4:
            print("Good Bye!!!")
            break;
        if k == 3:
            print(graph.find_mother())


        k = int(input("""Enter one of the below option :
                    1) Insert
                    2) DFS
                    3) Find Mother Vertex
                    4)Exit"""))



