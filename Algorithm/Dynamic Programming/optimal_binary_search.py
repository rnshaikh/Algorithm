

"""
    input we have given nodes and its frequency of search 
    we have construct binary search tree with minimum average frequency per search

    ex. 1,2,3,4    frequency : 60%, 20%, 15%, 5%

    so in this case  will be binary search tree

    1
     \
      2
       \
        3
         \
          4

    frequency of search node 1 is  1*0.6
    frequency of search node 2 is  2*0.2
    frequency of search node 3 is  3 * 0.15
    frequency of search node 4 is  4* 0.5

    so in short large freqeuncy node shold be as close to root
    small freqeuncy node should be close to leaf node


    we can solve this problem using dynamic programmin

    as there is overlapping subproblem and optimal substructure.

    optimal substructure :

        for node i to j optimum weighted seach cost if we know the root is r
        then left subtree i to r-1 should be optimum bst and right subtree
        r+1 to j shiuld be optimum bst


    recurrence:

        for every 0<=i<=j<=n
                       j
            cij = minr=i {summation k {fk + cir-1 + cr+1 j}}

        this optimal substructure formula narrows down root
        possiblity as well as smallest subproblem  with node is j-i+1



    Algorith:
        take 2-d array A to store weighted search cost of n

        outer for loop control subproblem
        for s = 0 to n-1     s=j-i
            for i= 1 to n
                A[i, i+s] =  we will compute cost considering each node i to i+s as root node r and take min cost from that
                            cost is calulate as  summation of k=i to i+s (fk + A[i][r-1] + A[r+1][i+s])


        return A[1, n]

"""
