class Solution:

    #Function to detect cycle using DSU in an undirected graph.
	
	
	def get_leader(self, leader, i):
        if leader[i] != i:
            leader[i] = self.get_leader(leader, leader[i])
        return leader[i]	
	
	def union(self, leader, rank, u, v):
        if rank[u] > rank[v]:
            leader[v] = u
	    elif rank[v] > rank[u]:
            leader[u] = v
        else:
            leader[v] = u
            rank[u] += 1

	def detectCycle(self, V, adj):
		#Code here
        edges = []
        hash_map = {}
		
        for i in range(len(adj)):
            for j in adj[i]:
                if (i, j) not in hash_map and (j,i) not in hash_map:
                    edges.append([i, j])
                    hash_map[(i, j)] = 1
                    hash_map[(j, i)] = 1
        
        rank = [0] * V
        leader = [0] * V
        
        for i in range(V):
            leader[i] = i
            
            
        for i in range(len(edges)):
            
            u, v = edges[i][0], edges[i][1]
            x, y = self.get_leader(leader, u), self.get_leader(leader, v)
            
            if x != y:
                self.union(leader, rank, x, y)
            else:
                return 1
        return 0