


"""Dijkstra's shortest path algorith from source vertex
if weight is negative dijkstras algorithm won't work
"""

"""
    it greedy method : it chooses vertex who has min_dist at every step

    1) take visited list of vertex and min_dist list where all vertex dist is inf except source vertex = 0
    2) loop through vertex call min_dist_ver method to return vertex who has min_dist and who is not visited yet
    3) after getting vertex loop thorugh its adjacent unvisisted vertex check if distance from current is small if small
    update distance
    4) after finshed adjacent unvisited vertex mark ver as visited repeat this.

    running time of dijskrats algo is O(n2)


    if we used minheap running time will be O(v+e log v)
    Following are the detailed steps.
        1) Create a Min Heap of size V where V is the number of vertices in the given graph. Every node of min heap contains vertex number and distance value of the vertex.
        2) Initialize Min Heap with source vertex as root (the distance value assigned to source vertex is 0). The distance value assigned to all other vertices is INF (infinite).
        3) While Min Heap is not empty, do following
        …..a) Extract the vertex with minimum distance value node from Min Heap. Let the extracted vertex be u.
        …..b) For every adjacent vertex v of u, check if v is in Min Heap. If v is in Min Heap and distance value is more than weight of u-v plus distance value of u, then update the distance value of v.
"""

class Graph:

    def __init__(self, v):

        self.v = v
        [[0]*self.v for _ in range(self.v)]



    def min_dist_vertex(self,min_dist, visited):

        min_dist_ver = float('inf')
        index = None

        for i in range(self.v):
            if min_dist[i] < min_dist_ver and visited[i] == False:
                min_dist_ver = min_dist[i]
                index = i

        return index


    def dijkstras(self, source):

        visited = [False] * self.v
        min_dist = [float('inf')] * self.v

        min_dist[source] = 0

        for i in range(self.v):
            ver = self.min_dist_vertex(min_dist, visited)
            for i in range(self.v):
                if self.graph[ver][i] > 0 and visited[i] == False:
                    min_dist_i = self.graph[ver][i] + min_dist[ver]
                    if min_dist_i <  min_dist[i]:
                        min_dist[i] = min_dist_i
            visited[ver] = True

        return min_dist


if __name__ == "__main__":

    gr = Graph(9)
    gr.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];
    print(gr.dijkstras(0))
