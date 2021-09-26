


# Graph

    1) Graph is order pair of a set of vertices or node V and set of edges E
    Graph is non-linear data structure and tree is special type of graph
    2) G = (V, E)
    3) Graph can undirected edges that means we can go from node A to B and vice versa
    3) Grap can have directed edges that mean if edge is directed form A to B then can't travel from B to A
    4) Directed Edge Graph is called Diagraph or Directed Graph and undirected edge graph is called undirected graph
    5) In Graph, Edges Can have weight associated with it to show importance or certain properties. so graph with weight
    edges can called weighted graph and graph with simple edges call unweighted graph.
    6) Graph used in many application's like social networking showing friends (undirected graph), web pages can be shown using
    directed graph, cities link and intracity link can be shown using weighted graph.


# Properties

    1) In Graph no of edges and no of vertices is called cardinality of graph
    |V| = 3 , |E|=10

    2) In directed Grpah then can be mazimum n(n-1) no of edges where n  is vertices
    |n| = 3

    |E| <= 0 <= n(n-1)

    3) In undirected Graph there can be maximum n(n-1) no of edges where n is vertices
    |n| = 4
    |E| <= 0 <= n(n-1)/2

    4) If graph have large no of edges then graph called dense graph in such cases we stored in adjacency matrix

    5) if graph have less no of edges then graph called sparse graph in such cases we stored in adjacency list

    6) self loop : if in graph node/vertices have path to itself is call self loop

    7) multiedge : if in graph nodes have multiple edges between them than it's called multiedge graph

    8) path : path is set of vertices where each adjacent pair is connected.

    9) simple path : in simple path no vertices and no edges is repeated.

    10) trail : in trail, vertices are repeated but not edges.

    11) strongly connected graph : in graph if every vertex is reachable from every other vertex. then it called strongly connected graph.

    12) cyclic graph : where path is start and end on same vertice without any other veritces repetation

    13) acyclic graph : graph called acyclic if there is no cycle in graph.

    14) complete graph : a simple undirected graph in which every pair of distinct vertices is connected by a unique edge.



# Representation:

    1) Graph can be stored using adjacancy matrix or adjacency list if graph is dense then we use adjacency matrix and
    if graph is sparse then we use adjacency list

    2) adjacency matrix : finding adjacent nodes = O(v) , if two nodes is connected O(1), but space complexity O(v2) that is too much for real world problem

    3) adjacency list: finding adjacent nodes = O(v), if two nodes is connected O(v), but space complexity is O(V) + O(E) which is lesser :
                    list can be array, linked list, or binary search tree.
                    most efficient will be binary search tree.


# Application of DFs:

    1) Finding cycle in graph
    2) Finding path between 2 vertex
    3) topological sorting
    4) check if graph is bipartite
    5) Finding Strongly Connected Components of a graph


# Application of BFS:

    1) finding all adjacent nodes
    2) finding path between 2 vertices
    4) Shortest Path and Minimum Spanning Tree for unweighted graph
    5) Peer to Peer Networks:In Peer to Peer Networks like BitTorrent, Breadth First Search is used to find all neighbor nodes.
    6)  GPS Navigation systems: Breadth First Search is used to find all neighboring locations.


