# find shortest path algorithm using bellaman ford algorithm


"""
    dijkastras algorithm is greedy algorithm and it does not work for negative edge directed graph
    dijkstras algorithm also does not detect negative edge cycle.
    dijkstras algorithm time complexity is v+e log v using minheap.
    in dijkstras algorithm does not work for distributed system where complete graph is not given

    but bellaman ford algortihm is worked for both. but time complexity of bellaman ford is O(v.e)
    bellaman ford algorithm works for distributed system.


    Algorithm:

        1) take dist[] list with all vertex initally inf except source vertex as 0
        2) recurse through v-1 times as shortest path contain atmost v-1 edges
            3) every recursion check every edge if dist[v]  < dist[v] + weight current edge then update dist[v]
        4) after finding out shortest distance loop thorugh all edges check for negative cycle
            if dis[v] > dist[u]+weight of current edges return negative cycle


        at every iteration it find out shortest path with i edges.
        at first iteration it find out shortest path with 1 edge.
        at 2nd iteration it find out shortest path with 2 edge.

"""



class Graph:


    def __init__(self, v):
        self.V = v
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u,v,w])

    def print_graph(self, dist):

        print("shortest path is as follws: vertex :  distance from the source")
        for i in range(self.V):
            print("%s ------ %s"  %(i, dist[i]))

    def bellaman(self):

        dist = [float('Inf')] * self.V
        dist[0] = 0
        print("distance, graph", dist, self.graph)

        import pdb
        pdb.set_trace()

        for i in range(self.V-1):

            for u,v,w in self.graph:
                if dist[u] != float("Inf") and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w

            import pdb
            pdb.set_trace()
            print("at %s iteration: %s" %(i, dist))

        for u,v,w in self.graph:
            if dist[v] != float('Inf') and dist[v] > dist[u] + w:
                print("Graph contain negative cycle.")
                return

        self.print_graph(dist)


if __name__ == "__main__":

    v = int(input("Enter a number of vertices:"))
    gr = Graph(v)

    ch = int(input("Enter a choice : \n 1) add edge  \n 2) find shortest path \n 3) Exit"))

    while(ch):

        if ch==1:
            edge_i = input("Enter edge as follows: u v w")
            u,v,w = edge_i.split(" ")
            u,v,w = int(u), int(v), int(w)
            gr.add_edge(u,v,w)

        elif ch==2:
            gr.bellaman()

        elif ch==3:
            print("Good Bye")
            break

        ch = int(input("Enter a choice : \n 1) add edge  \n 2) find shortest path \n 3) Exit"))










isNegativeWeightCycle(n,edges){
       //code here
       
        if(!edges.length){
            return 0
        }
        
        
        let dist = new Array(n).fill(Number.POSITIVE_INFINITY)
        dist[0] = 0
        for(let i = 0 ; i <= n-1; i++){
           if(i < edges.length){
               let[u, v, w] = edges[i]
               
               if (dist[u] != Number.POSITIVE_INFINITY && dist[v] > dist[u]+w){
                   dist[v] = dist[u]+w
               }
           }
        }
        
        for (let ele of edges){
            let [u, v, w] = ele
            if (dist[v] != Number.POSITIVE_INFINITY && dist[v] > dist[u]+w){
                return 1
            }
        }
        
        return 0