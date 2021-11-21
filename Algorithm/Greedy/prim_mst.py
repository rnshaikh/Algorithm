
"""
    Prim's is greedy algorithm at each step it choses vertex with min_cost

    1) initiated visited list vith all vertex False, min_cost all inf, parent to store last vertex.
    2) start from 0 update min_cost with index 0 value 0
    3) iterate through vertex :
    4) find min_cost unvisited vertex
    5) for all adjacent vertex of u of v check if min_cost[u] < graph[v][u] if it is update min_cost[u] = graph[v][u] update parent[u] = v
    6) marked vertex v as visited

    time complexity of aove algorithm is O(V2)

    bu we can use min heap to reduce time complexity to O(v+e log v)

    so here we can use min heap to store minimum cost of each vertex.

    1) initally construct min_heap with souce cost 0 all other inf
    2) while heap is not empty :
    3) extract min_cost vertex from heap
    4) for all adjust vertex of v update min_cost if is lesser than its previous value in heap. adjust min heap

"""



class Graph:

    def __init__(self, v):
        self.V = v


    def min_cost_vertex(self, visited, min_cost):

        min_index = 0
        min_c = float('inf')

        for i in range(self.V):
            if visited[i] == False and min_cost[i] < min_c:
                min_index = i
                min_c = min_cost[i]

        return min_index


    def prims(self, graph):

        visited = [False] * self.V
        min_cost = [float('inf')] * self.V
        edges = [0] * self.V
        min_cost[0] = 0

        for i in range(self.V):

            vertex = self.min_cost_vertex(visited, min_cost)

            for j in range(self.V):

                min_cost_j = graph[vertex][j]
                if graph[vertex][j] > 0 and visited[j] == False and min_cost[j] > min_cost_j:
                    min_cost[j] = min_cost_j
                    edges[j] = vertex

            visited[vertex] = True

        print("edges", edges, min_cost)
        self.print_mst(min_cost, edges)


    def print_mst(self, min_cost, edges):

        for i in range(1, self.V):

            print("Edge : %s --- %s Cost: %s" %(i, edges[i], min_cost[i]))




g = Graph(5)

graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]

g.prims(graph)


