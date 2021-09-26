

# Kosaraju algorithm

"""
        first we have to find correct ordering vertex according to its finnishing time
        vertex whose finnish last in dfs

        then after finding finishing order we do dfs on vertex according to decreasing order of finish time



        1) take stack and visited
        2) loop though vertex apply dfs and push vertex in to stack when its finnish
        3) transpose graph or reverse graph edges
        4) take visited
        5) while stack is not empty do dfs append it in connected component.
        6) return connected component

"""

from collections import defaultdict

class Graph:

    def __init__(self, v):

        self.graph = defaultdict(list)
        self.v =v
        self.component = []

    def add_edge(self, u, v):

        self.graph[u].append(v)

    def dfs_util(self, ver, gr, visited):

        visited[ver] = True
        self.component.append(ver)

        for i in gr[ver]:
            if visited[i] == False:
                self.dfs_util(i,gr,visited)


    def dfs_finish(self, ver, visited, stack):

        visited[ver] = True

        for i in self.graph[ver]:
            if visited[i] == False:
                self.dfs_finish(i, visited, stack)

        stack.append(ver)


    def transpose(self):

        g = [[] for i in range(self.v)]
        for i in range(self.v):
            for j in self.graph[i]:
                g[j].append(i)

        return g

    def connected_component(self):

        visited = [False] * self.v
        stack = []

        for i in range(self.v):
            if visited[i] == False:
                self.dfs_finish(i, visited, stack)

        visited = [False] * self.v
        gr = self.transpose()
        count = 0
        component = []

        while(len(stack)):

            ver = stack.pop(-1)
            if visited[ver] == False:
                self.dfs_util(ver, gr, visited)
                component.append(self.component)
                self.component = []
                count = count+1

        return count, component


if __name__ == "__main__":

    n = int(input("Enter no of vertex:"))
    gr = Graph(n)

    ch = int(input("Enter no of choice: \n 1.Add Edge \n 2.Find strongly Connected component \n 3.Exit."))

    while(ch):

        if ch==1:
            ver_str = input("Enter vertices between edge (space separated):")
            u, v = ver_str.split(" ")
            u, v = int(u) , int(v)
            gr.add_edge(u, v)

        if ch==2:
            print(gr.connected_component())

        if ch==3:
            print("Good Bye !!")
            break

        ch = int(input("Enter no of choice: \n 1.Add Edge \n 2.Find strongly Connected component \n 3.Exit."))
















