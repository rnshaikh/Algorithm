
"""
    stongly connected component = any vertex have path from any other vertex
"""

"""
    1) it required two dfs
    2) take stack in first dfs stored vertex in stack in dfs order
    3) reverse graph or transpose it
    4) take visited
    5) until stack is empty
    6) pop vertex from stack apply dfs on vertex and transpose graph
    7) increment count
    8) return count
"""





class Solution:

    #Function to find number of strongly connected components in the graph.

    def dfs(self, v, adj, visited):

        visited[v]=True
        for i in adj[v]:
            if visited[i] == False:
                self.dfs(i, adj, visited)



    def sfc(self, v, adj, visited, stack):

        visited[v] = True

        for i in adj[v]:
            if visited[i] == False:
                self.sfc(i, adj, visited, stack)

        stack = stack.append(v)

    def transpose(self, V, adj):
        g = [[] for i in range(V)]
        for i in range(V):
            for j in adj[i]:
                g[j].append(i)
        return g


    def kosaraju(self, V, adj):
        # code here
        visited = [False] * V
        stack = []
        for i in range(V):
            if visited[i] == False:
                self.sfc(i, adj, visited, stack)
        g = self.transpose(V, adj)
        visited = [False] * V
        count = 0
        while len(stack):
            v = stack.pop()
            if visited[v]==False:
                self.dfs(v,g, visited)
                count = count +1

        return count
