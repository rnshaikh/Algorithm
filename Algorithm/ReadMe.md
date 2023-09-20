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


    1) Binary Search Tree:
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

            left rotation : in left rotation parent is swap with right child

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


    2) Hash Table : hash table is array of objects stored in associative manner. its index
    has unqiue value which is calculated by hash function

    hash function : map or object to fixed unque value so that searching become fast in constant time

    hash table have time complexity of O(1) for insertion, deltion and searching

    it used for fast searching problems, like checking duplication, checking nodes or configuration is already visited in
    game graph. blocking network traffic.



    hashing : hashing take the input gives unique index where object is store
    there is property of hash function
    1) uniformly distributed : so objects should be uniformly distributed
    2) less collision : collison of objects in same key should be less.
    2) hashing algorithm : should be easy and run in constant time


    avoid collision :
    1) chaining: so here we store linked list at every index. so if there is more than 2 objects. it will be add as new node
                 space requirement is more here. but deletion is faster

    2) open addression : in open addressing there will one object at each index if it is already fill then you try next until it is empty it called
                         linear probing

                         onther one is if index is already filled then you hash again which give new index it call double hashing

                         here space requirement is less but deletion is difficult

    Quick And Dirty Hash function:
        1) take phonenumber or name convert into integers using compression function like mod n convert into index

        how many buckets or size of array should be:
        1) should be prime number
        2) not close to power  of 2 and power of 10


    load factor of hashing (alpha):
        load factor of hashing define how well datasets are spread in bucket

        formula : no of objects inserted / no of buckets

        in chaining load factor can a greater 1 than one beacuse every bucket have more than one object in linked list
        but in open addressing load factor should be a less than 1


        there is no prefect has function every hash function perform linear for some data sets

        so to imporove hash function we can do universal hashing.

        1) use cryptography for hashing
        2) randomization : use family of hash function and choose random hash function during runtime

    univeral hash function :

        defination : let h be the set of hash function h = {h1, h2, hn}
        and u is universal data set u = {0, 1, n}
        then x,y belong to h

        then probability of index of x, y data collision is  < = 1/n  where n is no of buckets


    proof of universal hash function in chaining:

        if we use random famliy of hash function and maintain load factor alpha constant then
        hash function searching will have constant time


    proof of universal hash function in open-addressing:

        under heuristic assumption expected insertion/lookup time
        = 1/1-alpha where alpha is load factor

        in Linear probing above assumption does not satisy,

        expected searching/insertion time is 1/(1-alpha)2 depends on alpha


    3) Bloom Filter:
        it is another data strature like hash table which is used for fast insertion and
        searching

        it also used array and family of hash function

        pros over hash table
        1) space efficient : does not store complete object just remembar it return true/false

        cons :
        1) deletion is not possible
        2) can have false positive : return true even if object is not inserted.

        in bloom filter false positive error rates depending no bits per object.

        as no bits increases error rate goes down.



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



     another example scheuling problems: if job have priority and time required for execution in this case
     there is 3 case 1) if jobs have same priority and diff time then job with less time will execute first
                     2) if job have diff priority and same time then job with high priority will execute first
                     3) if job have diff priority and diff time then in this case we create scroe base on both priority and tim
                     let say first optimal function do the difference p-t
                     second one do the division p/t
                     in this case 2nd will be most efficient so we will sort job according to higher weight and execute it


    proof of correctness of greedy algorithm can be prove by proof of contradiction.
    you have to assume given soltution is wrong there another optimal solution you have falsify that solution

    for example in above scheduling problem consider there is another optimal solution
    in that consider two job i and j and i execute first and then j  and i > j

    if we exchange there scheduling then j time will decrease by i time and its cost will also goest down wjti
    ith job time will increase by ti and it cost will be decrease as j > i

    so here cost will get imporve thats why another is not optimal solution so our greedy is optimal solution

    ex. dijkstra shortest path algorithm, MST, scheduling


# MST (Minimum Spanning Tree)(Greedy algorithm):

    Minimum spanning tree is minimum cost tree which have two property:
    1) it does not have any cycle
    2) it is will connect (for any vertex there is path to any other vertex)

    there two alogrithm for minimum spanning tree
    1) prims algorithm : prims alogrithm select vertex with optimum cost find min_cost to every adjacent vertex at each steps
    2) kruskals algorithm: kruskal algorithm select min_cost edge and check if create cycle if not added minimum spanning tree.


    1) prims algorithm:
        it is similiar to dikstras shortes path algorithm
        it choses vertex with minimum cost at every iteration
        update it adjacent vertex cost if its minimum than in min_cost array
        add that in mst.

        time complexity of prims algorthm is same as dikstras O(v2) and using heap it is O(v+e log v)
        time complexity of prims algorithm with min heap is O(v+e log v)
        min heap is used to store min_cost of each vertex.


        correctness of prims algorithms:
        as its greedy algorithm we can prove it by contradiction

        assumption that let e be the edge in graph
        and there is cut A B then e is cheapest crossing edge that should
        be included in minimum spanning tree

        no cut lemma:
            if there is cut A and B and there is no crossing edge then
            graph is not connect

        double cut lemma:
            it there is 2 crossing edge which get back to same vertex then
            there is cycle.

        so in proof we assume that there is e- edge which less cheaper than e that can include in mst
        so that cost will less than if we inclide e in mst.

        so it is possible if including e create cyle in mst then we can't include e so we include e`
        which create mst.



    2) Kruskal algorithm:

        it is also one of greedy algorithm for finding minimum spanning tree.
        1) sort all edges in ascending order
        2) iterate thorugh edge.
        3) if edge is unvisited and does not form cycle then added to mst.

        time complexity of kruskal's algorithm O(v2)
        time complexity of kruskal's algorithm with union-find algorithm is O(v+e log v)
        here bottleneck is to check if cycle will occure if add current edge
        for this we can use bfs or dfs which takes linear time but union-find take constant times.


        correctnsess of Kruskal Algorthm:
        as it is greedy algorithm we choose as edges in ascending order every time
        we can use proof by contradiction

        first we are gonna prove kruskal algorithm output spaning tree
        then we are gonna prove that it is mst.

        1) proving it out mst : 1) it should not contain cycle 2) it is well connected

        according to no cut lemma : if there is cut A,B and there is no crossing edge then graph is not well connected.

        according to single cut lemma : if thers is one one edge crosses cut A,B then it should not produced cycle in graph

        and in kruskal algortihm first crossing edge it sees will be included in mst

        in kruskal algorithm that first edge will be cheapest as we sort edges in ascending order
        so kruskal algorithm output minimum spanning tree.



        Union-Find:
            1) data is divided into groups
            2) it can find object is situated in which group
            3) it can also merge two group into single using union

            so in kruskal algorithms this groups are created by linked to leader arbitary vertex in each group
            so cycle is check is done by if both vertex have some leader if yes then cycle is exist if not then cycle is not existed
            after adding edge we have to merge component which nothing but updating leader in one component which has less vertex.


# Huffman Code(Greedy Algorithm):

    Huffman Code is variable length prefix free binary codes algorithm for encoding characters.

    so in encoding character into binary code you can used fixed bit codes in triditional algorithm but it takes more memory
    so for efficient memory we need variable length coding for characters.

    in variable length character there induces ambiguity if we dont care.
    for example.
            A B C D
            0 00 1 11

    if we have binary code 00011

    so in this case there is more than 1 string that can decode from above binary codes
    1) ABD 2) AAACC 3) BAD

    so to resolved ambiguity in code we need prefix free codes.
    in prefix codes character code should not start with any other value.
    for ex.
    A - 0
    B - 11
    c - 10
    D - 001

    0 11 11 10
    A B B C

    Huffman Coding Algorith for prefix free binary coding:

    in huffman coding you have given string you have to produced variable length prefix free code
    you have also given frequency of each character:

    1) while there is no two character to merge:

        choose least freequent two character merge them also merge there frequence

    2) build a binary tree with edge 0 and 1


    for example A B C D
    A - 50%
    B - 30%
    c - 15%
    D - 10%

    1) we are going to choose least frequenct 2 character merge them there freq.


    CD  A B
    25  50 30

    2)
    CDB  A
    55   50


    3) we need consturct binary tree with o and 1 edge 0 left 1 right edge


        node
      0  /\ 1
        /  \
        A  node
            0/\ 1
            B node
              0/\ 1
              C D

     A= 0  B= 10  C=110 D=111


     time complexity is O(n2)
     but we can use min heap data structure to get O(n log n) time


# Dynamic Programming:

    Dynamic programing is optimization over recusion. it store the solution of subproblems so if needed later we can take it from
    there. this simple solution reducses time complexity from exponential to linear


    Dynamic programming is algorithm paradigme which solves complext problem by dividing into smaller subproblem and storing solution
    of subproblem to avoid computing same result again


    if problem have can divide into subproblem and subproblem have optimal solution than we can use dynamic programming

    key features of dynamic programming.

    1) identfy subproblem for main problem

    2) can quickly solve larger subproblem given the solution to smaller subproblem

    3) after solving all subproblem can quickly compute the solution to  main problem


    problem should have following property that suggest that problem can be solve using dynamic programming

    1) overlapping subproblem
    2) optimal substructure

    overlapping subproblem :
        dynamic programming divide complex problem into sub problem. it solve this subproblem store solution.
        so that solution to this subproblems need again and again in dynamic programming.

        if solution of subproblem is not needed than there is no use of using dynamic programming
        fo ex. binary search does not need solution of subproblem

        fib num : we need solution of last 2 num to compute current fib so we can use dynmica


    optimal substructure :

        problem have optimal substructure if optimal solution of problem can be obtain from optimal solution of subprolems
        this same as in greedy algorithm which choose best possible solution at time in hope it leads optimal solution to
        main problem.

        ex. shortest path algorithm.


# polynomial time problem (p) and non deterministic polynomial time problem (np complete):

    polynomial time problem : it problem for which known algorithm is exist who solved it in polynomial time
    O(n^k)   n = length of input size
    ex. all problem sorting, searching, mst, shortest path algorithm are polynomial time algorithm


    np complete problem : if problem for which no known algorithm is exist which solved it in polynomial
    time is called np complete problem or non deterministic polynomial time problem.
    ex. travelling salesman problem, knapsack problem.


    how to determine whether problem is np complete problem.

    1) reduction  and completness: reduced given problem pi to pi2

    pi can be reduced to pi2 if function which solves pi2 can solved pi in polynomial time
    but if pi2 itself is np completed then we can say that pi is also np complete problem

    so if we found polynomial solution to pi then it will also solved pi2.


    problem is np compelte prolem if:
        1) solutions always have length polynomial in input size.
        2) purposed solution can be verified in polynomial time.


    approches for solving np complete problems:

    1) identify computational ease for special cases or input:
        weighted inpendant set for path graph have linear time
        but for general graph it np complete problem

    2) heuristic : proposing algorithm which is not correct but minmum.

    3) exponential time but better than brute force.
        here can use dynammic programming to solve problem which will
        have exponential time but more correct than brute force.























