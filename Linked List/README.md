

#  Linked List

    Linked list is collection of element of same type which is not stored in contagious block of memory.
    Linked list containing list of node where each node has data part and pointer to next element.
    there on pointer head which point first element of node.


# Advantage
    Array is fixed size and insertion/ deletion is costly in array for ex. if wand delete middle element you adjust other element.
    linked is dynamic
    linked list insertion/deletion is faster than array

# Disadvantage

    Linked list random access is not possible. we have search element sequentially starting from first node . binary search is not possible in
    default linked list implementation.
    extra space is required in each node to store address of next node.
    Not cache friendly. Since array elements are contiguous locations, there is locality of reference which is not there in case of linked lists.


# Representation

    1) linked list contained list of node.
    2) each node contain two part 1) data value 2) pointer to next node.
    3) thre is head node which point to first element of node





# Doubly Linked List

    In Doubly Linked list every node have extra pointer to previous node so that traversal in doubly linked list done in
    both direction.

# Advantages over singly linked list

    In dobuly linked list deletion of node is done faster as every node have pointer to previous node.
    A DLL can be traversed in both forward and backward direction.
    We can quickly insert a new node before a given node.


# Disadvantages over singly linked list

    Every node of DLL Require extra space for an previous pointer.
    All operations require an extra pointer previous to be maintained.




# Circular Linked List

    Circular linked list is linked list where there is no nul at end. last element is point to first element.
    all nodes are connected to form a circle

# Advantages:
    Any node can be a starting point. We can traverse the whole list by starting from any point. We just need to stop when the first visited node is visited again.

    Useful for implementation of queue. we don’t need to maintain two pointers for front and rear if we use circular linked list.
    We can maintain a pointer to the last inserted node and front can always be obtained as next of last.

    Circular lists are useful in applications to repeatedly go around the list. For example, when multiple applications are running on a PC,
    it is common for the operating system to put the running applications on a list and then to cycle through them,
    giving each of them a slice of time to execute, and then making them wait while the CPU is given to another application.
    It is convenient for the operating system to use a circular list so that when it reaches the end of the list it can cycle around to the front of the list.

    Circular Doubly Linked Lists are used for implementation of advanced data structures like Fibonacci Heap.

