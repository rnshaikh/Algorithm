import sys


"""
Dijkstras's Minimum path from source to each vertex (greed method):

1) take visited list with all vertex False, and min_dist list of tuple which store min dist, prev_vertex for path.
2) first min_dist of all vertex is inf except source vertex.
3) while all vertex is not visisted repeat :
4) find the vertex ver who is not visited and have minimum distance in min_dist list
5) then check its unvisited neigbhour if min_dist[ver][0]+graph[ver][i] < min_dist[i][0] then update distance for vertex i and also update prev_vertex as ver
6) after all unvisited neigbour marked ver as visited.

"""



class Graph:

    def __init__(self, v=0):

        self.V = v
        self.graph = [[0]*self.V for _ in range(self.V)]

    def min_dist_vertex_src(self, min_dist, visited):
        min_di = sys.maxsize

        for i in range(self.V):

            if min_dist[i][0] < min_di and visited[i] == False:
                min_di = min_dist[i][0]
                index = i
        return index

    def print_min_distance(self, src, min_dist):
        print("Distance of each vertex from src %s as follow" %(src))
        for i in range(self.V):
            print("vertex: %s , min_dist:%s" %(i, min_dist[i][0]))

    def print_min_path(self, src, min_dist):

        print("minimum path of each vertex from src %s as follow" %(src))
        for i  in range(self.V):
            path = []
            prev_vertex = min_dist[i][1]
            while prev_vertex != 0:
                path.append(prev_vertex)
                prev_vertex = min_dist[prev_vertex][1]

            path.append(prev_vertex)
            print("Path for vertex %s is as follow" %(i))
            print(path)



    def dijkstras(self, src):

        visited = [False] * self.V
        #store minimum dist + previous vertex in path.

        min_dist = []
        for i in range(self.V):
            min_dist.append([sys.maxsize, 0])

        min_dist[src] = [0,0]

        for i in range(self.V):
            ver = self.min_dist_vertex_src(min_dist, visited)
            for i in range(0, self.V):
                if visited[i] == False and self.graph[ver][i] > 0:
                    if min_dist[ver][0] + self.graph[ver][i] < min_dist[i][0]:
                        min_dist[i][0] = min_dist[ver][0] + self.graph[ver][i]
                        min_dist[i][1] = ver

            visited[ver] = True


        self.print_min_distance(src, min_dist)
        self.print_min_path(src, min_dist)


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
    gr.dijkstras(0)


