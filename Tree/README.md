

# Tree

    1) tree is hiearchial data structure which contain node call root node its childern.
    2) collection of objects that are linked together to define hiearchy.


# properties:

    recursive data structure = we can divide tree into smaller true of same kind. it has one node root node which dont have any parent
    edges = if there are n nodes then there will n-1 edges
    depth of node x = distance between root node to node (x) is its depth
    height of node(x) = longest path betwen node x  and leaf node is height of node(x)




# Binary Tree

    binary tree is trea where each node have atmost two childern which left chid and right child
    each node contained:
    1) data
    2) left child link
    3) right child link



# Why Trees?


    1. One reason to use trees might be because you want to store information that naturally forms a hierarchy. For example, the file system on a computer.
    2. Trees (with some ordering e.g., BST) provide moderate access/search (quicker than Linked List and slower than arrays).
    3. Trees provide moderate insertion/deletion (quicker than Arrays and slower than Unordered Linked Lists).
    4. Like Linked Lists and unlike Arrays, Trees don’t have an upper limit on number of nodes as nodes are linked using pointers.

    The maximum number of nodes at level ‘l’ of a binary tree is 2l.
    The Maximum number of nodes in a binary tree of height ‘h’ is 2h – 1.


    Main applications of trees include:
    1. Manipulate hierarchical data.
    2. Make information easy to search (see tree traversal).
    3. Manipulate sorted lists of data.
    4. As a workflow for compositing digital images for visual effects.
    5. Router algorithms
    6. Form of a multi-stage decision-making (see business chess).





Types Of Binary Tree:


1) Full Binary Tree: it is binary where each node have 2 0r 0 childern. all node except leaf node have 2 childern.

2) complete binary tree: The complete binary tree is a tree in which all the nodes are completely filled except the last level. In the last level, all the nodes must be as left as possible.
                        height = log(n) base 2

3) Perfect Binary Tree:  A Binary tree is a Perfect Binary Tree in which all the internal nodes have two children and all leaf nodes are at the same level.
                        height = log(n+1)base2 -1
                        maximum node at h = 2^h+1 -1

4) Balanced Binary Tree: The balanced binary tree is a tree in which both the left and right trees differ by atmost 1.


# Binary Search Tree:

1) Binary search tree is binary tree where left subtree have value less than or equal to root and right subtree have value greater than root

2) average search, insertion and deletion cost o(log n base 2) balanced binary tree best case and in worst case o(n) in unbalanced binary search tree,
  unorder array/ linkedlist search o(n), insert o(1), deletion O(n)


# Binary Tree Traversal:

1) traversal is visiting each node in tree exactly once in some order

2) types of traversal : 1) Breadth first traversal 2) Depth first traversal

3) Breadth first traversal : in breadth first traversal tree is traverse level wise. level order traversal

4) Depth first traversal : tree is traverse in first all childern on left and right side . first left subtree is completely traverse and then right subtree is traverse.
                            1) pre order traversal : root, left, right
                            2) in order traversal : left, root, right
                            3) post order traversal: left, right, root




# heap:

    heap is special tree data structure where tree is complete binary tree.
    there two types of heap which also binary heap.
    1) Min Heap : min heap is complete binary tree where root nodes have smallest value than all its childer node and which recursively true
                  for all subtree

    2) Max heap : max heap is complete binary tree where root nodes have largest value than all its childern and it recursively true for all
                  subtree



    if binary heap store in array representation in level order then
    for any ith node

    parent node : i-1/2
    left child node: 2*i+1
    right child node : 2*i+2


# Applications of heap:

    1) Heap sort : heap is used in heap sort which sort element O(nlogn) time
    2) PriorityQueue: Priority Queue is efficently implement using binary heap it perform insert, delete, extractmax operation O(log n) time.
    3) Graph Algorithms: The priority queues are especially used in Graph Algorithms like Dijkstra’s Shortest Path and Prim’s Minimum Spanning Tree.
    4) many other examples like find kth largest element in array, sort almost sorted array, merge k sorted array.


# operation on min heap:

1) insert : it add element in heap : o(log n)
2) delete : it remove element from heap : O(log n)
3) getmin : get min value from heap : O(1)
4) extractmin : remove min value from heap: O(log n)
5) decreaseKey : decrease key value of node if decrease value greater than parent no need fix heap else need to fixed violated heap
                O(log n)
