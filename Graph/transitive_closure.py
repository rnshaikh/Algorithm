from collections import defaultdict
"""
Given a directed graph, find out if a vertex j is reachable from another vertex i for all vertex pairs (i, j) in the given graph. 
Here reachable mean that there is a path from vertex i to j. The reach-ability matrix is called the transitive closure of a graph.
"""


"""
    1) transitive closure matrix chech if v is reachable from vertex u for every parir of vertex.
    2) initialize matrix tr_res
    3) for each vertex call dfs with i, i
    4) if if u and v is if same if it is in adjalist marked 1 in transitive res
    5) else tr_res marked 1
    6) travere through adjacent list of v  check if u, i is already 1 in transitive matrix if not call dfs for (u, i)
    7) print transitive matrix

"""


class Graph:

    def __init__(self, n):
        self.V = n
        self.graph = defaultdict(list)
        self.tr_res = [0] * self.V
        for i in range(self.V):
            self.tr_res[i] = [0] * self.V

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, u, v):

        if u == v:
            if v in self.graph[u]:
                self.tr_res [u][u] = 1
        else:
            self.tr_res[u][v] = 1

        for i in self.graph[v]:
            if self.tr_res[u][i] != 1:
                self.dfs_util(u, i)

    def transitive_closure(self):

        for i in range(self.V):
            self.dfs_util(i, i)



if __name__ == "__main__":

    n  = int(input("Enter no of vertices:"))
    graph = Graph(n)

    ch = int(input("Enert ypur choice: 1) add edge \n 2) transitive_closure  \n 3)Exit"))

    while(True):

        if ch==1:
            u, v  = input("Enter edge between 2 vetex:").split(" ")
            u = int(u)
            v = int(v)
            graph.add_edge(u, v)

        if ch == 2:

            graph.transitive_closure()
            print(graph.tr_res)

        if ch ==3:
            print("Good Bye !!!")
            break

        ch = int(input("Enert ypur choice: 1) add edge \n 2) transitive_closure  \n 3)Exit"))


