class Solution:

    #Function to detect cycle in an undirected graph.

    def cycleUtil(self, i, adj, visited, parent):

        visited[i] = True
        for j in adj[i]:

            if(visited[j] == False):
                if(self.cycleUtil(j,adj,visited,i)):
                    return True
            elif (j != parent):
                return True

        return False

    def isCycle(self, V, adj):
        #Code here

        visited = [False] * V
        for i in range(V):
            if (visited[i]==False):
                if (self.cycleUtil(i, adj, visited, -1)):
                    return 1

        return 0
