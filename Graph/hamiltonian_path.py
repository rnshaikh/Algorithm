# check if hamiltonian path exist or not


"""
    1) visited list, create adj list representation
    2) loop through vertex check if visited = false call dfs with cnt=1
    3) in dfs cnt == N return True
    4) for adj vertex of current vertex call dfs with cnt+1 if it True return True
    5) else mark current vertex == False return False
"""


from collections import defaultdict
class Solution:

    def dfs_util(self,ver,N,adj, visited, cnt):
        if cnt == N:
            return True
        visited[ver] = True
        for i in adj[ver]:
            if visited[i] == False:
                if(self.dfs_util(i, N, adj, visited, cnt+1))==True:
                    return True

        visited[ver]=False
        return False

    def check(self, N, M, Edges):
        #code here

        adj = defaultdict(list)
        visited = [False] * (N+1)
        recur_stack = [False] * N

        for i in Edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])

        for i in range(1, (N+1)):
            if(self.dfs_util(i,N,adj, visited, 1)) == True:
                return 1

        return 0
