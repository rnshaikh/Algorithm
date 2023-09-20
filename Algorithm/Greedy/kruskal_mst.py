


"""
    algorithms
    1) we sort edges with ascending order of their weight
    2) iterate through edges for V-1 beacuse(spanning tree will have atleast n-1 edges and mst will have n-1 edges)
    3) if edges does not induce cycle add it into mst
    4) return mst

    for checking cycle:
        we can use bfs and dfs but it gives linear time

    union-find algorithm for const time for checking cycle:
        we maintain leader list for storing leader of each component.
        rank is storing no of vertex in each leader group

        iterate through edge
            check if both vertex have different leader than no cycle
            add into result.
            update leader vertex of this current two vertex
            if rank of leader one is greate then 2nd one update 2nd one with leader one vertex and update rank = rank+rankof(2nd vertex)
            else do opposite of if

            if both vertex have same rank update one of the vertex leader and update rank = rank+1

"""



class Kruskal:

    def __init__(self, v):
        self.V = v
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u,v,w])

    def union(self, u, v, leaders, rank):

        if rank[u] > rank[v]:
            leaders[v] = leaders[u]
            rank[u] = rank[u]+1
        elif rank[v] > rank[u]:
            leaders[u] = leaders[v]
            rank[v] = rank[v]+1
        else:
            leaders[v] = leaders[u]
            rank[u] = rank[u]+1

    def print_mst(self, result):
        for edge in result:
            print("Edge: %s --- %s weight: %s" %(edge[0], edge[1], edge[2]))

    def kruskal(self):

        leaders = [0] * self.V
        rank = [1] * self.V

        for lead in range(self.V):
            leaders[lead] = lead
            rank[lead] = 1

        edges = sorted(self.graph, key=lambda item:item[2])
        result = []
        i = 0
        for j in range(0, len(edges)-1):

            edge = edges[i]
            if leaders[edge[0]] != leaders[edge[1]]:
                result.append(edge)
                self.union(edge[0], edge[1], leaders, rank)
            i = i+1

        self.print_mst(result)

if __name__ == "__main__":

    n = int(input("Enter a no of vertex: "))

    kr = Kruskal(n)

    ch = int(input("Enter a Choice: \n 1) add edges \n 2) MST \n 3)Exit"))

    while(ch):

        if ch == 1:
            n = input("Enter a vertex vertex weight:")
            uvw = n.split(" ")
            kr.add_edge(int(uvw[0]), int(uvw[1]), int(uvw[2]))

        if ch == 2:
            kr.kruskal()
            #print("coming soon")

        if ch == 3:
            break

        ch = int(input("Enter a Choice: \n 1) add edges \n 2) MST \n 3)Exit"))







class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    
    def find_leader(self, leader, i):
        
        if leader[i] != i:
            leader[i] = self.find_leader(leader, leader[i])
        return leader[i]
    
    def union(self, leader, rank, u, v):
        
        if rank[u] < rank[v]:
            
            leader[u] = v
            
        elif rank[v] < rank[u]:
            leader[v] = u
        else:
            leader[v] = u
            rank[u]+=1
    
    def spanningTree(self, V, adj):
        #code here
        
        n = len(adj)
        edges = []
        hash_map = {}
        
        for i in range(n):
            for j in adj[i]:
                if (i, j[0]) not in hash_map and (j[0], i) not in hash_map:
                    edges.append([i, j[0], j[1]])
                    hash_map[(i, j[0])]=1
                    hash_map[(j[0], i)]=1
        
        edges = sorted(edges, key=lambda item: item[2])
    
        leader = []
        rank = []
        
        for i in range(V):
            leader.append(i)
            rank.append(0)
        
        result = []
        i = 0
        e = 0
        
        while e < V - 1:
            u,v,w = edges[i]
            i = i+1
            leader_u = self.find_leader(leader, u)
            leader_v = self.find_leader(leader, v)
            
            if leader_u != leader_v:
                result.append([u,v,w])
                self.union(leader, rank, leader_u, leader_v)
                e = e+1
                
        
        minimum_cost = 0
        for u,v,w in result:
            minimum_cost += w
    
        return minimum_cost
