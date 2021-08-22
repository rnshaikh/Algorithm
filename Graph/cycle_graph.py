
from collections import defaultdict

"""
    1) take visited list to mark visited vertex and take recurstack to keep current track of vertex.
    2) then take first vertex to dfc recursive func
    3) mark visited and recurstack true for current vertex
    4) check if cureent neibhour vertex is visited or not if visted return true else step 5
    5) loop thorugh neighbour and call recursive func with visited curr stack if return true
    6) recursive func return True then cycle existed else false
"""


"""
    undirected graph:
    1)  you have to take visited and parent of current else everything is same
    2) in neibhour loop check if neibour alredy visited and neibour node  is not parent of its parent.

"""

class Graph:

    def __init__(self):

        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def cycle_util(self, ver, visited, recurStack):

        visited[ver] = True
        recurStack[ver] = True

        for neigbour in self.graph.get(ver, []):
            if visited[neigbour] == False:
                if self.cycle_util(neigbour, visited, recurStack) == True:
                    return True
            else:
                return True

        recurStack[ver] = False

    def detect_cycle(self):

        visited = [False] * (max(self.graph) + 10)
        recurStack = [False] * (max(self.graph) + 10)

        for i in self.graph:
            start=i
            break

        if self.cycle_util(start, visited, recurStack) == True:
            print("Cycle Exist")
        else:
            print("Cycle Not Exist")


    def undirected_cycle_util(self, ver, visited, parent):

        visited[ver] = True
        for neighbour in self.graph[ver]:

            if visited[neighbour] == False:
                if(self.undirected_cycle_util(neighbour, visited, ver)):
                    return True

            elif neigbour != parent:
                return True

        return False

    def detect_undirected_cyle(self):

        visited = [False] * (max(self.graph) + 10)

        for i in self.graph:
            start=i
            break

        if self.cycle_util(start, visited, -1) == True:
            print("Cycle Exist")
        else:
            print("Cycle Not Exist")


if __name__ == '__main__':

    graph = Graph()

    k = int(input("""Enter one of the below option :
                    1) Insert
                    2) Detect Cycle
                    3)Exit"""))

    while(True):

        if k == 1:
            a,b = input("Enter edge between 2 vertices:").split(" ")
            a = int(a)
            b = int(b)
            graph.add_edge(a,b)

        if k == 2:
            graph.detect_cycle()

        if k == 3:
            print("Good Bye!!!")
            break;

        k = int(input("""Enter one of the below option :
                    1) Insert
                    2) Detect Cycle
                    3)Exit"""))

