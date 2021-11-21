# Find shortest path from all pair of vertices in graph.


"""
    we have seen dijkstras , bellaman ford algorith for find single source shortest path.
    dijkstras is fast if you dont have negative edge.

    if there is negative edges then bellaman ford algorithm is used

    so to find shortest path from all vertex to every other vertex so we can say that we can use bellaman ford algorithm
    time complexity of bellaman ford algorithm is O(n2)

    for n vertices it will be O(n2) * n  = O(n3)

    but bellaman ford is depending on number of edges so for sparce graph it will be O(n3)
    but dense graph it is O(n4)

    so floyd warshall algorithm is efficent for every case negative path, sparce, or dense
    graph its time complexity is O(n3)


    Algorithm :

        optimal substructure:
            so here there are two cases
            shortest path i j = min (pij , pik+kj)

        so in this recursive algorithm in 1st iteration it check for 0 intermediate vertex.
        2nd iteration find shortest path with 1 intermediate vertex.
        nth iteration find shortest path with n intermediate vertex.



"""




class Floyd:

    def __init__(self, v):
        self.V = v

    def shortest_path(self, graph):

        dist = graph

        for outer in range(self.V):
            for inner in range(self.V):
                if dist[outer][inner] == 0:
                    dist[outer][inner] = float('Inf')

        print("dist", dist)
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                        dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
        import pdb
        pdb.set_trace()
        print("dist matrix: ", dist)



if __name__ == "__main__":


    n = 4
    graph = [[0, 5, 0, 10],
             [0,0,3,0],
             [0,0,0,1],
             [0,0,0,0]]

    fin = Floyd(n)
    fin.shortest_path(graph)








