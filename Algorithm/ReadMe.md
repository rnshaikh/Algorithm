# Algorithm

    it is fixed set of steps of procedure to convert input into desired output

    there are different algorithm designed paradigm namely
    1) Divide And Conquer
    2) Dynamic Programming
    3) Backtracking
    4) Greedy


# Algorithm Running time:

    it how many operation alogrithm performed or how many lines of code algorithm executes.
    it denoted by big Oh notation.



# Guiding Principle of analysis of algorithm:

    alogrithm is analyze using running time or time complexity. for this we use big Oh notation which gives
    how many operations algorithms perform roughfly.

    there is worst-case complexity : where we dont assume any input size, type or domain knowledge
    we just give time required to execute algorithm

    there average-case complexity : where we assume specific input which used frequently. we need to know domain
    knowledge and all that

    asymptomatic analysis: it takes time required for algorithm for large numbers of input size.
    high level reasoning about running time of algorithm. doest not consider constant factor.

    there 3 guiding principle for defining fast algorithm:
        1) worst-case complexity : alwayze analyze algorithm in worst-case complexity without assuming any conditions
        2) Ingore constant factor : in time complexity we remove contants factor which is depends on machine or programmer
        3) growth rate of algorithm: as input size grows to large how algorithms for perform should be taken into consideration


    Asymptomatic Notation:
    big Oh O : it gives upper bound of running time of algorithm
                t(n) = O(f(n)) if there is constant c such that
                t(n) <= c.f(n)

    omega W : it gives lower bound of running time of algorithm
                t(n) = W(f(n)) if there is contant c such that
                t(n) >= c.f(n)


    theta n : it gives equal bound of running time of algorithm
                t(n) = theta(n) if there is contant c such taht
                t(n) = c.f(n)



# Divide And Conquer:

    in divide and conquer main problem is divided into many subproblems of same type
    this subproblems are solved and results are combined which in turned gives result of main problem.
    it is recursive stratergy.

    1) Kartsuba multiplication
    2) Merge Sort


    # merge sort:
        1) In merge sort list is divied recursivly by 2 until base case there 1 element left in each list
        2) list are recursively merge to gives sorted list

    # running time of merge sort:

        1) list of n : for this it recursively divide list to n/2
        2) recursive call for divide until each list has 1 element is exactly no of time we divide n/2 until result is 1 or less
        that is log n
                    2

        3) for merge operation it check element in 2 array sort in 3rd which takes 6n operations.

        4) in recursive tree at level j there will be 2 raise j lists and in each list there will n/2 raise j elements

        time complexity of merge sort = O(nlogn)




# Master Method (Theorm):

        master method is black box for solving recurences or calculating running time of recursive algorithm

        assumption : it assumed that all of the subproblems in divide and conquer are same size.


        running time of recursion:
        1) base case -  T(n) <= a it is constant for all sufficiently small n.

        2) for larger n or in recursive call:
            T(n) <= aT(n/b) + O(n^d)

         where a = number of recursive call  >=1
         b = input size shrinkage factor > 1
         d = exponent running time of conquer step or outside recursive call >=0


        proof in recursion tree:
        thre are three case
        1) same amount work done at each level : a = b^d - root dominates n^d*logn
        2) amount work decrease with level : a  < b^d - root dominates : n^d
        3) amount work increases with level : a > b^d : no of leaves : n^log a to base b


        so there are three cases for checking running time in master method as follows:

        T(n) =   if a = b^d    O(n^d log n)
                 if a < b^d    O(n^d)
                 if a > b^d    O(n ^ log a to base b)


        example :
        1) merge sort
            a = 2
            b = 2
            d = 1   a = 2 b^d = 2

            a = b^d
            T(n)  = O(n^d logn)
            O(n^1 log n)
            O(nlogn)


        2) binary searh:
            a = 1
            b = 2
            d = 0    a=1  b=1
            if a = b^d
            T(n) = O(n^d logn)
            T(n) = O(n^0 log n)
            O(log n)


        3) strassen matrix multiplication
            a = 7
            b = 2
            d = 2    a = 7  b^d = 4
            a>b^d
            O(n loga to base b)
            O(n log72)
            O(n^2.81)



# Comparison based sorting has lower bound runing time of O(n log n)

    1) merge sort, quick sort, heap sort

    if there n number to sort in array then
    comparison based sorting to n! comparison
    that means algorithm executes  <= 2K no comparison

    pigon hole principle : n+1 hole with n pigon atleast 1 hole will more than 1 pigon

    n! <= 2^k

    n/2 log n/2 <= k

    k <= n logn



# minimum cuts in graph

    cuts : it is dividing vertices into two no-empty set

    minimum cuts : it is cuts who have few number of crossing edges in two sets.


    Application:
        1) it is used to detect weakness in network
        2) communiy detection in social networks



    finding minimum cut in graph:

    # randomized contraction algorithm:
        1) while vetrices > 2:
        2) randomally choose edges contract connecting vertex u and v . update other edges of u and v to this
        new edge. it create parallel edges and sel loop
        3) remove self loop


    here we choose edge randomly so it does not give success ouput everytime so success probability of
    this algorithm is 2/n(n-1) >= 1/n2
    where n is number of vertices.

    as this alogrithm success probability is very low then we have give many trails until we found minimum
    cut. but how trial do we need to increase success probability.

    if we take n2 no trial then probabilty of success is 1/n

    it is running time is O(n2m)

    where n = no of vertex while m is no of edges


    maximum nof minimum cut:
    ascyclic graph has minimun n-1 minimum cuts and maximum n(n-1)/2 minimum cuts

    n-cycle graph has minimum n(n-1)/2 minimum cuts



# Graph Search:

    graph search is traversing all vertices of graph in particular order
    there two types of graph search:
    1) BFS
    2) DFS

    1) BFS : It is level wise it traverse all adjacent node of current node in queue until last level
             it is used queue for storing vertices

    2) DFS : it is traverse through depth until leave node then go to adjacent node. it uses recursion for
            traversing child or adajcent node


    BFS :
        1) BFS is used to find shortest path in graph
        2) BFS is used to check connected component in undirected graph


    DFS :
        1) DFS is used to check connected component in direct graph
        2) DFS is used to do topological sorting in acylic directed graph
        see topological order program.


# Greedy Algorithm:

    greedy alogrithm is technique which choses best solution at that moment. it is choses locally optimal solution in a hope that it leads to
    optimal solution to global problem

    greedy algorithm is not always correct

    it is hard proof correctness of greedy algorithm


    when to choose greedy algorithm

    if you have some objective function. you have find optimal of that objective then you can choose greedy algorithm
    to choos optimal objective at every step

    problem must contain 2 component :
        1) problem has optimal substructure. sub problem has optimal solution which lead to optimal solution to main problem.
        2) It has a greedy property (hard to prove its correctness!). If you make a choice that seems the best at the moment and solve the remaining sub-problems later, you still reach an optimal solution. You will never have
          to reconsider your earlier choices.


    for example.
        if you want schedule job with its execution time. you have to execute many job in given time period
        in this case can use greedy algorithm which will choose job with less execution time at each step


    proof of correctness of greedy algorithm can be prove by proof of contradiction. you have to assume given soltution
    is wrong there another optimal solution you have falsify that solution


    ex. dijkstra shortest path algorithm, MST, scheduling


#  Randomized Algorithms

    problem : we have get ith samllest number from unsorted order

    one solution is reduced selection to sorting sort using merge sort then give it smallest
    number
    but running time for this algorithm is O(n log n) we can do better than tha


    second solution : used quick sort but in quick choos random pivot element which divide array into 25:75 list
    after we place pivot its rightful position than
    check if i == j return reurn j th element
    if j > i then  ith index will be on left part so send 1st part ofy array, j-1, ith index
    if j <i then ith index will on right side so send 2nd part, n-j , i-jth index


    in deterministic solution:
            we just choose pivot element as medians of median
            we divide array into 5 array of 5 element
            find out median of each array
            then find out median of median array
            choose that as pivot element


# Data Strutre:

    heap : min/max O(1)
    binary search tree : balanced fives insertion, deletion, searching in O(logn)


    Binary Search Tree:
        in binary search tree left subtree have value less than root node and right subtrees have have value greater
        than root node.

        its time complexity depend on height if it is balanced binary search tree the it has best time
        complexity O(log n) for insetion, deletion and searching

        so there is variant of binary search tree which can ensured that we will have perfectly balanced height of
        binary search tree

        1) Red - Black binary search tree
            red black tree is binary search tree where each node have either red or black
            color and it hold following properties.

            1) root node always be black

            2) node is read then it's childern will not be a red that means red node should not be adjacent.

            3) every root-null path  have same no of black node

            this red-black tree gaurantee that height of tree with n nodes
            will be <= 2log(n+1)
            height <= 2log(n+1)

        operation : rotations
            1) self balancing binary search tree like read-black, avl , b tree do rotations to maintain
            binary search property

            left rotation : in right rotation parent is swap with right child

            here right child become root parent become left child, parent left child will same
            righ child's left child become right child of parent, right child's right child will be same

            right rotation : in right rotation parent is swap with left child


        operation : insetion/ deletion

        insertion : initial insertion is same as binary search tree insert new node depending its value

        coloring: we can violate 2 property that no read node should be adjancent it is easier to fix than 3rd one

        so if we color new node red than will check parent if it is black no need rotate it already stisfy property

        but case 1:
                if parent of new node is red and it's parent is black it's sibling is also read then
                we invert read color of two sibling to black and parent of parent will be read,
                do this until root node if root node become red
                then just make it black so that all root-null path have one extra black node

        case 2:
                if parent is read , its parent of parent is black, its sibiling is also black

                then we are going to 2-3 rotation and recoloring.


    Hash Table : hash table is array of objects stored in associative manner. its index
    has unqiue value which is calculated by hash function

    hash function : map or object to fixed unque value so that searching become fast in constant time

    hash table have time complexity of O(1) for insertion, deltion and searching

    it used for fast searching problems, like checking duplication, checking nodes or configuration is already visited in
    game graph. blocking network traffic.





