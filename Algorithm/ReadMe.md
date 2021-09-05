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

