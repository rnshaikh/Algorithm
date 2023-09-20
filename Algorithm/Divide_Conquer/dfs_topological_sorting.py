"""
    find topological sorting of direct acyclic graph

"""

"""
    if graph is cycle there will be no topological sorting because
    in topological sorting vertex who have most outgoing vertex comes first and there will be one vertex who will
    not have no outgoing vertex (sink vertex) who will come last

    Algorithm:
        1) we are using dfs so we have give order_label = self.v-1
        2) so here we are going to find sink vertex who dont have outgoing vertex and then assigned order label to it
        then decrease that by 1
        3) so in dfs we are always going to have last recursive call of sink vertex one we get all vertex will get traverse in topological order.


        so in general algorithm if we get sink vertex we delete that with all incoming edge
        then again we traverse and find new sink vertex and so on but in dfs we dont have delete vertex bc it
        is traversing in same way

"""


from collections import defaultdict


class Graph:

    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)
        self.order_label = self.v-1
        self.order_list = [0] * self.v

    def add_edge(self, u, v):

        self.graph[u].append(v)


    def dfs(self, vertex, visited):
        visited[vertex] = True

        for i in self.graph[vertex]:
            if visited[i] == False:
                self.dfs(i, visited)

        self.order_list[vertex] = self.order_label
        self.order_label = self.order_label-1


    def top_sort(self):
        visited = [False] * self.v

        for i in range(self.v):
            if visited[i] == False:
                self.dfs(i, visited)

        print("topological order is", self.order_list)

if __name__ == "__main__":

    n = int(input("Enter no of vertex:"))
    gr = Graph(n)

    ch = int(input("Enter no of choice: \n 1.Add Edge \n 2.Find topological sort \n 3.Exit."))

    while(ch):

        if ch==1:
            ver_str = input("Enter vertices between edge (space separated):")
            u, v = ver_str.split(" ")
            u, v = int(u) , int(v)
            gr.add_edge(u, v)

        if ch==2:
            gr.top_sort()

        if ch==3:
            print("Good Bye !!")
            break

        ch = int(input("Enter no of choice: \n 1.Add Edge \n 2.Find topological sort \n 3.Exit."))



