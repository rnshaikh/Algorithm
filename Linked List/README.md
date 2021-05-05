

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
