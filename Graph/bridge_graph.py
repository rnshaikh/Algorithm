
# Bridge Edge in Graph

"""
    Given an undirected graph of V vertices and E edges and another edge (c-d), 
    the task is to find if the given edge is a bridge in graph, i.e., removing the edge disconnects the graph.
"""

"""
    deter mine if edge is removed c and d from graph if all vetex is visible

    1) remove vertex c and d and d and c from graph
    2) call dfs with from vertex c
    3) after dfs check if d in visited == False return 1 else 0

"""

class Solution:

    #Function to find if the given edge is a bridge in graph.

    def dfs_util(self, ver, adj, visited):

        visited[ver] = True

        for i in adj[ver]:
            if visited[i] == False:
                self.dfs_util(i, adj, visited)



    def isBridge(self, V, adj, c, d):
        # code here

        visited = [False] * V

        if d in adj[c]:
            adj[c].remove(d)

        if c in adj[d]:
            adj[d].remove(c)

        self.dfs_util(c, adj, visited)

        if visited[d]==False:
            return 1
        else:
            return 0
